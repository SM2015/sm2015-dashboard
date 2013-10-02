<?php

	include('loginClass.php');
	header('Content-type: application/x-javascript');
	header('Connection: close');

	$userid = $_POST['id'];
	$pass = $_POST['password'];
	$fname = $_POST['fname'];
	$lname = $_POST['lname'];
	$phone = $_POST['contact'];
	$level = $_POST['level'];
	$countries = $_POST['countries'];

	$response["username"] = "";
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
			//try login
			$login->getLogin($username, $password);
			//verify database erro
			if ($login->getDatabaseError()) {
				//error on database
				array_push($response["error"], "The system is not avaliable, please try again soon.");
			} else {
				//verify if the user exist
				if ($login->isValid()) {
					//LOGIN VALID SESSION MUST START!
					session_start();
					$_SESSION['SESS_MEMBER_ID'] = $login->getId();
					$_SESSION['SESS_USERNAME'] = $login->getUsername();
					$_SESSION['SESS_FIRST_NAME'] = $login->getFname();
					$_SESSION['SESS_LAST_NAME'] = $login->getLname();
					$_SESSION['SESS_LEVEL'] = $login->getLevel();
					$_SESSION['SESS_COUNTRIES'] = $login->getCountries();
					$_SESSION['SESS_LANG'] = 'es';

					$response["username"] = $login->getUsername();
					$response["fname"] = $login->getFname();
					$response["lname"] = $login->getLname();
					
				} else {
					array_push($response["error"], "The user/password is not correct.");
				}
			}
		}
	} else {
		array_push($response["error"], "Username and password are missing.");
	}

	$json = json_encode($response);
	echo($json);
?>