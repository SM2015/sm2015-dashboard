<?php

include('registerClass.php');
header('Content-type: application/x-javascript');
header('Connection: close');

$fname = $_POST['fname'];
$lname = $_POST['lname'];
$email = $_POST['email'];
$countries = $_POST['countries'];
$phone = $_POST['phone'];
$level = $_POST['level'];

$response["msg"] = '';
$response["error"] = array();


if (isset($fname) && isset($lname) && isset($email) && isset($countries)) {
	if (empty($fname)) {
		array_push($response["error"],'Please enter your first name.');
	}
	if (empty($lname)) {
		array_push($response["error"],'Please enter your last name.');
	}
	if (empty($email)) {
			array_push($response["error"],'Please enter your email.');
	}
	if (empty($countries)) {
		array_push($response["error"],'Please enter the countries.');
	}

	if (empty($response["error"])) {
		$register = new Register($fname, $lname, $email, $countries, $phone, $level);
		$result = $register->addUser();
		if (!empty($result)) {
			array_push($response["error"],$result[0]);
		} else {
			if ($register->isSuccess()) {
				$response["msg"] = "success";
			} else {
				array_push($response["error"], "The system is not avaliable, please try again soon.");
			}
		}
	}

} else {
	array_push($response["error"], "You must set the required fills.");
}

$json = json_encode($response);
echo($json);
?>