$(document).ready(function() {		
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
    backgroundColor: '#e5e9ec',
    markers: [
      {latLng: [13.78, -90.23], name: 'Guatemala'},
      {latLng: [16.78, -90.23], name: 'Guatemala'},
    ]
  });
	  
});
