<?php
$file="DashboardSM2015.xls";
header('Content-Type: application/vnd.ms-excel');
header('Content-Disposition: attachment;filename="'.$file.'"');
header('Cache-Control: max-age=0');
include('signin.php');
include("database.php");

$country = $_GET['country'];
$country = urldecode($country);
$html = array();
if (isset($country)) {
	array_push($html, '<table border="1"><tr>', '<th>Pais</th>','<th>Fecha de Actualizacion</th>', '<th>Avances Físicos Planificados</th>', '<th>Avances Financieros Planificados</th>', '<th>Monto Comprometido</th>', '<th>Alertas Tempranas</th>', '<th>Monto Desembolsado</th>', '<th>Avances Físicos Reales</th>', '<th>Avances Financieros actuales</th>', '<th>Recomendaciones</th></tr>');
	$db = new Database();
	$db->connect();
	$queryInfoMilestone = "SELECT * from infomilestone WHERE country='$country'";
	$queryMilestone = "SELECT * from milestone WHERE country='$country' ORDER BY ID ASC";
	$resultInfo = $db->retrieve($queryInfoMilestone);
	$resultMilestone = $db->retrieve($queryMilestone);

	if ($resultInfo != false) {
	  $rows = pg_num_rows($resultInfo);
	  if ($rows > 0) {
	    $info = pg_fetch_assoc($resultInfo);
	    array_push($html, '<tr><td>'.$info["country"].'</td>', '<td>'.$info["updated"].'</td>', '<td>'.$info["executed"].'</td>','<td>'.$info["planned"].'</td>','<td>'.$info["montocomprometido"].'</td>','<td>'.$info["alerts"].'</td>','<td>'.$info["expended"].'</td>','<td>'.$info["pep"].'</td>','<td>'.$info["progression"].'</td>','<td>'.$info["recommendation"].'</td></tr></table>');
	  }
	}

	array_push($html, '<tr></tr><table border="1"><tr>', '<th>Pais</th>', '<th>Indicator de Pago</th>', '<th>Hito</th>', '<th>Trimestre</th>', '<th>Audiencia</th>', '<th>Estatus</th>','<th>Alerts/Notes</th>', '<th>Recomendacion JE</th>', '<th>Acuerdos</th>', '<th>Actividad en POA</th></tr>');

	if ($resultMilestone != false) {
		$rows = pg_num_rows($resultMilestone);
		if ($rows > 0) {
			while ($row = pg_fetch_row($resultMilestone)) {
			  array_push($html, '<tr><td>'.$row[1].'</td>', '<td>'.$row[2].'</td>', '<td>'.$row[3].'</td>', '<td>'.$row[4].'</td>', '<td>'.$row[5].'</td>', '<td>'.$row[6].'</td>', '<td>'.$row[7].'</td>', '<td>'.$row[8].'</td>', '<td>'.$row[9].'</td>', '<td>'.$row[10].'</td></tr>');
			}
		}
	}

	array_push($html, '</table>');
}
echo join(" ",$html);
?>