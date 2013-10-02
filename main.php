<?php include('./php/signin.php'); ?>
<?php require_once('./php/trans.php'); ?>
<?php
$home = _t('HOME_PAGE', $_SESSION['SESS_LANG']);
?>
<!DOCTYPE html>
<html lang="en">
    
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Dashboard Web</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <!-- Le styles -->
        <link href="./css/bootstrap.css" rel="stylesheet">
        <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
            <script src="../assets/js/html5shiv.js"></script>
        <![endif]-->
        <!-- Fav and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="./ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="./ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="./ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="./ico/apple-touch-icon-57-precomposed.png">
        <link rel="shortcut icon" href="./ico/favicon.png">
        <style type="text/css">
            #container {
                padding-top: 60px !important;
                width: 940px !important;
            }
            .container > hr {
                margin: 60px 0;
            }
            /* Main marketing message and sign up button */
            .jumbotron {
                margin: 40px 0;
                text-align: center;
            }
            .jumbotron h1 {
                font-size: 50px;
                line-height: 1;
            }
            .jumbotron .lead {
                font-size: 24px;
                line-height: 1.25;
            }
            .jumbotron .btn {
                font-size: 21px;
                padding: 14px 24px;
            }
            /* Supporting marketing content */
            .marketing {
                margin: 60px 0;
            }
            .marketing p + h4 {
                margin-top: 20px;
            }
            /* Customize the navbar links to be fill the entire space of the .navbar */
        </style>
  		   
		<link rel="stylesheet" type="text/css" href="./css/style.css">
	    <link rel="stylesheet" type="text/css" href="./css/bootstrap-responsive.css">

    </head>
    
    <body>
        <!-- Part 1: Wrap all page content here -->
        <div id="wrap">
            <!-- NAVBAR -->
			<?php include 'menu.php'; ?>
	        <!-- /.navbar-wrapper -->
     
       		<div class="container">
                <!-- Jumbotron -->
                <div class="jumbotron">
                     <h1>SM2015 Dashboard</h1>

                    <p class="lead"><?php echo($home); ?></p>

                </div>
                <hr>
                <!-- Example row of columns -->
                <div class="row-fluid">
                    <div class="span4">
                         <h2>Milestones</h2>

                        <p>To update your milestones, please click on the 'View milestones' button below. The information will also update the Dashboard Website. Condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.</p>
                        <p><a class="btn" href="./milestones.php">Manage milestones &raquo;</a>
                        </p>
                    </div>
                    <div class="span4">
                         <h2>Advances</h2>

                        <p>To update the advances (triangle), please click on the advances button. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa. Justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.</p>
                        <p><a class="btn" href="./milestones.php">Manage advances &raquo;</a>
                        </p>
                    </div>
                    <div class="span4">
                         <h2>Risks</h2>

                        <p>To update risk table, please click on the risk button. There is no graphic on the dashboard linked to this information, it is only included in the report when you export. Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. </p>
                        <p><a class="btn" href="./milestones.php">Manage risks &raquo;</a>
                        </p>
                    </div>
                </div>
                <hr>
            </div>
        </div>
        <div id="footer">
            <div class="container">
                <p class="muted credit">© Copyright 2012. Banco Interamericano de Desarrollo, como administrador del Fondo Mesoamericano de Salud - <a href="http://sm2015.org">Salud Mesoamérica 2015</a>.</p>
            </div>
        </div>
        <!-- Le javascript==================================================- ->
		    <!-- Placed at the end of the document so the pages load faster -->
        <script src="http://code.jquery.com/jquery.js"></script>
        <script src="./js/bootstrap.min.js"></script>
        <script src="./js/utils.js"></script>
        <script src="./js/services.js"></script>
        <script src="./js/dashboard.js"></script>
        <script src="./js/menu.js"></script>
    </body>
</html>