(function ( $ ) {
    var dashboardMap = function(wrapper, countries){
        var self = this;
        this.map;
        this.greenMarkerIcon = '/static/img/green_waypoint.png';
        this.yellowMarkerIcon = '/static/img/yellow_waypoint.png';
        this.redMarkerIcon = '/static/img/red_waypoint.png';
        this.wrapper = wrapper;
        this.countries = countries;

        google.maps.event.addDomListener(window, 'load', function(){
            self.drawMap();
        });
    }
    
    dashboardMap.prototype.drawMap = function(){
        var self = this,
            latLngCenter = new google.maps.LatLng(15.961329,-90.981447), //Guatemala
            mapOptions = {
                zoom: 4,
                center: latLngCenter
            };

        this.map = new google.maps.Map(this.wrapper[0], mapOptions);
        this.getCountriesMarkers(function(countries){
            $.each(countries, function(i, country){
                google.maps.event.addListener(country.marker,'click', (function(marker) {
                  return function(){ country.infoBox.open(self.map, this); }
                })(country.marker));
            });
        });
    }

    dashboardMap.prototype.getCountriesMarkers = function(callback){
        var self = this, countries = [];
        $.each(this.countries, function(i, country){
            var icon = '';
            if(country.pin_color == 'green'){
                icon = self.greenMarkerIcon;
            } else if(country.pin_color == 'yellow'){
                icon = self.yellowMarkerIcon;
            } else if(country.pin_color == 'red'){
                icon = self.redMarkerIcon;
            }

            var latLng = new google.maps.LatLng(country.lat, country.lng),
                marker = new google.maps.Marker({
                    position: latLng,
                    map: self.map,
                    icon: icon,
                    visible: true
                });

            var infoBox = self._getInfoBox(country);
            countries.push({
                marker: marker,
                infoBox: infoBox
            });
        });
        callback(countries);
    }

    dashboardMap.prototype._getInfoBox = function(country){
    
        var InfoBoxHTML = ''+
          '<div class="content-info-window">'+
              '<div class="arrow-container"></div>'+
              '<div class="left-side">'+
                  '<div class="main-info">'+
                      '<h4 class="title-info">{TITLE}</h4>'+
                      '<p class="desc">{SHORT_DESCRIPTION}</p>'+
                  '</div>'+
                  '<a class="more-info" href="#">Más infos</a>'+
              '</div>'+
              '<div class="right-side">'+
                  '<div class="statistics">'+
                      '<span class="label-stats">Objetivos</span>'+
                  '</div>'+
              '</div>'+
          '</div>';

        var infoBoxDefault = document.createElement("div");
          infoBoxDefault.className = 'content-info-window'
          infoBoxDefault.innerHTML = InfoBoxHTML;

        var infoBoxOptions = {
            disableAutoPan: true
            ,maxWidth: 0
            ,pixelOffset: new google.maps.Size(0, -140)
            ,zIndex: null
            ,boxStyle: {
              width: '522px'
            }
            ,closeBoxMargin: "10px 40px 0px 0px"
            ,closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif"
            ,infoBoxClearance: new google.maps.Size(1, 1)
            ,isHidden: true
            ,pane: "floatPane"
            ,visible: true
        };

        var infoBoxOptions = infoBoxOptions;
        infoBoxOptions.content = infoBoxDefault.innerHTML
                                                .replace("{TITLE}", country.name)
                                                .replace("{SHORT_DESCRIPTION}", country.short_description);
        return new InfoBox(infoBoxOptions);
    }

    $.fn.dashboardMap = function(countries) {
        new dashboardMap( this, countries );
        return this;
    };
 
}( jQuery ));