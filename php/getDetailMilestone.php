<?php

include("milestonesClass.php");

header('Content-type: application/x-javascript');
header('Connection: close');

$rowid = $_GET["rowid"];

$response["msg"] = "";
$response["alerts"] ="";
$response["recommendation"] ="";
$response["agreements"] ="";
$response["activitypoa"] ="";
$response["error"] = array();

if (isset($rowid)) {
	$milestones = new Milestones('', '', '', '', '', '');
	$result = $milestones->getDetailMilestone($rowid);
	$temerro = empty($result);
	if (!$temerro) {	
		$response["alerts"] = $result["alerts"];
		$response["recommendation"] = $result["recommendation"];
		$response["agreements"] = $result["agreements"];
		$response["activitypoa"] = $result["activitypoa"];
	} else {
		array_push($response["error"], $error[0]);
	}
} else {
  array_push($response["error"], "The system is not avaliable, please try again soon.");
}


$json = json_encode($response);
echo($json);
?>