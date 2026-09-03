<?php
/*
 * Olimann — Constraint Audit form handler.
 *
 * Sends the request by authenticated SMTP through your Hostinger mailbox (reliable),
 * and falls back to PHP mail() when no SMTP password is configured.
 *
 * SET-UP (once): create the mailbox in hPanel → Emails, then either
 *   a) copy api/config.sample.php to api/config.php and put the mailbox password in it
 *      (config.php is never overwritten by a site re-upload), or
 *   b) edit the defaults right here.
 */
declare(strict_types=1);

$cfg = [
    'to'        => 'info@olimann.com',      // receives audit requests
    'from'      => 'info@olimann.com',      // sender; must be a mailbox on the domain
    'smtp_host' => 'smtp.hostinger.com',
    'smtp_port' => 465,                     // 465 = SSL, 587 = STARTTLS
    'smtp_user' => 'info@olimann.com',
    'smtp_pass' => '',                      // mailbox password; empty = fall back to mail()
];
if (is_file(__DIR__ . '/config.php')) {
    $override = include __DIR__ . '/config.php';
    if (is_array($override)) { $cfg = array_merge($cfg, $override); }
}

$lang   = (($_POST['lang'] ?? 'en') === 'de') ? 'de' : 'en';
$thanks = $lang === 'de' ? '/de/engpass-analyse/danke/' : '/constraint-audit/thanks/';
$back   = $lang === 'de' ? '/de/engpass-analyse/'       : '/constraint-audit/';

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') { header('Location: ' . $back, true, 303); exit; }

/* honeypot + time trap */
if (!empty($_POST['fax'])) { header('Location: ' . $thanks, true, 303); exit; }
$ts = (int)($_POST['ts'] ?? 0);
if ($ts > 0 && (time() - $ts) < 3) { header('Location: ' . $thanks, true, 303); exit; }

$line = static function (string $k, int $max = 200): string {
    $v = (string)($_POST[$k] ?? '');
    $v = preg_replace('/[\r\n\t]+/', ' ', $v) ?? '';
    return mb_substr(trim(strip_tags($v)), 0, $max);
};
$text = static function (string $k, int $max = 4000): string {
    return mb_substr(trim(strip_tags((string)($_POST[$k] ?? ''))), 0, $max);
};

$name    = $line('name');
$company = $line('company');
$role    = $line('role');
$website = $line('website');
$email   = $line('email');

if ($name === '' || $company === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    header('Location: ' . $back . '?error=1#audit-form', true, 303); exit;
}

$pile = [];
if (isset($_POST['pile']) && is_array($_POST['pile'])) {
    foreach (array_slice($_POST['pile'], 0, 12) as $p) { $pile[] = mb_substr(strip_tags((string)$p), 0, 80); }
}
$pileOther = $line('pile_other');
$revenue   = $line('revenue', 40);
$hc = [];
foreach (['hc_sales' => 'Sales & marketing', 'hc_delivery' => 'Delivery & operations', 'hc_support' => 'Support', 'hc_admin' => 'Admin'] as $k => $label) {
    $v = $line($k, 10); if ($v !== '') { $hc[] = $label . ': ' . $v; }
}
$q4 = $text('double');
$q5 = $text('tools');
$q6 = $text('costheavy');

$body  = ($lang === 'de' ? "Neue Engpass-Analyse-Anfrage" : "New Constraint Audit request") . "\n";
$body .= str_repeat('=', 40) . "\n\n";
$body .= "Name:     $name\nCompany:  $company\nRole:     $role\nEmail:    $email\nWebsite:  $website\nLanguage: $lang\n\n";
$body .= "Where work piles up:\n  " . ($pile ? implode("\n  ", $pile) : '-') . ($pileOther !== '' ? "\n  Other: $pileOther" : '') . "\n\n";
$body .= "Revenue band: " . ($revenue !== '' ? $revenue : '-') . "\n";
$body .= "Headcount:    " . ($hc ? implode(' | ', $hc) : '-') . "\n\n";
$body .= "Double the customers tomorrow - revenue doubles or something breaks?\n" . ($q4 !== '' ? $q4 : '-') . "\n\n";
$body .= "Tools in sales, delivery, support:\n" . ($q5 !== '' ? $q5 : '-') . "\n\n";
$body .= "Most cost- and resource-heavy workflow/department vs. its return:\n" . ($q6 !== '' ? $q6 : '-') . "\n\n";
$body .= str_repeat('-', 40) . "\nSent " . date('c') . " from " . ($_SERVER['REMOTE_ADDR'] ?? '?') . "\n";

$subject    = ($lang === 'de' ? 'Engpass-Analyse: ' : 'Constraint Audit: ') . $company;
$subjectEnc = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$safeName   = str_replace(['"', '\\'], '', $name);
$fromDomain = substr(strrchr($cfg['from'], '@') ?: '@olimann.com', 1);

$headers = [
    'From: Olimann Website <' . $cfg['from'] . '>',
    'Reply-To: "' . $safeName . '" <' . $email . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    'X-Mailer: olimann-site',
];

/* ---------------------------------------------------------------- minimal SMTP client (AUTH LOGIN, SSL or STARTTLS) */
function smtp_send(array $cfg, string $to, string $subjectEnc, array $headers, string $body, string &$err): bool
{
    $port   = (int)$cfg['smtp_port'];
    $secure = $port === 465 ? 'ssl' : ($port === 587 ? 'tls' : 'none');
    $target = ($secure === 'ssl' ? 'ssl://' : 'tcp://') . $cfg['smtp_host'] . ':' . $port;
    $ctx    = stream_context_create(['ssl' => ['verify_peer' => true, 'verify_peer_name' => true, 'SNI_enabled' => true]]);
    $fp     = @stream_socket_client($target, $errno, $errstr, 20, STREAM_CLIENT_CONNECT, $ctx);
    if (!$fp) { $err = "connect failed: $errstr ($errno)"; return false; }
    stream_set_timeout($fp, 20);

    $read = static function () use ($fp): string {
        $out = '';
        while (($l = fgets($fp, 1024)) !== false) { $out .= $l; if (isset($l[3]) && $l[3] === ' ') { break; } }
        return $out;
    };
    $expect = static function (string $send, array $ok, string $label) use ($fp, $read, &$err): bool {
        if ($send !== '') { fwrite($fp, $send . "\r\n"); }
        $r = $read();
        if (!in_array((int)substr($r, 0, 3), $ok, true)) { $err = $label . ': ' . trim($r); return false; }
        return true;
    };
    $ehlo = 'EHLO ' . (preg_replace('/[^a-z0-9.\-]/i', '', $_SERVER['SERVER_NAME'] ?? 'localhost') ?: 'localhost');

    $ok = $expect('', [220], 'greeting') && $expect($ehlo, [250], 'EHLO');
    if ($ok && $secure === 'tls') {
        $ok = $expect('STARTTLS', [220], 'STARTTLS')
           && (stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_TLS_CLIENT) === true || (($err = 'TLS negotiation failed') && false))
           && $expect($ehlo, [250], 'EHLO (tls)');
    }
    $ok = $ok
       && $expect('AUTH LOGIN', [334], 'AUTH')
       && $expect(base64_encode($cfg['smtp_user']), [334], 'AUTH user')
       && $expect(base64_encode($cfg['smtp_pass']), [235], 'AUTH password')
       && $expect('MAIL FROM:<' . $cfg['from'] . '>', [250], 'MAIL FROM')
       && $expect('RCPT TO:<' . $to . '>', [250, 251], 'RCPT TO')
       && $expect('DATA', [354], 'DATA');
    if ($ok) {
        $fromDomain = substr(strrchr($cfg['from'], '@') ?: '@localhost', 1);
        $all = array_merge(['To: <' . $to . '>', 'Subject: ' . $subjectEnc, 'Date: ' . date(DATE_RFC2822),
                            'Message-ID: <' . bin2hex(random_bytes(8)) . '@' . $fromDomain . '>'], $headers);
        $data = implode("\r\n", $all) . "\r\n\r\n" . str_replace("\n", "\r\n", str_replace("\r\n", "\n", $body));
        $data = preg_replace('/^\./m', '..', $data) ?? $data;     // dot-stuffing
        $ok = $expect($data . "\r\n.", [250], 'message');
    }
    fwrite($fp, "QUIT\r\n");
    fclose($fp);
    return $ok;
}

$err = '';
if ($cfg['smtp_pass'] !== '') {
    $sent = smtp_send($cfg, $cfg['to'], $subjectEnc, $headers, $body, $err);
    if (!$sent) { error_log('olimann audit form: SMTP failed - ' . $err); }
} else {
    $sent = @mail($cfg['to'], $subjectEnc, $body, implode("\r\n", $headers), '-f' . $cfg['from']);
    if (!$sent) { error_log('olimann audit form: mail() returned false (no SMTP password configured)'); }
}

header('Location: ' . ($sent ? $thanks : $back . '?error=2#audit-form'), true, 303);
exit;
