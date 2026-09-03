<?php
declare(strict_types=1);
/* Olimann — private inbox for Constraint Audit requests. Password-protected; change the password inside once logged in. */
require __DIR__ . '/../api/lib.php';
header('X-Robots-Tag: noindex, nofollow');
header('Cache-Control: no-store');
header('Referrer-Policy: no-referrer');

const INBOX_PASSWORD_HASH = '$2y$12$JDOBijHQgu3OC5JrIF8JmunbzggU.x8n3eB29osQxHVCZ2z02MmzG';

$dataDir  = olimann_data_dir();
$hashFile = $dataDir . '/inbox-password.txt';
$hash     = is_file($hashFile) ? trim((string)file_get_contents($hashFile)) : INBOX_PASSWORD_HASH;
$secret   = hash('sha256', $hash . '|olimann-inbox');
$https    = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
$cookie   = 'olimann_inbox';

function e(?string $s): string { return htmlspecialchars((string)$s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }
function cookie_opts(bool $https, int $exp): array { return ['expires' => $exp, 'path' => '/inbox/', 'secure' => $https, 'httponly' => true, 'samesite' => 'Lax']; }
function logged_in(string $secret, string $cookie): bool {
    $c = (string)($_COOKIE[$cookie] ?? '');
    if ($c === '' || strpos($c, '.') === false) { return false; }
    [$exp, $sig] = explode('.', $c, 2);
    return ctype_digit($exp) && (int)$exp > time() && hash_equals(hash_hmac('sha256', $exp, $secret), $sig);
}
function log_in(string $secret, string $cookie, bool $https): void {
    $exp = time() + 30 * 86400;
    setcookie($cookie, $exp . '.' . hash_hmac('sha256', (string)$exp, $secret), cookie_opts($https, $exp));
}

/* lockout: 8 wrong passwords per address per 15 minutes */
$ip = (string)($_SERVER['REMOTE_ADDR'] ?? '0');
$attFile = $dataDir . '/inbox-attempts.json';
$att = is_file($attFile) ? (json_decode((string)file_get_contents($attFile), true) ?: []) : [];
$now = time();
foreach ($att as $k => $ts) { $att[$k] = array_values(array_filter((array)$ts, static fn($t) => (int)$t > $now - 900)); if (!$att[$k]) { unset($att[$k]); } }
$locked = count($att[$ip] ?? []) >= 8;

$action = (string)($_POST['action'] ?? ($_GET['action'] ?? ''));
$msg = '';
if ($action === 'login') {
    if (!$locked && password_verify((string)($_POST['password'] ?? ''), $hash)) { log_in($secret, $cookie, $https); header('Location: /inbox/', true, 303); exit; }
    $att[$ip][] = $now; @file_put_contents($attFile, json_encode($att)); usleep(800000); $msg = $locked ? 'locked' : 'wrong';
}
$in   = logged_in($secret, $cookie);
$csrf = hash_hmac('sha256', 'csrf', $secret . (string)($_COOKIE[$cookie] ?? ''));
$csrfOk = hash_equals($csrf, (string)($_POST['csrf'] ?? ''));
if ($in && $action === 'logout' && $csrfOk) { setcookie($cookie, '', cookie_opts($https, time() - 3600)); header('Location: /inbox/', true, 303); exit; }
if ($in && $action === 'password' && $csrfOk) {
    $cur = (string)($_POST['current'] ?? ''); $new = (string)($_POST['new'] ?? '');
    if (!password_verify($cur, $hash)) { $msg = 'badcurrent'; }
    elseif (strlen($new) < 12) { $msg = 'short'; }
    else {
        $newHash = password_hash($new, PASSWORD_DEFAULT);
        file_put_contents($hashFile, $newHash);
        log_in(hash('sha256', $newHash . '|olimann-inbox'), $cookie, $https);
        header('Location: /inbox/?changed=1', true, 303); exit;
    }
}
$rows = $in ? olimann_read_all() : [];

if ($in && $action === 'csv') {
    header('Content-Type: text/csv; charset=UTF-8');
    header('Content-Disposition: attachment; filename="olimann-audit-requests-' . date('Y-m-d') . '.csv"');
    $out = fopen('php://output', 'w'); fwrite($out, "\xEF\xBB\xBF");
    fputcsv($out, ['Time', 'Language', 'Name', 'Company', 'Role', 'Email', 'Website', 'Where work piles up', 'Other', 'Revenue', 'Headcount sales', 'Headcount delivery', 'Headcount support', 'Headcount admin', 'Double the customers', 'Tools', 'Cost-heavy workflow']);
    foreach (array_reverse($rows) as $r) {
        $h = $r['headcount'] ?? [];
        fputcsv($out, [$r['time'] ?? '', $r['lang'] ?? '', $r['name'] ?? '', $r['company'] ?? '', $r['role'] ?? '', $r['email'] ?? '', $r['website'] ?? '', implode('; ', $r['pile'] ?? []), $r['pile_other'] ?? '', $r['revenue'] ?? '', $h['sales'] ?? '', $h['delivery'] ?? '', $h['support'] ?? '', $h['admin'] ?? '', $r['double'] ?? '', $r['tools'] ?? '', $r['costheavy'] ?? '']);
    }
    fclose($out); exit;
}
?><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>Olimann · Inbox</title>
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/site.css">
<style>
  body{background:var(--paper)}
  .bar{background:var(--navy-2);color:var(--cream)}
  .bar .wrap{display:flex;align-items:center;gap:18px;flex-wrap:wrap;height:auto;padding-top:14px;padding-bottom:14px}
  .bar .word{font-family:var(--serif);font-style:italic;font-size:26px}
  .bar .tag{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-light)}
  .bar form{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
  .bar .btn{padding:9px 14px;font-size:13px;--accent:var(--gold-light);--accent-ink:#081F40}
  .content{padding:36px 0 80px;color:var(--ink)}
  .login{max-width:420px;margin:12vh auto;background:var(--paper-2);padding:34px 32px}
  .login h1{font-size:34px;margin-bottom:6px}
  .login p{color:var(--muted);font-size:14.5px}
  .login input[type=password]{width:100%;font:inherit;font-size:16px;padding:13px 14px;border:1px solid var(--line);background:#fff;margin:14px 0}
  .login .btn{width:100%;justify-content:center}
  .alert{background:#FBE9E7;color:#8A2A22;border-left:2px solid #B03333;padding:10px 14px;font-size:14px;margin-bottom:8px}
  .ok{background:#E6F1EA;color:#2D5F3F;border-left:2px solid #2D5F3F;padding:10px 14px;font-size:14px;margin-bottom:18px}
  .count{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--copper);margin-bottom:18px}
  .card{background:#fff;border:1px solid var(--line);padding:22px 24px;margin-bottom:16px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:18px 32px}
  @media (max-width:800px){.card{grid-template-columns:1fr}}
  .card h2{font-size:26px;line-height:1.1;margin-bottom:2px}
  .card .who{font-size:14.5px;color:var(--muted);margin-bottom:10px}
  .card .who a{color:var(--copper)}
  .card .when{font-family:var(--mono);font-size:11.5px;color:var(--muted);letter-spacing:.06em}
  .lbl{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--copper);margin:12px 0 4px}
  .lbl:first-child{margin-top:0}
  .chipsx{display:flex;flex-wrap:wrap;gap:6px}
  .chipsx span{font-family:var(--mono);font-size:12px;padding:4px 8px;border:1px solid var(--line);background:var(--paper-2)}
  .ans{white-space:pre-wrap;font-size:15px;line-height:1.55;margin:0}
  .empty{background:var(--paper-2);padding:40px;text-align:center;color:var(--muted)}
  details.pw{margin-top:40px;max-width:520px}
  details.pw summary{cursor:pointer;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  details.pw input{width:100%;font:inherit;font-size:15px;padding:11px 12px;border:1px solid var(--line);background:#fff;margin:8px 0}
</style>
</head>
<body class="light">
<?php if (!$in): ?>
<main class="content"><div class="wrap">
  <form class="login" method="post" action="/inbox/">
    <input type="hidden" name="action" value="login">
    <div class="tag" style="font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--copper)">Olimann · Inbox</div>
    <h1>Audit requests</h1>
    <p>Private. Enter the inbox password.</p>
    <?php if ($msg === 'wrong'): ?><div class="alert">That password is not right.</div><?php endif; ?>
    <?php if ($msg === 'locked' || $locked): ?><div class="alert">Too many attempts. Try again in 15 minutes.</div><?php endif; ?>
    <input type="password" name="password" autocomplete="current-password" autofocus required aria-label="Password">
    <button class="btn btn-primary" type="submit">Open inbox</button>
  </form>
</div></main>
<?php else: ?>
<header class="bar"><div class="wrap">
  <span class="word">Olimann</span><span class="tag">Inbox · audit requests</span>
  <form method="post" action="/inbox/"><input type="hidden" name="csrf" value="<?= e($csrf) ?>">
    <button class="btn" name="action" value="csv" type="submit">Download CSV</button>
    <button class="btn" name="action" value="logout" type="submit">Log out</button>
  </form>
</div></header>
<main class="content"><div class="wrap">
  <?php if (isset($_GET['changed'])): ?><div class="ok">Password changed.</div><?php endif; ?>
  <?php if ($msg === 'badcurrent'): ?><div class="alert">The current password was not right. Nothing changed.</div><?php endif; ?>
  <?php if ($msg === 'short'): ?><div class="alert">Use at least 12 characters for the new password.</div><?php endif; ?>
  <div class="count"><?= count($rows) ?> request<?= count($rows) === 1 ? '' : 's' ?></div>
  <?php if (!$rows): ?><div class="empty">No requests yet. Submissions from the Constraint Audit form will appear here.</div><?php endif; ?>
  <?php foreach ($rows as $r): $h = $r['headcount'] ?? []; $hc = array_filter(['Sales & marketing' => $h['sales'] ?? '', 'Delivery & operations' => $h['delivery'] ?? '', 'Support' => $h['support'] ?? '', 'Admin' => $h['admin'] ?? '']); ?>
  <article class="card">
    <div>
      <div class="when"><?= e(date('d M Y · H:i', strtotime((string)($r['time'] ?? 'now')) ?: time())) ?> · <?= e(strtoupper((string)($r['lang'] ?? ''))) ?></div>
      <h2><?= e($r['company'] ?? '') ?></h2>
      <div class="who"><?= e($r['name'] ?? '') ?><?= !empty($r['role']) ? ' · ' . e($r['role']) : '' ?><br><a href="mailto:<?= e($r['email'] ?? '') ?>"><?= e($r['email'] ?? '') ?></a><?php if (!empty($r['website'])): ?> · <?= e($r['website']) ?><?php endif; ?></div>
      <div class="lbl">Where work piles up</div>
      <div class="chipsx"><?php foreach ((array)($r['pile'] ?? []) as $p): ?><span><?= e($p) ?></span><?php endforeach; ?><?php if (!empty($r['pile_other'])): ?><span><?= e($r['pile_other']) ?></span><?php endif; ?><?php if (empty($r['pile']) && empty($r['pile_other'])): ?><span>–</span><?php endif; ?></div>
      <div class="lbl">Size</div>
      <div style="font-size:14.5px"><?= e(($r['revenue'] ?? '') !== '' ? $r['revenue'] : '–') ?><?php if ($hc): ?> · <?php foreach ($hc as $k => $v): ?><?= e($k) ?> <?= e((string)$v) ?> &nbsp;<?php endforeach; ?><?php endif; ?></div>
    </div>
    <div>
      <div class="lbl">Double the customers tomorrow: revenue doubles, or something breaks?</div><p class="ans"><?= e(($r['double'] ?? '') !== '' ? $r['double'] : '–') ?></p>
      <div class="lbl">Tools in sales, delivery, support</div><p class="ans"><?= e(($r['tools'] ?? '') !== '' ? $r['tools'] : '–') ?></p>
      <div class="lbl">Most cost- and resource-heavy workflow or department vs. its return</div><p class="ans"><?= e(($r['costheavy'] ?? '') !== '' ? $r['costheavy'] : '–') ?></p>
    </div>
  </article>
  <?php endforeach; ?>
  <details class="pw"><summary>Change the inbox password</summary>
    <form method="post" action="/inbox/"><input type="hidden" name="action" value="password"><input type="hidden" name="csrf" value="<?= e($csrf) ?>">
      <input type="password" name="current" placeholder="Current password" autocomplete="current-password" required>
      <input type="password" name="new" placeholder="New password (12+ characters)" autocomplete="new-password" minlength="12" required>
      <button class="btn btn-primary" type="submit">Change password</button>
    </form>
  </details>
</div></main>
<?php endif; ?>
</body>
</html>
