(function( $ ){
    google.load("visualization", "1", {
        packages: ["corechart"]
    });

    google.load('visualization', '1', {
        packages: ['table']
    });

    function loadGraph($wrapper, country_slug){
        $wrapper.find("*").remove();

        if(!country_slug){
          var countriesTableCell = ''+
            '<td style="width: 160px; font-size: 0.9em;">'+
              '<div id="control1">'+
                '<form>'+
                    '<fieldset>'+
                        '<legend>Country</legend>'+
                        '<p>'+
                           '<select id = "operationList">'+
                             '{OPTIONS_COUNTRIES}'+
                           '</select>'+
                        '</p>'+
                    '</fieldset>'+
                '</form>'+
                ''+
              '</div>'+
              '<div id="control2" style="display: none;"></div>'+
              '<div id="control3"></div>'+
            '</td>';
        } else {
          var countriesTableCell = '';
        }

        var html = ''+
            '<div class="span12">'+
                '<div class="grid simple">'+
                  '<div class="grid-title no-border">'+
                    '<h4></h4>'+
                    '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
                  '</div>'+
                  '<div class="grid-body no-border">'+
                    '<div class="row-fluid">'+
                        '<table>'+
                            '<tr style="vertical-align: top;">'+
                              countriesTableCell+
                              '<td style="width: 680px">'+
                                '<div style="float: left;" id="chart1"></div>'+
                                '<div style="float: left;" id="chart2"></div>'+
                                '<div style="float: left;" id="chart3"></div>'+
                              '</td>'+
                            '</tr>'+
                        '</table>'+
                    '</div>'+
                  '</div>'+
                '</div>'+
            '</div>';

        if(!country_slug){
          $.getJSON('/country/list', function(response){
            var options_countries = [];
            $.each(response, function(){
              options_countries.push('<option value="'+this.slug+'">'+this.name+'</option>');
            });
            html = html.replace("{OPTIONS_COUNTRIES}", options_countries.join())

            $wrapper.html(html);

            var DEFAULT = 'belize';
            drawVisualization('belize');
            $("#operationList").change(function() {
                drawVisualization($(this).val());
            });
          });
        } else {
          $wrapper.html(html);
          drawVisualization(country_slug);
        }
    }

    function drawVisualization(country_slug) {
        $.getJSON('/graphs/country_disbursement/'+country_slug+'/', handleQueryResponse);
    }

    function handleQueryResponse(data_json) {
        var dataTable = new google.visualization.DataTable(),
            data = new google.visualization.DataTable(data_json);

        dataTable.addColumn('string', 'Quarter');
        dataTable.addColumn('number', 'SM2015 Projected Disbursements (IT + PT)');
        dataTable.addColumn('number', 'SM2015 Actual Disbursements');
        dataTable.addColumn('number', 'Planned Financial Execution');
        dataTable.addColumn('number', 'Actual Financial Execution');

        var numRows = data.getNumberOfRows();
        var quarter = data.getValue(0, 0);
        var status = new Array();

        validateQuarter('2011Q4');


        for (var i = 0; i < numRows; i++) {

            if (quarter.indexOf(data.getValue(i, 0)) != -1) {

                var type = data.getValue(i, 1);
                var value = data.getValue(i, 2);

                if (typeof status[type] !== 'undefined' && status[type] !== null) {

                    if (type.indexOf("Actual") > -1) {
                        if (validateQuarter(quarter)) {
                            var newValue = status[type].value + value;
                            status[type] = {
                                value: newValue
                            };

                        }else{
                            status[type] = {
                                value: null
                            };
                            
                        }   
                    } else {
                        status[type] = {
                            value: value
                        };
                    }
                } else {
                    status[type] = {
                        value: value
                    };

                }

            } else {

                addRow(dataTable, quarter, status);

                quarter = data.getValue(i, 0);
                i--;
            }

        }

        addRow(dataTable, quarter, status);

        drawChart(dataTable, 'chart1', 'Country Disbursement tracking per Quarter ( US$ )');
    }

    function toInt(n) {
        return Math.round(Number(n));
    };

    function validateQuarter(inQuarter) {

        var now = new Date();
        var currentQuarter = toInt((now.getMonth() + 3) / 3);
        var nowYr = toInt(now.getFullYear());

        var databaseYr = toInt(inQuarter.substring(0, inQuarter.lastIndexOf('Q')));
        var databaseQuarter = toInt(inQuarter.substring(inQuarter.lastIndexOf('Q') + 1, inQuarter.lenght));

        if (databaseYr < nowYr) {
            //alert(databaseYr + 'Q' + databaseQuarter);
            return true;

        } else if (databaseYr == nowYr) {
            if (databaseQuarter <= currentQuarter) {
                //alert(databaseYr + 'Q' + databaseQuarter);
                return true;
            } else {
                return false;
            }

        } else {
            return false
        }

    }

    function addRow(dataTable, quarter, status) {
        var sumDisbursement = status['SM2015 Projected Disbursements'] ? status['SM2015 Projected Disbursements'].value : 0;
        var sumCounterpart = status['SM2015 Actual Disbursements'] ? status['SM2015 Actual Disbursements'].value : 0;
        var sumSM2015Actual = status['Planned Financial Execution'] ? status['Planned Financial Execution'].value : 0;
        var sumActualCountry = status['Actual Financial Execution'] ? status['Actual Financial Execution'].value : 0;

        dataTable.addRow([quarter, sumDisbursement, sumCounterpart, sumSM2015Actual, sumActualCountry]);

        // alert(sumActual);
    }

    function drawChart(data, visualizationTag, title) {

        var options = {
            width: 800,
            height: 400,
            title: title,
            pointSize: '4',
            legend: {
                position: 'right'
            },
            animation: {
                duration: 1000,
                easing: 'in'
            },
            hAxis: {
                type: 'string',
                title: 'Quarter',
                titleTextStyle: {
                    color: 'black'
                }
            },
            vAxis: {
                title: 'US$',
                titleTextStyle: {
                    color: 'black'
                }
            },
            strictFirstColumnType: 'true'
        }

        var chart = new google.visualization.LineChart(document.getElementById('chart1'));
        chart.draw(data, options);


        var formatter = new google.visualization.NumberFormat({
            prefix: '$',
            negativeColor: 'red',
            negativeParens: true
        });
        formatter.format(data, 1);
        formatter.format(data, 2);
        formatter.format(data, 3);
        formatter.format(data, 4);

    }

    function checkStatus(response) {

        if (response.isError()) {
            alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
            return false;
        }

        return true;
    }

    $.fn.graficoDisbursement = function(country_slug) {
        var wrapper = this;
        loadGraph( this, country_slug );

        $(this).find(".reload").click(function(){
            loadGraph( wrapper, country_slug );
        });
        return this;
    };
}( jQuery ));
