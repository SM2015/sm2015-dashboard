<?php
include('signin.php');
header('Content-type: application/x-javascript');
header('Connection: close');
session_start();
$lang = $_GET['lang'];

if (empty($lang)) {
	$lang = 'en';
}

$_SESSION['SESS_LANG'] = $lang;
$response['msg'] = 'success';
$response['lang'] = $lang;

$json = json_encode($response);
echo($json);
?>