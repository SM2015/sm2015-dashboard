options = {chart: {polar: true,type: "line",marginLeft: 10,marginRight: 10},title: {"text": "Belize SM2015"},pane: {size: "85%"},xAxis: {categories: ["% Time Progress", "Financial Execution", "Physics Execution"],tickmarkPlacement: "on",lineWidth: 0,labels: {style: {width: "30px"}}},yAxis: {gridLineInterpolation: "polygon",lineWidth: 0,min: 0,width: 30},tooltip: {shared: true,pointFormat: "<span style='color:{series.color}'>{series.name}: <b>{point.y}% </b><br/>"},exporting: {enabled: true},credits: {enabled: false},series: [{"data": [100.0, 70.0, 50.0], "name": "Ejecucion Actual (%)", "pointPlacement": "on"}, {"data": [100.0, 2.0, 30.0], "name": "Ejecucion Programada (%)", "pointPlacement": "on"}, {"data": [100.0, 3.0, 5.0], "name": "Ejecucion Original Programada (%)", "pointPlacement": "on"}]}