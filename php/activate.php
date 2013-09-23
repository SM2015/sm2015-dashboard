<?php

include_once ('database.php');

if (isset($_GET['email']) && preg_match('/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/', $_GET['email'])) {
  $email = $_GET['email'];
}

if (isset($_GET['key']) && (strlen($_GET['key']) == 32))
 //The Activation key will always be 32 since it is MD5 Hash
 {
  $key = $_GET['key'];
}

if (isset($email) && isset($key)) {

  $db = new Database();
  $db->connect();

 // Update the database to set the "activation" field to null
 $query_activate_account = "UPDATE member SET activation=NULL WHERE username='$email' AND activation='$key'";
 $result_activate_account = $db->update($query_activate_account);


 // Print a customized message:
 if (pg_affected_rows($result_activate_account) == 1) //if update query was successfull
 {
 // echo '<div>Your account is now active. You may now <a href="../index.php">Log in</a></div>';
 ?>
 <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Sign in &middot; Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="../css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
      }

      .form-signin {
        max-width: 300px;
        padding: 19px 29px 29px;
        margin: 0 auto 20px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
        -webkit-border-radius: 5px;
           -moz-border-radius: 5px;
                border-radius: 5px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.05);
           -moz-box-shadow: 0 1px 2px rgba(0,0,0,.05);
                box-shadow: 0 1px 2px rgba(0,0,0,.05);
      }
      .form-signin .form-signin-heading,
      .form-signin .checkbox {
        margin-bottom: 10px;
      }
      .form-signin input[type="text"],
      .form-signin input[type="password"] {
        font-size: 16px;
        height: auto;
        margin-bottom: 15px;
        padding: 7px 9px;
      }

    </style>
    <link href="../css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="../assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="../assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="../assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="../assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="../assets/ico/favicon.png">
  </head>

  <body>

    <div class="container">

      <form class="form-signin" name="form-activity" id="form-activity">
        <h2 class="form-signin-heading">Please set your password</h2>
        <input id="activity-password" type="password" class="input-block-level" placeholder="Password" required />
        <input id="activity-password-confirm" type="password" class="input-block-level" placeholder="Confirm Password" required />
        <button class="btn btn-large btn-primary" type="submit">Sign in</button>
      </form>

      <div id="alert-error-activity" class="alert alert-block alert-error fade in" style="display:none; margin: 0 auto 20px; max-width: 300px;">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <h4 class="alert-heading">Set password error</h4>
        <p id="alert-msg-activity">Please, try again or send a message for admin@sm2015.org!</p>
      </div>
      <!-- TODO the code validation INPUT MUST VALIDATION JAVASCRIPT -->

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/services.js"></script>
    <script src="../js/utils.js"></script>
    <script src="../js/dashboard.js"></script>
  </body>
</html>
<?php
 } else {
 echo '<div>Oops !Your account could not be activated. Please recheck the link or contact the system administrator.</div>';
 }

} else {
 echo '<div>Error Occured .</div>';
}
$db->close();
?>