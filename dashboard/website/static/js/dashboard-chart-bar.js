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
                '<div class="placeholder" style="width:450px;height:250px;position:relative; padding-top:10px;"></div>'+
              '</div>'+
            '</div>';

        this.loadChart(url);
    }

    dashboardChartBar.prototype.loadChart = function(url){
        var self = this;

        $.getJSON(url, function(response){
            self.plotChart(response.columns, url);
        });
    }

    dashboardChartBar.prototype.plotChart = function(columns, url){
        var self = this;
        var html = this.html;
        var $newElement = $(html);


        $newElement.find('.placeholder').highcharts({
            chart: {
                type: 'column',
            },
            title: '',
            xAxis: {
                type: 'category',
                title: {
                    text: 'Donnors'
                }
            },
            yAxis: {
                title: {
                    text: 'Accumulative'
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
                        format: '${point.label}'
                    }
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
                pointFormat: '<span style="color:{point.color}">{point.name}</span><br/>'
            }, 
            series: [{
                name: 'Donnors',
                colorByPoint: true,
                data: columns
            }]
        });

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

    $.fn.dashboardChartBar = function(urls, opts) {
        new dashboardChartBar( this, urls, opts );
        return this;
    };
 
}( jQuery ));
