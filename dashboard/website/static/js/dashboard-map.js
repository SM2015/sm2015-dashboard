(function ( $ ) {
    var dashboardMap = function(wrapper, countries, opts){
        var self = this;
        this.map;
        this.greenMarkerIcon = '/static/img/green_waypoint.png';
        this.yellowMarkerIcon = '/static/img/yellow_waypoint.png';
        this.redMarkerIcon = '/static/img/red_waypoint.png';
        this.wrapper = wrapper;
        this.countries = countries;
        this.opts = opts || {};

        this._bindEvents();

        google.maps.event.addDomListener(window, 'load', function(){
            self.drawMap();
        });
    }
    
    dashboardMap.prototype._bindEvents = function(slug){
    }

    dashboardMap.prototype._getCountryBySlug = function(slug){
      for(var i=0; i < this.countries.length; i++){
        var country = this.countries[i];
        if(country.slug == slug){
          return country;
        }
      }
    }

    dashboardMap.prototype.drawPanel = function(){
      var country = this.panelCountry,
        html = ''+
          '<div class="menu-country">'+
            '<div class="map-overlay"></div>'+
            '<div class="map-infos-wrapper">'+
              '<i class="icon icon-down"></i>'+
              '<div class="columns">'+
                '<h6 class="title">Country: <strong>'+country.name+'</strong></h6>'+
                '<label class="subtitle">Operation Number: <span>'+country.operation.number+'</span></label>'+
                '<label class="subtitle">Name: <span>'+country.operation.name+'</span></label>'+
                '<label class="subtitle">Executing Agency: <span>'+country.operation.executing_agency+'</span></label>'+
                '<label class="subtitle">Eligibility Date: <span>'+country.operation.starting_date+'</span></label>'+
              '</div>'+
              '<div class="columns">'+
                '<h6 class="title">Focalized Zones</h6>'+
                '<label class="subtitle"><span>{ZONES}</span></label>'+
              '</div>'+
              '<div class="columns">'+
                '<h6 class="title">Benefitted Population</h6>'+
                '<label class="subtitle"><span>'+country.operation.benefitted_population+'</span></label>'+
              '</div>'+
            '</div>'+
          '</div>';

      zone_names = []
      for(var i=0; i < country.operation.zones.length; i++){
        var zone = country.operation.zones[i];
        zone_names.push(zone.name);
      }

      html = html.replace('{ZONES}', zone_names.join(', '));
      this.wrapper.after(html);
    }

    dashboardMap.prototype.drawMap = function(){
        var self = this,
            latLngCenter, zoomMap;

        if(this.opts.countryZoom){
          var countryZoom = this._getCountryBySlug(this.opts.countryZoom);
          if(countryZoom){
            if(countryZoom.slug == 'el-salvador'){
              latLngCenter = new google.maps.LatLng(13.502971, -88.814850);
              zoomMap = 9;
            } else {
              latLngCenter = new google.maps.LatLng(countryZoom.lat, countryZoom.lng);
              zoomMap = 8;
            }
          }
        }

        if(!latLngCenter){
          latLngCenter = new google.maps.LatLng(15.961329,-90.981447); //Guatemala
          zoomMap = 5;
        }
        
        mapOptions = {
          zoom: zoomMap,
          center: latLngCenter
        };


        this.map = new google.maps.Map(this.wrapper[0], mapOptions);

        if(self.opts.panel){
          for(var i=0; i < self.countries.length; i++){
            var country = self.countries[i];
            if(country.slug == this.opts.panel){
              self.panelCountry = country;
              self.drawPanel();
              this.getOperationZoneMarkers();
              break;
            }
          }
        } else {
          this.getCountriesMarkers(function(countries){
              $.each(countries, function(i, country){
                  google.maps.event.addListener(country.marker,'click', (function(marker) {
                    return function(){ 
                      $.each(countries, function(i, country_to_close){
                        if(country != country_to_close){
                          country_to_close.infoBox.close();
                        }
                      });

                      country.infoBox.open(self.map, this);
                      self.map.setOptions( {scrollwheel:false} ); 
                      self.map.setCenter(country.marker.position);

                      setTimeout(function(){
                        $('.easy-pie-custom').easyPieChart({
                          lineWidth:11,
                          barColor:'#447744',
                          trackColor:'#e5e9ec',
                          scaleColor:false
                        });
                      }, 500);
                    }
                  })(country.marker));
              });
          });
        }
    }

    dashboardMap.prototype.getOperationZoneMarkers = function(){
        var self = this, countries = [];
        $.each(this.panelCountry.operation.zones, function(i, zone){
            var icon = self.greenMarkerIcon;

            var latLng = new google.maps.LatLng(zone.lat, zone.lng),
                marker = new google.maps.Marker({
                    position: latLng,
                    map: self.map,
                    icon: icon,
                    visible: true
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

            google.maps.event.addListener(infoBox,'closeclick',function(){
              self.map.setOptions({ scrollwheel:true }); 
            });
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
                  '<a class="more-info" href="{INFOS_URL}">Más infos</a>'+
              '</div>'+
              '<div class="right-side">'+
                  '<div class="statistics">'+
                      '<span class="label-stats">Tiempo</span>'+
                      '<div class="goal">'+
                        '<div class="easy-pie-custom" data-percent="{GOAL}"><span class="easy-pie-percent">{GOAL}%</span></div>'+
                      '</div>'+
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
                                                .replace("{SHORT_DESCRIPTION}", country.short_description)
                                                .replace("{INFOS_URL}", country.infos_url)
                                                .replace("{GOAL}", country.goal)
                                                .replace("{GOAL}", country.goal);


        return new InfoBox(infoBoxOptions);
    }

    $.fn.dashboardMap = function(countries, opts) {
        new dashboardMap( this, countries, opts );
        return this;
    };
 
}( jQuery ));
