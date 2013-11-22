<?php include('./php/signin.php'); ?>
<?php require_once('./php/trans.php'); ?>
<?php
$home = _t('HOME_PAGE', $_SESSION['SESS_LANG']);
?>

<?php include_once('./header.php') ?>

<!-- BEGIN CONTAINER -->
<div class="page-container row-fluid"> 

    <?php include_once('./sidebar.php') ?>
    
    <div class="page-content"> 
        <div class="map-container">
            <script>
                var map;
                function initialize() {
                  /* Geo LatLng */
                  var geoGuatemala = new google.maps.LatLng(15.961329,-90.981447);
                  /* END OF Geo LatLng */

                  var mapOptions = {
                    zoom: 4,
                    center: geoGuatemala
                  };
                  map = new google.maps.Map(document.getElementById('map-goals'), mapOptions);
                  var markerIcon = 'img/green_waypoint.png';

                  /* InfoWIdows */
                  var InfoBoxHTML = ''+
                    '<div class="content-info-window">'+
                        '<div class="arrow-container"></div>'+
                        '<div class="left-side">'+
                            '<div class="main-info">'+
                                '<h4 class="title-info">{TITLE}</h4>'+
                                '<p class="desc">Meta: melhorar o acesso.</p>'+
                            '</div>'+
                            '<a class="more-info" href="#">Más infos</a>'+
                        '</div>'+
                        '<div class="right-side">'+
                            '<div class="statistics">'+
                                '<span class="label-stats">Objetivos</span>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
    
                  var infoBoxDefault = document.createElement("div");
                    infoBoxDefault.className = 'content-info-window'
                    infoBoxDefault.innerHTML = InfoBoxHTML;

                  var infoBoxOptions = {
                      disableAutoPan: false
                      ,maxWidth: 0
                      ,pixelOffset: new google.maps.Size(0, -140)
                      ,zIndex: null
                      ,boxStyle: {
                        width: '522px'
                      }
                      ,closeBoxMargin: "10px 40px 0px 0px"
                      ,closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif"
                      ,infoBoxClearance: new google.maps.Size(1, 1)
                      ,isHidden: false
                      ,pane: "floatPane"
                      ,enableEventPropagation: false
                  };
                  /* END OF InfoWIdows */

                  /* Markers */
                  var markerGuatemala = new google.maps.Marker({
                      position: geoGuatemala,
                      map: map,
                      icon: markerIcon,
                      visible: true
                  });

                  var infoBoxGuatemalaOptions = infoBoxOptions;
                  infoBoxGuatemalaOptions.content = infoBoxDefault.innerHTML.replace("{TITLE}", "Guatemala");
                  var infoBoxGuatemala = new InfoBox(infoBoxGuatemalaOptions);
                  infoBoxGuatemala.open(map, markerGuatemala);
                  /* END OF Markers */


                }

                google.maps.event.addDomListener(window, 'load', initialize);
            </script>
            <div id="map-goals"></div>
        </div>

        <div class="content">  
           <div id="container">
                <div class="row-fluid spacing-bottom 2col">	
                    <div class="span9 grafico-barra-01">	
                        <div class="F4" id="ID-overview-narrative">
                            <div class="hm"></div>
                        </div>

                        <table class="p5">
                            <tbody>
                                <tr>
                                    <td><div id="indicator-graph" class="Oqb">
                                            <table class="in">
                                                <tbody>
                                                    <tr>
                                                        <td class="Yf">
                        <div id="container" style="min-width: 800px; height: 400px; margin: 0 auto"></div>
                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div></td>
                                </tr>
                                  
                            </tbody>
                        </table>

                        <div class="Jdb">
                            <div id="miniTable" class="fZ">
                                <table class="gc CQ" id="dataTable">
                                    <tbody id="inIndicator">
                                        <tr>
                                            <th class="Ru"></th>
                                            <th class="uE ">Proxy - Coberturas institutionales calculados por el MINSAL</th>
                                            <th class="Cw">Promedio Reportado</th>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        
                    </div>
                    <div class="span3 ">	
                        (grafico)
                    </div>
		        </div>
           </div> 
        </div>  
    </div>
</div>
<!-- END CONTAINER --> 

<?php include_once('./footer.php') ?>
