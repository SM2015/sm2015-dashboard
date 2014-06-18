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
                '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
              '</div>'+
              '<div class="grid-body no-border">'+
                '<div class="placeholder" style="width:960px;height:250px;position:relative; padding-top:10px;"></div>'+
              '</div>'+
            '</div>';

        this.loadChart(url);
    }

    dashboardChartBar.prototype.loadChart = function(url){
        var self = this;

        $.getJSON(url, function(response){
          var rows_flot = [];
          var colors = [
            "rgba(243, 89, 88, 0.7)",
            "rgba(251, 176, 94, 0.7)"
          ];
          $.each(response.values, function(i){
            console.log(this);
            var row = {
              data: this,
              animator: {steps: 60, duration: 1000, start:0}, 		
              shadowSize: 0,
              bars: { 
                show: true,
                barWidth: 0.2,
                fill: true,
                lineWidth: 0,
                order: i+1,
                fillColor:  colors[i]
              },
              color:  colors[i]
            };
            rows_flot.push(row);
          });

          self.origins = response.origins;
          self.values_labels = response.values_labels;
          self.plotChart(rows_flot, url);
        });
    }

    dashboardChartBar.prototype.plotChart = function(rows, url){
        var self = this;
        var html = this.html;
        var $newElement = $(html);

        $.plot($newElement.find(".placeholder"), 
            rows,
            {	
              series: {
                bars: {
                  show: true,
                  barWidth: 0.5,
                }
              },
              xaxis: {
                ticks: self.origins,
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
                labelWidth: 50,
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
              },
            }
        );
      
        $newElement.bind("plothover", function (event, pos, item) {
          if (item) {
            var origin = self.origins[item.dataIndex][1],
                value = thousandSeparator(item.datapoint[1] * 1000000),
                label;
      
            if (item.seriesIndex == 0){
              label = origin + " (Real): " + value;
            } else if (item.seriesIndex == 1){
              label = origin + " (Expected): " + value;
            }
            $("#tooltip").html(label)
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

    $.fn.dashboardChartBar = function(urls, opts) {
        new dashboardChartBar( this, urls, opts );
        return this;
    };
 
}( jQuery ));
