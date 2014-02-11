(function( $ ){
    function loadGraph($wrapper){
        $wrapper.find("*").remove();

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
                              '<td style="width: 160px; font-size: 0.9em;">'+
                                '<div id="control1">'+
                                  '<form>'+
                                       '<fieldset>'+
                                          '<legend>Country</legend>'+
                                          '<p>'+
                                             '<select id = "operationList">'+
                                               '<option value = "BL-G1001">Belize</option>'+
                                               '<option value = "CR-G1001">Costa Rica</option>'+
                                               '<option value = "ES-G1001">El Salvador</option>'+
                                               '<option value = "GU-G1001">Guatemala</option>'+
                                               '<option value = "HO-G1001">Honduras</option>'+
                                               '<option value = "NI-G1001">Nicaragua</option>'+
                                               '<option value = "ME-G1001">Mexico</option>'+
                                               '<option value = "PN-G1001">Panama</option>'+
                                             '</select>'+
                                          '</p>'+
                                       '</fieldset>'+
                                    '</form>'+
                                    ''+
                                 '</div>'+
                                '<div id="control2" style="display: none;"></div>'+
                                '<div id="control3"></div>'+
                              '</td>'+
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

        $wrapper.html(html);
        var DEFAULT = 'BL-G1001';
        google.setOnLoadCallback(drawVisualization(DEFAULT));
        $("#operationList").val(DEFAULT).attr('selected', true);
        $("#operationList").change(function() {
            drawVisualization($(this).val());
        });

    }

    google.load("visualization", "1", {
        packages: ["corechart"]
    });

    google.load('visualization', '1', {
        packages: ['table']
    });

    var operations = {
        "ME-G1001": {
            country: 'Mexico',
            start: "A120",
            end: "G156"
        },
        "BL-G1001": {
            country: 'Belize',
            start: "A63",
            end: "G99"
        },
        "ES-G1001": {
            country: 'El Salvador',
            start: "A68",
            end: "G104"
        },
        "HO-G1001": {
            country: 'Honduras',
            start: "A64",
            end: "G100"
        },
        "NI-G1001": {
            country: 'Nicaragua',
            start: "A67",
            end: "G103"
        },
        "PN-G1001": {
            country: 'Panama',
            start: "A52",
            end: "G88"
        },
        "GU-G1001": {
            country: 'Guatemala',
            start: "A54",
            end: "G90"
        },
        "CR-G1001": {
            country: 'Costa Rica',
            start: "A124",
            end: "G160"
        }

    };


    function drawVisualization(ope) {

        var operationInfo = operations[ope];

        var DATA_SOURCE_URL = 'https://docs.google.com/spreadsheet/tq?key=0AjFAkwSrq381dFJkZkd2YXdXLUNJdFlwTHRwb3NNOVE&sheet=' + operationInfo.country + '&range=' + operationInfo.start + ':' + operationInfo.end + '&pub=1';
        console.log(DATA_SOURCE_URL);

        //alert(DATA_SOURCE_URL);
        var query = new google.visualization.Query(DATA_SOURCE_URL);

        // Optional request to return only column C and the sum of column B, grouped by C members.
        query.setQuery('select D, B, sum(G) group by D, B');

        // Send the query with a callback function.
        query.send(handleQueryResponse);

    }

    function handleQueryResponse(response) {

        if (checkStatus(response)) {

            var data = response.getDataTable();
            console.log(data);

            var dataTable = new google.visualization.DataTable();
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
                            var newValue = status[type].value + value;
                            status[type] = {
                                value: newValue
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

            console.log(dataTable)
            drawChart(dataTable, 'chart1', 'Country Disbursement tracking per Quarter ( US$ )');

        }
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

        var table = new google.visualization.Table(document.getElementById('chart2'));
        table.draw(data, {
            allowHtml: true,
            showRowNumber: true
        });


    }

    function checkStatus(response) {

        if (response.isError()) {
            alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
            return false;
        }

        return true;
    }

    $.fn.graficoDisbursement = function() {
        var wrapper = this;
        loadGraph( this );

        $(this).find(".reload").click(function(){
            loadGraph( wrapper );
        });
        return this;
    };
}( jQuery ));
