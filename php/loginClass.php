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
	private $picture;
	private $gender;
	private $level;
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
		$info->countries = $this->getCountries();
		return $info;

	}

}

?>