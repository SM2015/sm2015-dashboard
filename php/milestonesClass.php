<?php

include("database.php");

class Milestones {

  private $country;
  private $indicator;
  private $milestone;
  private $quarter;
  private $audience;
  private $status;
  private $success;
  private $alerts;
  private $recommendation;
  private $agreements;
  private $activitypoa;

  function __construct($country, $indicator, $milestone, $quarter, $audience, $status) {
    $this->country = $country;
    $this->indicator = $indicator;
    $this->milestone = $milestone;
    $this->quarter = $quarter;
    $this->audience = $audience;
    $this->status = $status;
  }


  function update($rowID) {
    
    $query_update = "UPDATE milestone SET country = '$this->country', indicator = '$this->indicator', milestone = '$this->milestone', quarter = '$this->quarter', audience = '$this->audience', status = '$this->status' WHERE id='$rowID'";
    $db = new Database();
    $db->connect();
    $result = $db->update($query_update);
    $error = array();
    if ($result != false) {
      if (pg_affected_rows($result) == 1) {
        $this->success = true;
      }
    } else {
      array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
    }

    $db->close();
    return $error;
  }

  function getDetailMilestone($rowID) {
    $query = "SELECT * from milestone WHERE id='$rowID'";
    $db = new Database();
    $db->connect();
    $result = $db->retrieve($query);
    $error = array();
    if ($result != false) {
      $rows = pg_num_rows($result);
      if ($rows > 0) {
        $details = pg_fetch_assoc($result);
        $this->setDetails($details);
      } else {
        array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
      }
    } else {
      array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
    }
    $db->freeMemory($result);
    $db->close();
    return $details;
  }

  function setDetails($details) {
    $this->alerts = $details->alerts;
    $this->recommendation = $details->recommendation;
    $this->agreements = $details->agreements;
    $this->activitypoa = $details->activitypoa;
  }

  function getDetails() {
    $details = new stdClass();
    $details->alerts = $this->alerts;
    $details->recommendation = $this->recommendation;
    $details->agreements = $this->agreements;
    $details->activitypoa = $this->activitypoa;
    return $details;
  }

  function updateDetail($rowID, $alerts, $recommendation, $agreements, $activitypoa) {
    $query_update = "UPDATE milestone SET alerts = '$alerts', recommendation = '$recommendation', agreements = '$agreements', activitypoa = '$activitypoa' WHERE id='$rowID'";
    $db = new Database();
    $db->connect();
    $result = $db->update($query_update);
    $error = array();
    if ($result != false) {
      if (pg_affected_rows($result) == 1) {
        $this->success = true;
      }
    } else {
      array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
    }

    $db->close();
    return $error;
  }

  function isSuccess() {
    return $this->success;
  }

  function insert() {

  }

  function delete($rowID) {
    $query_delete ="DELETE FROM milestone WHERE id='$rowID'";
    $db = new Database();
    $db->connect();
    $result = $db->delete($query_delete);
    $error = array();
    if ($result != false) {
      if (pg_affected_rows($result) == 1) {
        $this->success = true;
      }
    } else {
      array_push($error, "You could not be registered due to a system error. We apologize for any inconvenience");
    }

    $db->close();
    return $error;
  }
}

?>