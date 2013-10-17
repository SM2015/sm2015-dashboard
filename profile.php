<?php 
    include('./php/signin.php');
    require_once('./php/trans.php');
    include('./php/loginClass.php');

    $login = new Login();
    $user = null;
    if (isset($_GET['id'])) {
        $user = $login->getInfoDatabase($_GET['id']);
    } else {
        $user = $login->getInfoDatabase($_SESSION['SESS_MEMBER_ID']);
    }
    $userCountries = $user->countries;
    $level = $_SESSION['SESS_LEVEL'];
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
                @import "./css/bootstrap.css";
                @import "./css/dataTables.bootstrap.css";

        #container {
            padding-top: 60px !important;
            width: 940px !important;
        }
        #dt_example .big {
            font-size: 1.3em;
            line-height: 1.45em;
            color: #111;
            margin-left: -10px;
            margin-right: -10px;
            font-weight: normal;
        }
        #dt_example {
            font: 85%/1.40em "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
            color: #111;
        }
        div.dataTables_wrapper, table {
            font: 13px/1.40em "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
        }
        #dt_example h1 {
            font-size: 16px !important;
            color: #111;
        }
        #footer {
            line-height: 1.45em;
        }
        div.examples {
            padding-top: 1em !important;
        }
        div.examples ul {
            padding-top: 1em !important;
            padding-left: 1em !important;
            color: #111;
        }
      table {
        margin: 1em 0;
        clear: both;
        width: 80%;
        float: center;
        margin-left: 10px;
      }
    
    </style>

        <link rel="stylesheet" type="text/css" href="./css/style.css">
        <link rel="stylesheet" type="text/css" href="./css/bootstrap-responsive.css">
    <script type="text/javascript" charset="utf-8" src="./js/utils.js"></script>
    </head>
    
    <body>
        <!-- Part 1: Wrap all page content here -->
        <div id="wrap">
            <!-- NAVBAR -->
      <?php include 'menu.php'; ?>
            <!-- /.navbar-wrapper -->

            <!-- Begin page content -->
            <div class="container">
                <div class="page-header" id="follow">
                <h2>Profile</h2>
                </div>
                <!-- Form -->
                <form class="form-horizontal" id="formEditUser">
                    <fieldset>
                        <legend>Required fields are followed by <strong><abbr title="required">*</abbr></strong>.</legend>
                        <div class="control-group">
                            <label class="control-label">First Name:</label>
                            <div class="controls">
                                <input id="formeditfirstname" value="<?= $user->fname; ?>" name="firstname" type="text" required />
                                <strong><abbr title="required">*</abbr></strong>
                            </div>
                        </div>
                        <div class="control-group">
                            <label class="control-label">Last Name:</label>
                            <div class="controls">
                                <input id="formeditlastname" value="<?= $user->lname; ?>" name="formlastname" type="text" required />
                                <strong><abbr title="required">*</abbr></strong>
                            </div>
                        </div>
                        <div class="control-group">
                            <label class="control-label">Password:</label>
                            <div class="controls">
                                <input id="formeditemailuser" value="<?= $user->password; ?>" name="formemailuser" type="password" required />
                                <strong><abbr title="required">*</abbr></strong>
                            </div>
                        </div>
                        <div class="control-group">
                            <label class="control-label">Phone:</label>
                            <div class="controls">
                                <input id="formeditphoneuser" value="<?= $user->contact; ?>" name="formphoneuser" type="text" />
                            </div>
                        </div>
                        <? if ($level == 'admin'): ?>
                        <div class="control-group">
                            <label class="control-label">Level:</label>
                            <div class="controls">
                                <select id="formeditleveluser">
                                  <option value="leader">Leader</option>
                                  <option selected="selected" value="user">User</option>
                                </select>
                            </div>
                        </div>
                    <? endif; ?>
                        <div class="control-group">
                            <label class="control-label">Countries:</label>
                            <div class="controls">
                                <label class="checkbox" for="belize"><input id="belize" type="checkbox" value="Belize" class="inputCountries"/> Belize</label>
                                <label class="checkbox"  for="costarica"><input id="costarica" type="checkbox" value="Costa Rica" class="inputCountries" /> Costa Rica</label>
                                <label class="checkbox"  for="elsalvador"><input id="elsalvador" type="checkbox" value="El Salvador" class="inputCountries" /> El Salvador</label>
                                <label class="checkbox"  for="honduras"><input id="honduras" type="checkbox" value="Honduras" class="inputCountries" /> Honduras</label>
                                <label class="checkbox"  for="guatemala"><input id="guatemala" type="checkbox" value="Guatemala" class="inputCountries" /> Guatemala</label>
                                <label class="checkbox"  for="mexico"><input id="mexico" type="checkbox" value="Mexico" class="inputCountries" /> Mexico</label>
                                <label class="checkbox"  for="nicaragua"><input id="nicaragua" type="checkbox" value="Nicaragua" class="inputCountries" /> Nicaragua</label>
                                <label class="checkbox"  for="panama"><input id="panama" type="checkbox" value="Panama" class="inputCountries" /> Panama</label>
                            </div>
                        </div>
                        <div class="control-group">
                            <div class="controls">
                                <button type="submit" class="btn">Edit Profile</button>
                            </div>
                        </div>
                        <div class="control-group">
                        <div id="alert-create-user" class="alert alert-block alert-warn fade in">
                          <p id="alert-create-user-msg"></p>
                        </div>
                    </div>
                    </fieldset>
                </form>
            </div>
        </div>
        <div id="footer">
            <div class="container">
                <p class="muted credit">© Copyright 2013. Banco Interamericano de Desarrollo, como administrador del Fondo Mesoamericano de Salud - <a href="http://sm2015.org">Salud Mesoamérica 2015</a>.</p>
            </div>
        </div>

        <!-- Le javascript==================================================- ->
        <!-- Placed at the end of the document so the pages load faster -->
    </body>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    <script src="./js/utils.js"></script>
    <script src="./js/services.js"></script>
    <script src="./js/dashboard.js"></script>
    <script src="./js/menu.js"></script>
    <script type="text/javascript">
        var countryForm = '<?= $userCountries; ?>'.split(',');
        var checkboxs = $("form input:checkbox");
        checkboxs.each(function (index, elem) {
            for (var i = 0; i < countryForm.length; i++) {
                if (elem.value.toLowerCase() == countryForm[i].toLowerCase()) {
                    $(elem).attr('checked', true);
                }
            }
        });
    </script>
</html>