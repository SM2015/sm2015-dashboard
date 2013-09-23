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
Editor::inst( $db, 'milestone' )
    ->fields(
        Field::inst( 'country' )->validator( 'Validate::required'),
        Field::inst( 'indicator' )->validator( 'Validate::required' ),
        Field::inst( 'milestone' )->validator( 'Validate::required' ),
        Field::inst( 'quarter' )->validator( 'Validate::required' ),
        Field::inst( 'audience' )->validator( 'Validate::required' ),
        Field::inst( 'status' )->validator( 'Validate::required' ),
        Field::inst( 'alerts' )->validator( 'Validate::required' ),
        Field::inst( 'recommendation' )->validator( 'Validate::required' ),
        Field::inst( 'agreements' )->validator( 'Validate::required' ),
        Field::inst( 'activitypoa' )->validator( 'Validate::required' )
    )
    ->process( $_POST )
    ->json();