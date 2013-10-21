<?php

// DataTables PHP library
include( "./lib/DataTables.php" );
include( "lib/ChromePhp.php" );
// Alias Editor classes so they are easy to use
use
    DataTables\Editor,
    DataTables\Editor\Field,
    DataTables\Editor\Format,
    DataTables\Editor\Join,
    DataTables\Editor\Validate;

// Build our Editor instance and process the data coming from _POST
Editor::inst( $db, 'infomilestone' )
    ->fields(
        Field::inst( 'country' )->validator( 'Validate::required'),
        Field::inst( 'updated' )->validator( 'Validate::required' ),
        Field::inst( 'executed' )->validator( 'Validate::required' ),
        Field::inst( 'planned' )->validator( 'Validate::required' ),
        Field::inst( 'alerts' )->validator( 'Validate::required' ),
        Field::inst( 'expended' )->validator( 'Validate::required' ),
        Field::inst( 'pep' )->validator( 'Validate::required' ),
        Field::inst( 'progression' )->validator( 'Validate::required' ),
        Field::inst( 'recommendation' )->validator( 'Validate::required' ),
        Field::inst( 'montocomprometido' )->validator( 'Validate::required' )
    )
    ->process( $_POST )
    ->json();