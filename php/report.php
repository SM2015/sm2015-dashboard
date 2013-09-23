<?php

require_once 'lib/PHPWord.php';

include('database.php');

header('Content-type: application/x-javascript');
header('Connection: close');

$infoMilestone = $_POST['info'];
$table = $_POST['table'];

$jsonTable = json_encode($table);

/*Create TABLE*/
$PHPWord = new PHPWord();
$section = $PHPWord->createSection();

$fontStyle = array('bold'=>false, 'align'=>'center', 'color'=>'FFFFFF', 'size'=>'8', 'font-family'=>'Times New Roman');
$firstRowStyle = array('bgColor' => '5dbaf4');
$evenStyle = array('bgColor' => 'b4ddf7');
// Add table
$table = $section->addTable();
	
//cria a primeira linha e suas colunas
$table->addRow();
$table->addCell(1750, $firstRowStyle)->addText("Pais", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Indicador de pago", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Hito", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Trimestre", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Estado Actual", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Alerta/Notas", $fontStyle);
$table->addCell(1750, $firstRowStyle)->addText("Recommendacion", $fontStyle);


foreach ($table as $d) {
	$activitypoa = $d['activitypoa'];
	$agreements = $d['agreements'];
	$alerts = $d['alerts'];
	$audience = $d['audience'];
	$country = $d['country'];
	$indicator = $d['indicator'];
	$milestone = $d['milestone'];
	$quarter = $d['quarter'];
	$recommendation = $d['recommendation'];
	$status = $d['status'];

	$table->addRow();
	$table->addCell(1750,$evenStyle)->addText($country);
	$table->addCell(1750,$evenStyle)->addText($indicator);
	$table->addCell(1750,$evenStyle)->addText($milestone);
	$table->addCell(1750,$evenStyle)->addText($audience);
	$table->addCell(1750,$evenStyle)->addText($quarter);
	$table->addCell(1750,$evenStyle)->addText($quarter);
}

// Save File
$objWriter = PHPWord_IOFactory::createWriter($PHPWord, 'Word2007');
$objWriter->save('Report.docx');

$response = new stdClass();
$response->url = 'php/Report.docx';

$json = json_encode($response);
echo($json);
?>