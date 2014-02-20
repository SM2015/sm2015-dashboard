(function ( $ ) {
    var dashboardChartFlot = function(wrapper, urls){
        this.$wrapper = $(wrapper);
        this.urls = urls;
        this.$element;
        this.html = ''+
            '<div class="span12">'+
              '<div class="grid simple">'+
                '<div class="grid-title no-border">'+
                  '<h4></h4>'+
                  '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
                '</div>'+
                '<div class="grid-body no-border">'+
                  '<div class="row-fluid">'+
                    '<div><select class="select-options">{OPTIONS}</select></div>'+
                    '<div class="placeholder" style="width:1015px;height:250px;position:relative"></div>'+
                    '<div class="row-fluid">'+
                      '<div class="span12">'+
                        '<div class="mini-chart-wrapper">'+
                          '<div class="chart-details-wrapper">'+
                            '<div class="chartname"> </div>'+
                            '<div class="chart-value"></div>'+
                          '</div>'+
                          '<div class="mini-chart">'+
                            '<div class="mini-chart-graph"></div>'+
                          '</div>'+
                        '</div>'+
                      '</div>'+
                    '</div>'+
                  '</div>'+
                '</div>'+
              '</div>'+
            '</div>';

        var options = [],
            first_url;
        $.each(urls, function(i){
          if(i == 0){
            first_url = this.url;
          }
          options.push('<option value="'+this.url+'">'+this.name+'</option>');
        });
        this.html = this.html.replace("{OPTIONS}", options.join());
        this.loadChart(first_url);
    }

    dashboardChartFlot.prototype.bindElements = function($elem){
      var self = this;
      $elem.find('.select-options').change(function(){
        self.loadChart(this.value);
      });
    }
    
    dashboardChartFlot.prototype.loadChart = function(url){
        var self = this;

        $.getJSON(url, function(response){
            var rows_flot = [];
            var totals = [];
            var count = 0;
            var colors = {
              'expected': '#ddd',
              'real': '#5c5'
            }

            var row_line_expected = {
              data: response.expected,
              animator: {steps: 60, duration: 1000, start:0}, 		
              lines: {lineWidth:2},	
              shadowSize: 0,
              color: colors.expected,
            };
            var row_line_real = {
              data: response.real,
              animator: {steps: 60, duration: 1000, start:0}, 		
              lines: {lineWidth:2, fill:0.6},	
              shadowSize: 0,
              color: colors.real,
            };
            var row_point_expected = {
              data: response.expected,
              points: { show: true, fill: true, radius: 6, fillColor: colors.expected, lineWidth:3 },
              color: "#fff",
              shadowSize: 0,
            };
            var row_point_real = {
              data: response.real,
              points: { show: true, fill: true, radius: 6, fillColor: colors.real, lineWidth:3 },
              color: "#fff",
              shadowSize: 0,
            };

            rows_flot.push(row_line_expected)
            rows_flot.push(row_line_real);
            rows_flot.push(row_point_expected)
            rows_flot.push(row_point_real);

            self.plotChart(rows_flot, url, response.periods);
            self.plotMiniChart(totals);
        });
    }

    dashboardChartFlot.prototype.plotChart = function(rows, url, periods){
        var self = this;
        var html = this.html;
        var $newElement = $(html);
        $newElement.find("option[value='"+url+"']").attr("selected", true);
        this.bindElements($newElement);
        $.plotAnimator($newElement.find(".placeholder"), 
            rows,
            {	
                xaxis: {
                  labelWidth: 100,
                    ticks: periods,
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
                    ticks: 3,
                    tickDecimals: 0,
                    tickColor: "#f0f0f0",
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        weight: "bold",
                        family: "sans-serif",
                        variant: "small-caps",
                        color: "#6F7B8A"
                    }
                },
                grid: {
                    backgroundColor: { colors: [ "#fff", "#fff" ] },
                    borderWidth:1,borderColor:"#f0f0f0",
                    margin:0,
                    minBorderMargin:0,							
                    labelMargin:20,
                    hoverable: true,
                    clickable: true,
                    mouseActiveRadius:6
                }
            }
        );
      
        $newElement.bind("plothover", function (event, pos, item) {
          if (item) {
            var period = String(item.datapoint[0]).replace(".", "Q"),
                value = item.datapoint[1] * 1000000;
      
            $("#tooltip").html(period + ": " + value)
                          .css({ top: item.pageY+5, left: item.pageX+5 })
                          .fadeIn(200);
          } else {
            $("#tooltip").hide();
          }
        });

        $("<div id='tooltip'></div>").css({
            position: "absolute",
            display: "none",
            border: "1px solid #fdd",
            padding: "2px",
            "background-color": "#fee",
            "z-index":"99999",
            opacity: 0.80
        }).appendTo("body");


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

    dashboardChartFlot.prototype.plotMiniChart = function(totals){
        this.$element.find(".mini-chart-graph").sparkline(totals, {
            type: 'bar',
            height: '30px',
            barWidth: 6,
            barSpacing: 2,
            barColor: '#f35958',
            negBarColor: '#f35958'
        });

        var total = 0;
        $.each(totals, function(){
            total+=this;
        });
        //this.$element.find(".chart-details-wrapper").find(".chart-value").text(total);
    }

    $.fn.dashboardChartFlot = function(urls) {
        new dashboardChartFlot( this, urls );
        return this;
    };
 
}( jQuery ));
