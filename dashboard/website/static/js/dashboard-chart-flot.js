(function ( $ ) {
    var dashboardChartFlot = function(wrapper, url, opts){
        this.$wrapper = $(wrapper);
        this.url = url;
        this.opts = opts;
        this.$element;
        this.html = ''+
            '<div class="span6">'+
              '<div class="grid simple">'+
                '<div class="grid-title no-border">'+
                  '<h4>{NAME} <span class="semi-bold"></span></h4>'+
                  '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
                '</div>'+
                '<div class="grid-body no-border">'+
                  '<div class="row-fluid">'+
                    '<div class="placeholder" style="width:460px;height:250px;"></div>'+
                    '<div class="row-fluid">'+
                      '<div class="span6">'+
                        '<div class="mini-chart-wrapper">'+
                          '<div class="chart-details-wrapper">'+
                            '<div class="chartname"> Total </div>'+
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

        this.loadChart();
    }
    
    dashboardChartFlot.prototype.loadChart = function(){
        var self = this;
        $.getJSON(this.url, function(response){
            var rows_flot = [];
            var totals = [];
            $.each(response, function(i, origin_data){
                var row = {
                    data: origin_data,
                    animator: {steps: 60, duration: 1000, start:0}, 		
                    lines: {lineWidth:2},	
                    shadowSize:0,
                    color: '#f35958'
                };
                rows_flot.push(row);

                $.each(origin_data, function(i2, data_per_period){
                    if(!totals[i2]){
                        totals[i2] = 0;
                    }
                    totals[i2]+=data_per_period[1];
                });
            });
            self.plotChart(rows_flot);
            self.plotMiniChart(totals);
        });
    }

    dashboardChartFlot.prototype.plotChart = function(rows){
        var self = this;
        var html = this.html;
        if(this.opts.name){
            html = html.replace("{NAME}", this.opts.name);
        }

        var $newElement = $(html);

        $.plotAnimator($newElement.find(".placeholder"), 
            rows,
            {	
                xaxis: {
                    tickDecimals: 0,
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        weight: "bold",
                        family: "sans-serif",
                        variant: "small-caps",
                        color: "#6F7B8A"
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
                },
                legend: { show: false}
            }
        );
        if(this.$element){
            this.$element.replaceWith($newElement);
        } else {
            this.$wrapper.append($newElement);
        }
        this.$element = $newElement;

        this.$element.find(".reload").click(function(){
            self.loadChart();
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
        this.$element.find(".chart-details-wrapper").find(".chart-value").text(total);
    }

    $.fn.dashboardChartFlot = function(url, opts) {
        new dashboardChartFlot( this, url, opts );
        return this;
    };
 
}( jQuery ));
