<?php

include("milestonesClass.php");

header('Content-type: application/x-javascript');
header('Connection: close');

$action = $_POST["action"];

$response["msg"] = "";
$response["error"] = array();

if (isset($action)) {

  if ($action == 'update') {
    $country = $_POST["country"];
    $indicator = $_POST["indicator"];
    $milestone = $_POST["milestone"];
    $quarter = $_POST["quarter"];
    $audience = $_POST["audience"];
    $status = $_POST["status"];
    $id = $_POST["id"];
    $milestones = new Milestones($country, $indicator, $milestone, $quarter, $audience, $status);
    $result = $milestones->update($id);
    if (!empty($result)) {
      array_push($response["error"],$result[0]);
    } else {
      if ($milestones->isSuccess()) {
        $response["msg"] = "The new data was inserted.";
      } else {
        array_push($response["error"], "The system is not avaliable, please try again soon.");
      }
    }
  } elseif ($action == 'delete') {
    $id = $_POST["id"];
    $milestones = new Milestones('','','','','','');
    $result = $milestones->delete($id);
    if (!empty($result)) {
      array_push($response["error"],$result[0]);
    } else {
      if ($milestones->isSuccess()) {
        $response["msg"] = "The data was deleted.";
      } else {
        array_push($response["error"], "The system is not avaliable, please try again soon.");
      }
    }
  } elseif ($action == 'create') {
    $response["msg"] = 'create';
  } elseif ($action == 'detail') {
    
    $alerts = $_POST['alerts'];
    $recommendation = $_POST['recommendation'];
    $agreements = $_POST['agreements'];
    $activitypoa = $_POST['activitypoa'];
    $id = $_POST["id"];
    
    $milestones = new Milestones('','','','','','');
    $result = $milestones->updateDetail($id, $alerts, $recommendation, $agreements, $activitypoa);
    if (!empty($result)) {
      array_push($response["error"],$result[0]);
    } else {
      if ($milestones->isSuccess()) {
        $response["msg"] = "The new data was inserted.";
      } else {
        array_push($response["error"], "The system is not avaliable, please try again soon.");
      }
    }
  }

} else {
  array_push($response["error"], "The system is not avaliable, please try again soon.");
}


  $json = json_encode($response);
  echo($json);
?>