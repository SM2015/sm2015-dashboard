<?php

include('database.php');
include('./lib/SendGrid_loader.php');
// include('lib/SendGrid.php');

class Register {

	private $fname;
	private $lname;
	private $email;
	private $countries;
	private $phone;
	private $success;

	function __construct($fname, $lname, $email, $countries, $phone) {
		$this->fname = $fname;
		$this->lname = $lname;
		$this->email = $email;
		$this->countries = $countries;
		$this->phone = $phone;
		$this->success = false;
	}

	function addUser() {
		//make sure the email address is available
		$username = $this->email;
		$query_verify_email = "SELECT * FROM member WHERE username='$username'";
		$db = new Database();
		$db->connect();
		$result_verify_email = $db->retrieve($query_verify_email);
		$error = array();
		if ($result_verify_email != false) {
			$rows = pg_num_rows($result_verify_email);
			if ($rows == 0) {
				// Create a unique  activation code:
				$activation = md5(uniqid(rand(), true));
				$query_insert_user = "INSERT INTO member ( username, password, fname, lname, address, contact, picture, gender, activation, level, countries) VALUES ( '$this->email', '', '$this->fname', '$this->lname', '', '$this->phone', '', '','$activation', 'admin', '$this->countries')";

				$result_insert_user = $db->insert($query_insert_user);

				if ($result_insert_user != false) {
					if (pg_affected_rows($result_insert_user) == 1) {
						//send EMAIL
						$message = "To activate your account, please click on this link:\n\n";
						$message .= '<a href="http://sm2015dashboard.org/php/activate.php?email=' . urlencode($this->email) . '&key=' . $activation .'">Active</a>';
						
						$sendgrid = new SendGrid('zoop.mail', 'Rio2016');
						$mail     = new SendGrid\Mail();
						$mail->addTo($this->email)->
							setFrom('SM2015')->
							setSubject('[SM2015] Confirm Registration')->
							setText('Hello World!')->
							setHtml('<html><head><title>SM2015</title></head><body><p>' . $message . '</p></body></html>');
							$response = json_decode($sendgrid->web->send($mail));
							if ($response->message == 'success') {
								$this->setSuccess(true);
							}
					}
				} else {
					array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
				}

			} else {
				array_push($error, "That email address has already been registered.");
			}
		} else {
			array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
		}
		$db->close();
		return $error;
	}

	function getDatabaseError() {
		return $this->databaseError;
	}

	function getHasUser() {
		return $this->userExist;
	}

	function isSuccess() {
		return $this->success;
	}

	function setSuccess($value) {
		$this->success = $value;
	}
}

?>
