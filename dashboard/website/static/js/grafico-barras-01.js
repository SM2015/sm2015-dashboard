google.load("visualization", "1", {
    packages: ["corechart"]
});

var indicators = {
    "AllIndicators": {
        start: "A1",
        end: "U35"
    },
    "Indicators": {
        start: "A1",
        end: "U35"
    }
};

var title = '% de mujeres inscritas en control prenatal precoz (primeras 12 semanas)';

var indicatorId = "Indicator1";

$(document).ready(function() {

    setSummaryBar();
    var DEFAULT = 'Indicator1';
    google.setOnLoadCallback(drawVisualization);

});

function setSummaryBar() {
    var indicatorsList = indicators['AllIndicators'];

    var DATA_SOURCE_URL = 'https://docs.google.com/spreadsheet/tq?key=0AjFAkwSrq381dG5zejZ0dzV4VWhoWDExaXU2TjdjT2c&sheet=Q1 2013 ES&range=' + indicatorsList.start + ':' + indicatorsList.end + '&pub=1';

    var query = new google.visualization.Query(DATA_SOURCE_URL);

    query.setQuery('select B, Q');

    query.send(handleQuerySummaryIndicators);

}

var indicatorsGoal = {};

function handleQuerySummaryIndicators(response) {

    var data = response.getDataTable();

    var numRows = data.getNumberOfRows();

    var output = $('#inIndicator');

    for (var i = 0; i < numRows; i++) {

        var index = i;
        var indicator = data.getValue(i, 0);
        var average = data.getValue(i, 1);

        //if (average <= 1) average = toInt(data.getValue(i, 1) * 100);
        //else average = toInt(data.getValue(i, 1));

        average = toInt(data.getValue(i, 1) * 100);
        
        if (index >= 0 && indicator && average) {
            var incrIdx = ++index
            indicatorsGoal['Indicator' + incrIdx] = {
                "average": average
            };

            var indicatorIndexHtml = '<td class="AK">' + incrIdx + '</td>';

            var indicatorHtml = '<td class = "JE" id = "Indicator' + incrIdx + '"><div class="yq meb" >' + indicator + '</div></td >';

                            var averageHtml = "<td class='Cw g4' id=''><div class='PT' style='width: " + average + "%;'></div>" + average + "%</td>";
/*
            if (average <= 100) {

                var averageHtml = "<td class='Cw g4' id=''><div class='PT' style='width: " + average + "%;'></div>" + average + "%</td>";

            } else {
                var averageHtml = "<td class='Cw g4' id=''>" + numberWithCommas(average) + "</td>";

            }
*/
            var indicatorRowHtml = '<tr class="xdb">' + indicatorIndexHtml + indicatorHtml + averageHtml + '</tr>';

            output.append(indicatorRowHtml);
        }
    }

    $('#Indicator1').addClass('highlight');

}

function toInt(n) {
    return Math.round(Number(n));
};

$(document).ready(function() {

    $("#dataTable > tbody > tr").live('click', function() {
        indicatorId = $(this).closest('tr').children('td.JE').attr('id');
        title = $(this).closest('tr').children('td.JE').text();
        $(this).closest('tbody').find('.highlight').removeClass('highlight');
        $(this).closest('tr').children('td.JE').children('div').addClass('highlight');

        //alert(key);
        drawVisualization();
    });
});

function drawVisualization() {

    var graphInfo = indicators['Indicators'];

    var DATA_SOURCE_URL = 'https://docs.google.com/spreadsheet/tq?key=0AjFAkwSrq381dG5zejZ0dzV4VWhoWDExaXU2TjdjT2c&sheet=Q1 2013 ES&range=' + graphInfo.start + ':' + graphInfo.end + '&pub=1';

    var query = new google.visualization.Query(DATA_SOURCE_URL);

    query.setQuery('select B, C, D, E, F, G, H, I, J, L, M, N, O, P');

    query.send(handleQueryResponse);

}

function handleQueryResponse(response) {

    if (checkStatus(response)) {
        var data = response.getDataTable();
        drawChart(data);
    }
}

function drawChart(data) {

    $('div.hm').text('T1 2013: '+ title);

    var seriesArray = [];

    // Create a view 
    var view = new google.visualization.DataView(data);

    view.setRows(view.getFilteredRows([{
        column: 0,
        value: title}]));

    var numColumns = view.getNumberOfColumns();
    var maxValue = 0;

    for (var i = 1; i < numColumns; i++) {

        var key = view.getColumnLabel(i);
        
        if (isInt(view.getValue(0, i))) value = toInt(view.getValue(0, i));
        else value = toInt(view.getValue(0, i) * 100);

        console.log('key: ' + key + ' | value: ' + value);
        
        seriesArray.push({
            "type": "column",
            "name": key,
            "data": [value]
        });

        if (value > maxValue) {
            if (value <= 100) maxValue = 100;
            else maxValue = value;
        }

    }

    console.log(maxValue);

    var splineAverageData = {
        name: 'Promedio Actual',
        data: [indicatorsGoal[indicatorId].average],
        marker: {
            //symbol: 'url(http://97.107.129.138/linha.png)'
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[3],
            fillColor: 'white'
        }
    };

    seriesArray.push(splineAverageData);

    var chart;

    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            marginTop: 20,
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: [''],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            max: maxValue,
            title: {
                text: 'Porcentaje',
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = '' + this.point.name + ': ' + this.y + ' fruits';
                } else {
                    s = '' + this.series.name + ': ' + this.y;
                }
                return s;
            }
        },
        credits: {
            enabled: false
        },
        series: seriesArray
    });


}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function isInt(n) {
   return n != 1 && n % 1 == 0;
}

function checkStatus(response) {

    if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return false;
    }

    return true;
}
