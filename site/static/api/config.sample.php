<?php
/*
 * Copy this file to config.php (same folder) and fill in the mailbox password.
 * config.php is read by send.php and is not part of the site bundle, so a re-upload never overwrites it.
 */
return [
    'to'        => 'info@olimann.com',
    'from'      => 'info@olimann.com',
    'smtp_host' => 'smtp.hostinger.com',
    'smtp_port' => 465,
    'smtp_user' => 'info@olimann.com',
    'smtp_pass' => 'PASTE-THE-MAILBOX-PASSWORD-HERE',
];
