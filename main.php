<!DOCTYPE html>
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<head>
<meta charset="utf-8" />
<title>Webarch - Responsive Admin Dashboard</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<meta content="" name="description" />
<meta content="" name="author" />

<!-- BEGIN PLUGIN CSS -->
<link href="assets/plugins/fullcalendar/fullcalendar.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/pace/pace-theme-flash.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/gritter/css/jquery.gritter.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/bootstrap-datepicker/css/datepicker.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="assets/plugins/jquery-ricksaw-chart/css/rickshaw.css" type="text/css" media="screen" charset="utf-8">
<link rel="stylesheet" href="assets/plugins/jquery-morris-chart/css/morris.css" type="text/css" media="screen" charset="utf-8">
<link href="assets/plugins/jquery-slider/css/jquery.sidr.light.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/bootstrap-select2/select2.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/jquery-jvectormap/css/jquery-jvectormap-1.2.2.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/boostrap-checkbox/css/bootstrap-checkbox.css" rel="stylesheet" type="text/css" media="screen"/>
<!-- END PLUGIN CSS -->

<!-- BEGIN CORE CSS FRAMEWORK -->
<link href="assets/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/font-awesome/css/font-awesome.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/animate.min.css" rel="stylesheet" type="text/css"/>
<!-- END CORE CSS FRAMEWORK -->

<!-- BEGIN CSS TEMPLATE -->
<link href="assets/css/style.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/responsive.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/custom-icon-set.css" rel="stylesheet" type="text/css"/>
<!-- END CSS TEMPLATE -->

<link href="css/custom-sm2012.css" rel="stylesheet" type="text/css"/>
<link href="css/maps-custom.css" rel="stylesheet" type="text/css"/>
<link href="css/custom-sm2012.css" rel="stylesheet" type="text/css"/>
<link href='http://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>

</head>
<!-- END HEAD -->

<!-- BEGIN BODY -->
<body class="">
<!-- BEGIN HEADER -->
<div class="header navbar navbar-inverse "> 
  <!-- BEGIN TOP NAVIGATION BAR -->
  <div class="navbar-inner">
	<div class="header-seperation"> 
		<ul class="nav pull-left notifcation-center" id="main-menu-toggle-wrapper" style="display:none">	
		 <li class="dropdown"> <a id="main-menu-toggle" href="#main-menu"  class="" > <div class="iconset top-menu-toggle-white"></div> </a> </li>		 
		</ul>
      <!-- BEGIN LOGO -->	
      <a href="#"><img src="img/sm2015_tablero_logo.png" class="logo"  data-src="img/sm2015_tablero_logo.png" data-src-retina="img/sm2015_tablero_logo.png" width="165"/></a>
      <!-- END LOGO --> 
      <ul class="nav pull-right notifcation-center">	
        <li class="dropdown" id="header_task_bar"> <a href="main.php" class="dropdown-toggle active" data-toggle=""> <div class="iconset top-home"></div> </a> </li>
      </ul>
      </div>
      <!-- END RESPONSIVE MENU TOGGLER --> 
      <div class="header-quick-nav" > 
      <!-- BEGIN TOP NAVIGATION MENU -->
	  <div class="pull-left"> 
		  <ul class="nav quick-section">
			<li class="quicklinks"> <a href="#" class="" id="layout-condensed-toggle" ><div class="iconset top-menu-toggle-white"></div> </a> </li>        
		  </ul>
		  <ul class="nav quick-section">
			<div class="input-prepend inside search-form no-boarder">
				<span class="add-on"> <a href="#" class="" ><div class="iconset top-search"></div></a></span>
				 <input name="" type="text"  class="no-boarder " placeholder="Search Dashboard" style="width:250px;">
			</div>
		  </ul>
	  </div>
	 <!-- END TOP NAVIGATION MENU -->
	 <!-- BEGIN CHAT TOGGLER -->
      <div class="pull-right"> 
		<div class="chat-toggler">	
				<a href="#" class="dropdown-toggle" id="my-task-list">
					<div class="user-details"> 
						<div class="username">
							Hola, <span class="bold">Emma</span>									
						</div>						
					</div> 
				</a>						
			</div>
		 <ul class="nav quick-section ">
			<li class="quicklinks"> 
				<a data-toggle="dropdown" class="dropdown-toggle  pull-right" href="#">						
					<div class="iconset top-settings-dark "></div> 	
				</a>
				<ul class="dropdown-menu  pull-right" role="menu" aria-labelledby="dropdownMenu">
                  <li><a href="user-profile.html"> My Account</a>
                  </li>
                  <li><a href="calender.html">My Calendar</a>
                  </li>
                  <li><a href="email.html"> My Inbox&nbsp;&nbsp;<span class="badge badge-important animated bounceIn">2</span></a>
                  </li>
                  <li class="divider"></li>                
                  <li><a href="login.html"><i class="icon-off"></i>&nbsp;&nbsp;Log Out</a></li>
               </ul>
			</li> 
		</ul>
      </div>
	   <!-- END CHAT TOGGLER -->
      </div> 
      <!-- END TOP NAVIGATION MENU --> 
   
  </div>
  <!-- END TOP NAVIGATION BAR --> 
</div>
</div>
<!-- END HEADER --> 
<!-- BEGIN CONTAINER -->
<div class="page-container row-fluid"> 
  <!-- BEGIN SIDEBAR -->
  <div class="page-sidebar" id="main-menu"> 
  
  <!-- BEGIN MINI-WIGETS -->

   <!-- END MINI-WIGETS -->
   
   <!-- BEGIN SIDEBAR MENU -->	
    <ul>	
      <li class="start active "> <a href="#" class="clearfix"> <i class="icon-custom-dashboard"></i> <span class="title">Mi Tablero</span></a> </li>
      <li class="start "> <a href="#"> <i class="icon-custom-paises"></i> <span class="title">Paises</span></a> </li>
      <li class="start "> <a href="#"> <i class="icon-custom-gantz"></i> <span class="title">Gantz & Finanzas</span></a> </li>
      <li class="start "> <a href="#"> <i class="icon-custom-sm"></i> <span class="title">SM2015</span></a> </li>
      <li class="start "> <a href="#"> <i class="icon-custom-reports"></i> <span class="title">Informes</span></a> </li>
      <li class="start "> <a href="#"> <i class="icon-custom-db"></i> <span class="title">Base de datos</span></a> </li>
	</ul>

	<a href="#" class="scrollup">Scroll</a>
	<div class="clearfix"></div>
    <!-- END SIDEBAR MENU --> 
  </div>
  <!-- END SIDEBAR --> 
  <!-- BEGIN PAGE CONTAINER-->
  <div class="page-content"> 
    <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
    <div id="portlet-config" class="modal hide">
      <div class="modal-header">
        <button data-dismiss="modal" class="close" type="button"></button>
        <h3>Widget Settings</h3>
      </div>
      <div class="modal-body"> Widget settings form goes here </div>
    </div>
    <div class="clearfix"></div>
    <div class="map-container">
       <div id="world-map" class="demo-map" style="min-height:400px; height: 400px;"></div>
    </div>

    <div class="content graficos-triangulo">  
        <table>
            <tr>
                <td>
                    <div id="container0" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <div id="container1" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <div id="container2" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div id="container3" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <div id="container4" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <div id="container5" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div id="container6" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <div id="container7" style="width: 300px; height: 300px; margin: 0 auto"></div>
                </td>
            </tr>
        </table>
    </div>
  </div>  
  <!-- END PAGE --> 
</div>
<!-- END CONTAINER --> 

<!-- BEGIN CORE JS FRAMEWORK--> 
<script src="assets/plugins/jquery-1.8.3.min.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-ui/jquery-ui-1.10.1.custom.min.js" type="text/javascript"></script> 
<script src="assets/plugins/bootstrap/js/bootstrap.min.js" type="text/javascript"></script> 
<script src="assets/plugins/breakpoints.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-unveil/jquery.unveil.min.js" type="text/javascript"></script> 
<!-- END CORE JS FRAMEWORK --> 
<!--[if lt IE 9]>
	<script src="assets/plugins/excanvas.js"></script>
	<script src="assets/plugins/respond.js"></script>	
	<![endif]--> 

<!-- BEGIN PAGE LEVEL JS --> 
<script src="assets/plugins/pace/pace.min.js" type="text/javascript"></script>  
<script src="assets/plugins/jquery-slimscroll/jquery.slimscroll.min.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-slider/jquery.sidr.min.js" type="text/javascript"></script> 	
<script src="assets/plugins/jquery-numberAnimate/jquery.animateNumbers.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-jvectormap/js/jquery-jvectormap-1.2.2.min.js" type="text/javascript"></script> 	
<script src="assets/plugins/jquery-jvectormap/js/jquery-jvectormap-world-mill-en.js" type="text/javascript"></script> 	
<!--<script src="assets/plugins/skycons/skycons.js"></script>-->
<!-- END PAGE LEVEL PLUGINS --> 	
<!-- PAGE JS --> 	
<script src="assets/js/vector_maps.js" type="text/javascript"></script>
<!-- BEGIN CORE TEMPLATE JS --> 
<script src="assets/js/core.js" type="text/javascript"></script> 
<script src="assets/js/demo.js" type="text/javascript"></script> 
<!-- END CORE TEMPLATE JS --> 

<script type="text/javascript" src="http://www.google.com/jsapi"></script>
<script type="text/javascript" src="http://code.highcharts.com/highcharts.js"></script>
<script type="text/javascript" src="http://code.highcharts.com/modules/exporting.js"></script>
<script type="text/javascript" src="http://code.highcharts.com/highcharts-more.js"></script>

<script>
    google.load("visualization", "1", {
        packages: ["corechart"]
    });

    var WORKSHEET = "Avances NEW";

    var items = {
        "Performance": {
            start: "A1",
            end: "E33"
        }
    };

    $(document).ready(function () {
        google.setOnLoadCallback(drawVisualization());

    });

    function drawVisualization() {

        var graphInfo = items['Performance'];

        var DATA_SOURCE_URL = 'https://docs.google.com/spreadsheet/tq?key=0AjFAkwSrq381dGNLZ1RBZGFxaHlWV3VXUzluVWU0VHc&sheet=' + WORKSHEET + '&range=' + graphInfo.start + ':' + graphInfo.end + '&pub=1';

        var query = new google.visualization.Query(DATA_SOURCE_URL);

        query.send(handleQueryResponse);

    }

    function handleQueryResponse(response) {
        if (checkStatus(response)) {
            var data = response.getDataTable();
            drawChart(data)
        }
    }

    function drawChart(data) {

        var seriesArray = [];
        var categoriesArray = [];
        var dataArray = [];

        // Create a view 
        var view = new google.visualization.DataView(data);
        var numColumns = view.getNumberOfColumns();
        var numRows = data.getNumberOfRows();

        for (var i = 2; i < numColumns; i++) {
            var category = view.getColumnLabel(i);
            if (category) categoriesArray.push(category);
        }

        var index = 0;
        var div = '#container' + index;

        for (var i = 0; i <= numRows; i++) {

            if (i > 1 && !(i % 4)) {
                index++;
                console.log('div: ' + div + ' | series: ' + seriesArray);

                drawSpider(div, view.getValue(i - 1, 1), categoriesArray, seriesArray);

                seriesArray = [];
                div = '#container' + index;
                console.log('i: ' + i + ' | container' + index);
            }

            if (i < numRows) {
                var country = view.getValue(i, 1);
                var seriesName = view.getValue(i, 0);

                if (country && seriesName) {

                    for (var col = 2; col < numColumns; col++) {
                        if (isInt(view.getValue(i, col))) var value = toInt(view.getValue(i, col));
                        else value = toInt(view.getValue(i, col) * 100);

                        dataArray.push(value);
                    }

                    seriesArray.push({
                        name: seriesName,
                        data: dataArray,
                        pointPlacement: 'on'
                    });

                    dataArray = [];
                }

            }


        }

    }

    function drawSpider(div, country, categoriesArray, seriesArray) {

        Highcharts.theme = {
            colors: ['#058DC7', '#0d233a', '#bbbbbb', '#F9CCCA', '#F9CCCA', '#64E572', '#FF9655', '#FFF263', '#6AF9C4'],

            title: {
                style: {
                    color: '#000',
                    font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
                }
            },
            subtitle: {
                style: {
                    color: '#666666',
                    font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
                }
            },
            xAxis: {
                gridLineWidth: 1,
                lineColor: '#000',
                tickColor: '#000',
                labels: {
                    style: {
                        color: '#000',
                        font: '11px Trebuchet MS, Verdana, sans-serif'
                    }
                },
                title: {
                    style: {
                        color: '#333',
                        fontWeight: 'bold',
                        fontSize: '12px',
                        fontFamily: 'Trebuchet MS, Verdana, sans-serif'

                    }
                }
            },

            legend: {
                itemStyle: {
                    font: '9pt Trebuchet MS, Verdana, sans-serif',
                    color: 'black'

                },
                itemHoverStyle: {
                    color: '#039'
                },
                itemHiddenStyle: {
                    color: 'gray'
                }
            },
            labels: {
                style: {
                    color: '#99b'
                }
            },

            navigation: {
                buttonOptions: {
                    theme: {
                        stroke: '#CCCCCC'
                    }
                }
            }
        };

        // Apply the theme
        var highchartsOptions = Highcharts.setOptions(Highcharts.theme);

        $(div).highcharts({

            chart: {
                polar: true,
                type: 'line'
            },

            title: {
                text: country + ' Primera Operación SM2015'
            },

            pane: {
                size: '85%'
            },

            xAxis: {
                categories: categoriesArray,
                tickmarkPlacement: 'on',
                lineWidth: 0
            },

            yAxis: {
                gridLineInterpolation: 'polygon',
                lineWidth: 0,
                min: 0
            },

            tooltip: {
                shared: true,
                pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y}%</b><br/>'
            },
            exporting: {
                enabled: true
            },
            credits: {
                enabled: false
            },

            series: seriesArray

        });


    }

    function isInt(n) {
        return n != 1 && n % 1 == 0;
    }

    function toInt(n) {
        return Math.round(Number(n));
    };

    function checkStatus(response) {

        if (response.isError()) {
            alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
            return false;
        }

        return true;
    }
</script>

    
</body>
</html>
