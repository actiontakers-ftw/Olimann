<?php
declare(strict_types=1);
/* Shared helpers: where submissions are stored, how they are read and written. */

function olimann_data_dir(): string
{
    static $dir = null;
    if ($dir !== null) { return $dir; }
    $candidates = [];
    $root = rtrim((string)($_SERVER['DOCUMENT_ROOT'] ?? ''), '/');
    if ($root !== '') { $candidates[] = dirname($root) . '/olimann-data'; }   // outside public_html: survives re-uploads
    $candidates[] = __DIR__ . '/data';                                        // fallback inside public_html
    foreach ($candidates as $d) {
        if (!is_dir($d)) { @mkdir($d, 0755, true); }
        if (is_dir($d) && is_writable($d)) {
            if (!is_file($d . '/.htaccess')) { @file_put_contents($d . '/.htaccess', "Require all denied\n"); }
            if (!is_file($d . '/index.html')) { @file_put_contents($d . '/index.html', ''); }
            return $dir = $d;
        }
    }
    return $dir = __DIR__ . '/data';
}

function olimann_store(array $rec): bool
{
    $line = json_encode($rec, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if ($line === false) { return false; }
    return @file_put_contents(olimann_data_dir() . '/submissions.jsonl', $line . "\n", FILE_APPEND | LOCK_EX) !== false;
}

/** newest first */
function olimann_read_all(): array
{
    $f = olimann_data_dir() . '/submissions.jsonl';
    if (!is_file($f)) { return []; }
    $out = [];
    foreach (file($f, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) ?: [] as $l) {
        $r = json_decode($l, true);
        if (is_array($r)) { $out[] = $r; }
    }
    return array_reverse($out);
}
