<?php

require_once('database.php');

class Login {

	private $info;
	private $id;
	private $username;
	private $fname; //first name
	private $lname; //last name;
	private $address;
	private $contact;
	private $password;
	private $picture;
	private $gender;
	private $level;
	private $phone;
	private $activation;
	private $countries;
	private $databaseError = False; //error from database
	private $loginValid = False;  //if the user already exist
	private $hasPassword = false;

	function isEmail($user) {
		return filter_var($user, FILTER_VALIDATE_EMAIL);
	}

	function isPassword($pass) {
		return ($pass == '') ? false : true;
	}

	function hasPassword() {
		return $this->hasPassword;
	}

	function setPassword($pass, $email) {
		$query = "UPDATE member SET password='$pass' WHERE username='$email'";
		$db = new Database();
		$db->connect();
		$result = $db->update($query);
		if (pg_affected_rows($result) == 1) {
			$this->hasPassword = true;
		}
		$db->close();
		return $this->hasPassword;
	}

	function getLogin($user, $pass) {
		$query="SELECT * FROM member WHERE username='$user' AND password='$pass'";
		//connect database
		$db = new Database();
		$db->connect();
		$result = $db->retrieve($query);
		if ($result != False) {
			$rows = pg_num_rows($result);
			if ($rows > 0) {
				$member = pg_fetch_assoc($result);
				$this->setInformation($member);
				if ($this->getActivation() != null) {
					$this->loginValid = False;
				} else {
					$this->loginValid = True;
				}
				$db->freeMemory($result);
			}
		} else {
			$this->databaseError = True;
		}

		$db->close();
	}

	function updateInfo($id, $pass, $fname, $lname, $contact) {
		$query = "UPDATE member SET password = '$pass', fname = '$fname', lname = '$lname', contact = '$contact' WHERE mem_id=$id";
		$db = new Database();
		$db->connect();
		$response = False;
		$result = $db->update($query);
		if ($result != False) {
			$response = True; //ok, just confirm!
			$db->freeMemory($result);
		}
		$db->close();
		return $response;
	}

	function getDatabaseError() {
		return $this->databaseError;
	}

	function isValid() {
		return $this->loginValid;
	}

	function setInformation($info) {
		$this->id = $info['mem_id'];
		$this->username = $info['username'];
		$this->fname = $info['fname'];
		$this->lname = $info['lname'];
		$this->address = $info['address'];
		$this->contact = $info['contact'];
		$this->picture = $info['picture'];
		$this->password = $info['password'];
		$this->gender = $info['gender'];
		$this->activation = $info['activation'];
		$this->level = $info['level'];
		$this->countries = $info['countries'];
	}

	function getId() {
		return $this->id;
	}

	function getUsername() {
		return $this->username;
	}

	function getFname() {
		return $this->fname;
	}

	function getLname() {
		return $this->lname;
	}

	function getAddress() {
		return $this->address;
	}

	function getContact() {
		return $this->contact;
	}

	function getPicture() {
		return $this->picture;
	}

	function getGender() {
		return $this->gender;
	}

	function getLevel() {
		return $this->level;
	}

	function getActivation() {
		return $this->activation;
	}

	function getCountries() {
		return $this->countries;
	}

	function getPassword() {
		return $this->password;
	}

	function getInfoDatabase($id) {
		$query="SELECT * FROM member WHERE mem_id=$id";
		//connect database
		$db = new Database();
		$db->connect();
		$result = $db->retrieve($query);
		if ($result != False) {
			$rows = pg_num_rows($result);
			if ($rows > 0) {
				$member = pg_fetch_assoc($result);
				$this->setInformation($member);
				$db->freeMemory($result);
			}
		} else {
			$this->databaseError = True;
		}

		$db->close();
		$info = $this->getInfo(); 
		return $info;
	}

	function getInfo() {
		$info = new stdClass();
		$info->id = $this->getId();
		$info->username = $this->getUsername();
		$info->fname = $this->getFname();
		$info->lname = $this->getLname();
		$info->address = $this->getAddress();
		$info->contact = $this->getContact();
		$info->picture = $this->getPicture();
		$info->gender = $this->getGender();
		$info->level = $this->getLevel();
		$info->activation = $this->getActivation();
		$info->password = $this->getPassword();
		$info->countries = $this->getCountries();
		return $info;
	}

}

?>