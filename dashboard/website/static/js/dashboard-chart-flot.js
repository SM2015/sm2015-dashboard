(function ( $ ) {
    var dashboardChartFlot = function(wrapper, url, opts){
        this.$wrapper = $(wrapper);
        this.url = url;
        this.$element;
        this.opts = opts || {};
        title = opts.title || ''
        this.html = ''+
            '<div class="grid simple">'+
              '<div class="grid-title">'+
                '<h4>' + title + '</h4>'+
                '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
              '</div>'+
              '<div class="grid-body">'+
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
      
        $newElement.bind("plothover", function (event, pos, item) {
          if (item) {
            var origin = self.origins[item.dataIndex][1],
                value = item.datapoint[0] * 1000000;
      
            $("#tooltip").html(origin + ": " + value)
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

    $.fn.dashboardChartFlot = function(urls, opts) {
        new dashboardChartFlot( this, urls, opts );
        return this;
    };
 
}( jQuery ));
