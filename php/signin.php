<?php
session_start();
if (!isset($_SESSION["SESS_MEMBER_ID"])) {
	$redirect = "index.php";
 	header("Location: ". $redirect);
}
?>