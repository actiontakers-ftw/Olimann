<?php
/*
 * Olimann — Constraint Audit form handler (Hostinger shared hosting, PHP mail()).
 * 1. Set $TO to the mailbox that should receive audit requests.
 * 2. Set $FROM to a mailbox that exists on this domain (create it in hPanel → Emails). Hostinger rejects mail() from foreign domains.
 */
declare(strict_types=1);

$TO   = 'info@olimann.com';       // receives audit requests
$FROM = 'info@olimann.com';       // sender: an existing mailbox on olimann.com

$lang   = (($_POST['lang'] ?? 'en') === 'de') ? 'de' : 'en';
$thanks = $lang === 'de' ? '/de/engpass-analyse/danke/' : '/constraint-audit/thanks/';
$back   = $lang === 'de' ? '/de/engpass-analyse/'       : '/constraint-audit/';

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') { header('Location: ' . $back, true, 303); exit; }

/* honeypot + time trap (bots fill hidden fields / submit instantly) */
if (!empty($_POST['fax'])) { header('Location: ' . $thanks, true, 303); exit; }
$ts = (int)($_POST['ts'] ?? 0);
if ($ts > 0 && (time() - $ts) < 3) { header('Location: ' . $thanks, true, 303); exit; }

$line = static function (string $k, int $max = 200): string {
    $v = (string)($_POST[$k] ?? '');
    $v = preg_replace('/[\r\n\t]+/', ' ', $v) ?? '';
    return mb_substr(trim(strip_tags($v)), 0, $max);
};
$text = static function (string $k, int $max = 4000): string {
    $v = (string)($_POST[$k] ?? '');
    return mb_substr(trim(strip_tags($v)), 0, $max);
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
$q4 = $text('capacity');
$q5 = $text('tools');
$q6 = $text('expensive');

$body  = ($lang === 'de' ? "Neue Engpass-Analyse-Anfrage" : "New Constraint Audit request") . "\n";
$body .= str_repeat('=', 40) . "\n\n";
$body .= "Name:     $name\nCompany:  $company\nRole:     $role\nEmail:    $email\nWebsite:  $website\nLanguage: $lang\n\n";
$body .= "Where work piles up:\n  " . ($pile ? implode("\n  ", $pile) : '-') . ($pileOther !== '' ? "\n  Other: $pileOther" : '') . "\n\n";
$body .= "Revenue band: " . ($revenue !== '' ? $revenue : '-') . "\n";
$body .= "Headcount:    " . ($hc ? implode(' | ', $hc) : '-') . "\n\n";
$body .= "20% more capacity next quarter:\n$q4\n\n";
$body .= "Tools in sales, delivery, support:\n$q5\n\n";
$body .= "Most expensive person / typical Tuesday:\n$q6\n\n";
$body .= str_repeat('-', 40) . "\nSent " . date('c') . " from " . ($_SERVER['REMOTE_ADDR'] ?? '?') . "\n";

$subject    = ($lang === 'de' ? 'Engpass-Analyse: ' : 'Constraint Audit: ') . $company;
$subjectEnc = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$safeName   = str_replace(['"', '\\'], '', $name);
$headers  = "From: Olimann Website <$FROM>\r\n";
$headers .= "Reply-To: \"$safeName\" <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
$headers .= "X-Mailer: olimann-site\r\n";

$ok = @mail($TO, $subjectEnc, $body, $headers, '-f' . $FROM);
header('Location: ' . ($ok ? $thanks : $back . '?error=2#audit-form'), true, 303);
exit;
