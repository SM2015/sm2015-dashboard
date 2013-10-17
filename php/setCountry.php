<?php
include('signin.php');
header('Content-type: application/x-javascript');
header('Connection: close');
session_start();
$country = $_GET['country'];

$_SESSION['SESS_COUNTRY'] = $country;
$response['msg'] = 'success';
$response['country'] = $country;

$json = json_encode($response);
echo($json);
?>