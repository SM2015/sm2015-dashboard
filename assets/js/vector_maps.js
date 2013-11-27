$(document).ready(function() {		

var tooltipHTML = ''+
  '<div class="content-info-window">'+
      '<div class="left-side">'+
          '<div class="main-info">'+
              '<h4 class="title-info">{TITLE}</h4>'+
              '<p class="desc">Meta: melhorar o acesso.</p>'+
          '</div>'+
          '<a class="more-info" href="#">Más infos</a>'+
      '</div>'+
      '<div class="right-side">'+
          '<div class="statistics">'+
              '<span class="label-stats">Objetivos</span>'+
          '</div>'+
      '</div>'+
  '</div>';

$('#world-map').vectorMap({
   map: 'world_mill_en',
    scaleColors: ['#C8EEFF', '#0071A4'],
    normalizeFunction: 'polynomial',
    focusOn:{
          x: 0.2,
		  y: 0.5,
		  scale: 4
	},
	zoomMin:0.85,
    hoverColor: false,
	regionStyle:{
		  initial: {
			fill: '#babdc0',
			"fill-opacity": 1,
			stroke: '#babdc0',
			"stroke-width": 0,
			"stroke-opacity": 0
		  },
		  hover: {
			"fill-opacity": 0.8
		  },
		  selected: {
			fill: 'yellow'
		  },
		  selectedHover: {
		  }
		},
    markerStyle: {
		  initial: {
			fill: '#f35958',
			stroke: '#f35958',
			"fill-opacity": 1,
			"stroke-width": 4,
			"stroke-opacity": 0.2,
			r: 5
		  },
		  hover: {
			stroke: 'black',
			"stroke-width": 2
		  },
		  selected: {
			fill: 'blue'
		  },
		  selectedHover: {
		  }
		},
    onMarkerLabelShow: function(e, label, code) {

        console.log(code);
        switch(code){
            case '0':
                tooltipHTML = tooltipHTML.replace("{TITLE}", "Guatemala");
                console.log(tooltipHTML);
                label.html(tooltipHTML);
                break;
            case '1':
                tooltipHTML = tooltipHTML.replace("{TITLE}", "Belize");
                label.html(tooltipHTML);
                console.log(tooltipHTML);
                break;
        }
    },
    backgroundColor: '#e5e9ec',
    markers: [
      {latLng: [16.78, -90.23], name: 'Guatemala'},
      {latLng: [17.25, -88.75], name: 'Belize'},
    ]
  });
	  
});
