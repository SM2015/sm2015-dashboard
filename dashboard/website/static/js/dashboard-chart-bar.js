(function ( $ ) {
    var dashboardChartBar = function(wrapper, url, opts){
        this.$wrapper = $(wrapper);
        this.url = url;
        this.$element;
        this.opts = opts || {};
        title = opts.title || ''
        this.html = ''+
            '<div class="grid simple">'+
              '<div class="grid-title no-border">'+
                '<h4>' + title + '</h4>'+
                '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
              '</div>'+
              '<div class="grid-body no-border">'+
                '<div class="placeholder" style="width:450px;height:250px;position:relative"></div>'+
              '</div>'+
            '</div>';

        this.loadChart(url);
    }

    dashboardChartFlot.prototype.loadChart = function(url){
        var self = this;

        $.getJSON(url, function(response){
            var rows_flot = [];
            var color_default = '#5c5';
            var row_line = {
              data: response.values,
              animator: {steps: 60, duration: 1000, start:0}, 		
              lines: {lineWidth:2, fill:0.6},	
              shadowSize: 0,
              color: self.opts.color || color_default,
              yaxis: 1
            };
            var row_point = {
              data: response.values,
              points: { show: true, fill: true, radius: 6, fillColor: self.opts.color || color_default, lineWidth:3 },
              color: "#fff",
              shadowSize: 0,
            };

            rows_flot.push(row_line)
            rows_flot.push(row_point);

            self.origins = response.origins;
            self.values_labels = response.values_labels;
            self.plotChart(rows_flot, url);
        });
    }

    dashboardChartFlot.prototype.plotChart = function(rows, url){
        var self = this;
        var html = this.html;
        var $newElement = $(html);
        Highcharts.data({
        csv: document.getElementById('tsv').innerHTML,
        itemDelimiter: '\t',
        parsed: function (columns) {

            var brands = {},
                brandsData = [],
                versions = {},
                drilldownSeries = [];
            
            // Parse percentage strings
            columns[1] = $.map(columns[1], function (value) {
                if (value.indexOf('%') === value.length - 1) {
                    value = parseFloat(value);
                }
                return value;
            });

            $.each(columns[0], function (i, name) {
                var brand,
                    version;

                if (i > 0) {

                    // Remove special edition notes
                    name = name.split(' -')[0];

                    // Split into brand and version
                    version = name.match(/([0-9]+[\.0-9x]*)/);
                    if (version) {
                        version = version[0];
                    }
                    brand = name.replace(version, '');

                    // Create the main data
                    if (!brands[brand]) {
                        brands[brand] = columns[1][i];
                    } else {
                        brands[brand] += columns[1][i];
                    }

                    // Create the version data
                    if (version !== null) {
                        if (!versions[brand]) {
                            versions[brand] = [];
                        }
                        versions[brand].push(['v' + version, columns[1][i]]);
                    }
                }
                
            });

            $.each(brands, function (name, y) {
                brandsData.push({ 
                    name: name, 
                    y: y,
                    drilldown: versions[name] ? name : null
                });
            });
            $.each(versions, function (key, value) {
                drilldownSeries.push({
                    name: key,
                    id: key,
                    data: value
                });
            });

            // Create the chart
            $('#container').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Browser market shares. November, 2013'
                },
                subtitle: {
                    text: 'Click the columns to view versions. Source: netmarketshare.com.'
                },
                xAxis: {
                    type: 'category'
                },
                yAxis: {
                    title: {
                        text: 'Total percent market share'
                    }
                },
                legend: {
                    enabled: false
                },
                plotOptions: {
                    series: {
                        borderWidth: 0,
                        dataLabels: {
                            enabled: true,
                            format: '{point.y:.1f}%'
                        }
                    }
                },

                tooltip: {
                    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
                    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
                }, 

                series: [{
                    name: 'Brands',
                    colorByPoint: true,
                    data: brandsData
                }],
                drilldown: {
                    series: drilldownSeries
                }
            })

        }
    });



        $.plotAnimator($newElement.find(".placeholder"), 
            rows,
            {	
              xaxis: {
                ticks: self.origins,
                tickFormatter: 'string',
                font :{
                    lineHeight: 13,
                    style: "normal",
                    weight: "bold",
                    family: "sans-serif",
                    variant: "small-caps",
                    color: "#6F7B8A",
                }
              },
              yaxis: {
                ticks: self.values_labels,
                tickFormatter: 'string',
                labelWidth: 100,
                  font :{
                      style: "normal",
                      weight: "bold",
                      family: "sans-serif",
                      variant: "small-caps",
                      color: "#6F7B8A",
                  }
              },
              grid: {
                  backgroundColor: { colors: [ "#fff", "#fff" ] },
                  borderWidth:1,
                  borderColor:"#f0f0f0",
                  margin:0,
                  minBorderMargin:0,							
                  labelMargin:20,
                  hoverable: true,
                  clickable: true,
                  mouseActiveRadius:6
              }
            }
        );


        if(this.$element){
            this.$element.replaceWith($newElement);
        } else {
            this.$wrapper.append($newElement);
        }
        this.$element = $newElement;

        this.$element.find(".reload").click(function(){
            self.loadChart(url);
        });
        this.$element.find(".remove").click(function(){
            self.$element.remove();
        });
    }

    $.fn.dashboardChartFlot = function(urls, opts) {
        new dashboardChartFlot( this, urls, opts );
        return this;
    };
 
}( jQuery ));
