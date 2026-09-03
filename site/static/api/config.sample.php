<?php
/*
 * Copy this file to config.php (same folder) and fill in a Google App Password for info@olimann.com.
 * Google Account of info@ → Security → 2-Step Verification (must be on) → App passwords → create one.
 * config.php is read by send.php and is not part of the site bundle, so a re-upload never overwrites it.
 */
return [
    'to'        => 'info@olimann.com',
    'from'      => 'info@olimann.com',
    'smtp_host' => 'smtp.gmail.com',
    'smtp_port' => 465,
    'smtp_user' => 'info@olimann.com',
    'smtp_pass' => 'PASTE-THE-16-CHARACTER-APP-PASSWORD-HERE',
];
