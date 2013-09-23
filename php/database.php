<?php

/**/
Class Database {

	var $hostname = 'localhost'; /*ip database*/
    var $user = 'postgres'; /*user database*/
    var $password = '12345'; /*password*/
    var $dbname = 'dashboard'; /*database name*/
    var $connection; /**/
    var $database; /*selection database*/

    function connect() {
    	$this->connection = pg_connect("host=localhost dbname=dashboard user=postgres password=12345") or die ('Could not connect: ' . pg_last_error());
    }

    function freeMemory($result) {
    	pg_free_result($result);
    }

    function close() {
    	pg_close($this->connection);
    }

    function retrieve($query) {
    	$result = pg_query($this->connection,$query); //or die('Query failed: '. pg_last_error());
    	return $result;
    }

    function insert($query) {
        $result = pg_query($this->connection,$query); //or die('Query failed: '. pg_last_error());
        return $result;
    }

    function update($query) {
        $result = pg_query($this->connection,$query); //or die('Query failed: '. pg_last_error());
        return $result;
    }

    function delete($query) {
        $result = pg_query($this->connection,$query); //or die('Query failed: '. pg_last_error());
        return $result;
    }
}

?>