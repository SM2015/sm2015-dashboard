(function( $ ){
    function loadGraphs($wrapper, url, opts){
        $container_graphs = $wrapper.find(".graph-triangle-container");
        $container_graphs.find("*").remove();

        if(opts && opts.title){
          title = opts.title;
        } else {
          title = '[[COUNTRY]] Primera Operación SM2015';
        }

        $.getJSON(url, function(data){
            $.each(data, function(i){
                var div_triangle_id = 'graph-triangle-' + this.country_slug;
                createDivTriangle(div_triangle_id, $container_graphs,i, opts);
                drawSpider('#'+div_triangle_id, this.country, this.triangle_categories, this.series, title);
            });
        });
    }

    function createDivTriangle(id_div, $container, position, opts){
        var class_first = '';
        if(parseInt(position) == 0 || (parseInt(position)) % 3 == 0){
            class_first = 'first-column';
        }
       
        if(opts.alone){
          var html_div = '<div id="'+id_div+'" style="height: 400px; margin: 0 auto"></div>';
        } else {
          var html_div = ''+
              '<div class="span4 '+class_first+'">'+
                '<div id="'+id_div+'" style="height: 400px; margin: 0 auto"></div>'+
              '</div>';
        }

        $container.append(html_div);
    }

    function drawSpider(div, country, categoriesArray, seriesArray, title) {
        title = title.replace("[[COUNTRY]]", country);

        Highcharts.theme = {
            colors: ['#058DC7', '#FF9655', '#DD9999', '#6AF9C4', '#64E572', '#0d233a', '#bbbbbb', '#F9CCCA', '#F9CCCA'],
            title: {
                style: {
                    color: '#000',
                    font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
                }
            },
            subtitle: {
                style: {
                    color: '#666666',
                    font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
                }
            },
            xAxis: {
                gridLineWidth: 1,
                lineColor: '#000',
                tickColor: '#000',
                labels: {
                    style: {
                        color: '#000',
                        font: '10px Trebuchet MS, Verdana, sans-serif'
                    }
                },
                title: {
                    style: {
                        color: '#333',
                        fontWeight: 'bold',
                        fontSize: '12px',
                        fontFamily: 'Trebuchet MS, Verdana, sans-serif'

                    }
                }
            },
            legend: {
                itemStyle: {
                    font: '9pt Trebuchet MS, Verdana, sans-serif',
                    color: 'black'

                },
                itemHoverStyle: {
                    color: '#039'
                },
                itemHiddenStyle: {
                    color: 'gray'
                }
            },
            labels: {
                style: {
                    color: '#99b'
                }
            },

            navigation: {
                buttonOptions: {
                    theme: {
                        stroke: '#CCCCCC'
                    }
                }
            }
        };

        // Apply the theme
        var highchartsOptions = Highcharts.setOptions(Highcharts.theme);
        $(div).highcharts({
            chart: {
                polar: true,
                type: 'line',
            },
            title: {
                text: title
            },
            xAxis: {
                categories: categoriesArray,
                tickmarkPlacement: 'on',
                offset: 20,
                lineWidth: 0,
            },
            yAxis: {
                gridLineInterpolation: 'polygon',
                lineWidth: 0,
            },
            tooltip: {
                shared: true,
                pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y}%</b><br/>'
            },
            exporting: {
                enabled: true
            },
            credits: {
                enabled: false
            },
            series: seriesArray
        });
    }

    $.fn.graficoTrianguloPorPais = function(url_dados_grafico, opts) {
        var wrapper = this;
        loadGraphs( this, url_dados_grafico, opts);

        $(this).find(".reload").click(function(){
            loadGraphs( wrapper, url_dados_grafico, opts);
        });
        return this;
    };
}( jQuery ));
