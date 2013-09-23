<?php 
    include('./php/signin.php');
    session_start();
    $name = $_SESSION['SESS_FIRST_NAME'] . ' ' . $_SESSION['SESS_LAST_NAME'];
?>
      <div class="navbar-wrapper">
            <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
            <div class="container">
                <div class="navbar navbar-inverse">
                    <div class="navbar-inner">
                        <div class="container"> <a class="btn btn-navbar" data-toggle="collapse" data-target=".navbar-responsive-collapse">
						                    <span class="icon-bar"></span>
						                    <span class="icon-bar"></span>
						                    <span class="icon-bar"></span>
						                  </a><a class="brand" href="#">Dashboard<sup><small></small></sup></a>

                            <div class="nav-collapse collapse navbar-responsive-collapse">
                                <ul class="nav">
                                    <li class="active"><a href="main.php">Home</a>
                                    </li>
                                    </li>
                                    <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Visualization <b class="caret"></b></a>
                                        <ul class="dropdown-menu">
                                            <li id="menuenglish"><a href="#">English</a>

                                            </li>
                                            <li id="menuspanish"><a href="#">Spanish (Español)</a>

                                            </li>
                                        </ul>
                                    </li>
                                    <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown">Data Entry <b class="caret"></b></a>

                                        <ul class="dropdown-menu">
                                            <li><a href="#">Milestones</a>

                                            </li>
                                            <li><a href="#">Performance</a>

                                            </li>
                                            <li><a href="#">Risks</a>

                                            </li>
                                            <li class="divider"></li>
                                            <li class="nav-header">Nav header</li>
                                            <li><a href="#">Separated link</a>

                                            </li>
                                            <li><a href="#">One more separated link</a>

                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                                <form class="navbar-search pull-left" action="">
                                    <input type="text" class="search-query" placeholder="Search">
                                    <div class="icon-search"></div>
                                </form>
                                <ul class="nav pull-right">
                                    <li><a href="#">Need help?</a>

                                    </li>
                                    <li class="divider-vertical"></li>
                                    <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown"><?php echo($name); ?> <b class="caret"></b></a>

                                        <ul class="dropdown-menu">
                                            <? if ($_SESSION['SESS_LEVEL'] == 'admin') : ?>
                                            <li><a id="menuAddUser" href="#">Create Account</a>
                                            </li>
                                            <li class="divider"></li>
                                            <? endif; ?>
                                            <li><a href="#">Profile</a>
                                            </li>
                                            <li><a href="#">Settings</a>
                                            </li>
                                            <li class="divider"></li>
                                            <li><a href="php/logout.php">Sign out</a>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                            <!-- /.nav-collapse -->
                        </div>
                    </div>
                    <!-- /navbar-inner -->
                </div>
            </div>
            <!-- /.container -->
        </div>



