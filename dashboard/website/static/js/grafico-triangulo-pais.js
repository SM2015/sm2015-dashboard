(function( $ ){
    function loadGraphs($wrapper, url){
        $wrapper.remove();
        $.getJSON(url, function(data){
            $.each(data, function(){
                var div_triangle_id = 'graph-triangle-' + this.country_slug;
                createDivTriangle(div_triangle_id, $wrapper);
                drawSpider('#'+div_triangle_id, this.country, this.triangle_categories, this.series);
            });
        });
    }

    function createDivTriangle(id_div, $wrapper){
        var html_div = ''+
            '<div class="span4">'+
              '<div id="'+id_div+'" style="min-width: 230px; height: 400px; margin: 0 auto"></div>'+
            '</div>';
        $wrapper.append(html_div);
    }

    function drawSpider(div, country, categoriesArray, seriesArray) {
        Highcharts.theme = {
            colors: ['#058DC7', '#0d233a', '#bbbbbb', '#F9CCCA', '#F9CCCA', '#64E572', '#FF9655', '#FFF263', '#6AF9C4'],
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
                        font: '11px Trebuchet MS, Verdana, sans-serif'
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
                marginLeft: 10,
                marginRight: 10,
            },
            title: {
                text: country + ' Primera Operación SM2015'
            },
            pane: {
                size: '85%'
            },
            xAxis: {
                categories: categoriesArray,
                tickmarkPlacement: 'on',
                lineWidth: 0,
                labels: {
                    style: {
                        width: '30px'
                    }
                }
            },
            yAxis: {
                gridLineInterpolation: 'polygon',
                lineWidth: 0,
                min: 0,
                width: 30
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

    $.fn.graficoTrianguloPorPais = function(url_dados_grafico) {
        loadGraphs( this, url_dados_grafico );
        return this;
    };
}( jQuery ));
