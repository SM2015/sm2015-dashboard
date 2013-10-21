<?php

	include('loginClass.php');
	header('Content-type: application/x-javascript');
	header('Connection: close');

	$userid = $_SESSION['SESS_MEMBER_ID'];
	$pass = $_POST['pass'];
	$fname = $_POST['fname'];
	$lname = $_POST['lname'];
	$phone = $_POST['contact'];

	$response["fname"] = "";
	$response["lname"] = "";
	$response["error"] = array();

	if (isset($userid)) {

		//Function to sanitize values received from the form. Prevents SQL injection
		function clean($str) {
			$str = @trim($str);
			if(get_magic_quotes_gpc()) {
				$str = stripslashes($str);
			}
			return pg_escape_string($str);
		}

		$username = clean($userid);

		$login = new Login();

		if (isset($pass) && $pass == '') {
			array_push($response["error"], "Password missing");
		}

		if (count($response["error"]) == 0) {
			//try update
			$result = $login->updateInfo($username, $pass, $fname, $lname, $phone);
			if ($result == True) {
				$response["fname"] = $fname;
				$response["lname"] = $lname;
			}
		}
	} else {
		array_push($response["error"], "Username and password are missing.");
	}

	$json = json_encode($response);
	echo($json);
?>