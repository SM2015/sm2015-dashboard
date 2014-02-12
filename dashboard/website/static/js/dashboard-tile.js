(function ( $ ) {
    var dashboardTile = function(wrapper, origin){
        this.$wrapper = $(wrapper);
        this.$html;
        this.origin = origin;

        this.loadTile();
    }
    
    dashboardTile.prototype.loadTile = function(){
        var self = this;

        $.getJSON(this.origin.url_ongoing, function(response){
            var color, html = ''+
                '<div class="span3">'+
                    '<div class="tiles {TILE_COLOR} added-margin">'+
                      '<div class="tiles-body">'+
                        '<div class="controller">'+
                            '<a href="javascript:;" class="reload"></a>'+
                            '<a href="javascript:;" class="remove"></a>	'+
                        '</div>		'+
                        '<div class="tiles-title">'+
                            '<strong>{TILE_ORIGIN}</strong> TOTAL'+
                        '</div>	'+
                        '<div class="heading">'+
                        '<span class="animate-number" data-value="{TILE_VALUE}" data-animation-duration="1200">0</span>'+
                        '</div>'+
                        '<div class="progress transparent progress-white progress-small no-radius">'+
                            '<div class="bar animate-progress-bar" data-percentage="{TILE_PERCENTAGE}%"></div>'+
                        '</div>'+
                        '<div class="description"><i class="icon-custom-up"></i><span class="text-white mini-description ">&nbsp; {TILE_DV}% <span class="blend">variance from expected</span></span></div>'+
                        '</div>	'+
                    '</div>'+
                '</div>';

            if(response.dpi <= 0.8){ 
                color = 'red';
            } else if(response.dpi <= 0.99){ 
                color = 'yellow';
            } else { 
                color = 'green';
            }

            html = html.replace("{TILE_COLOR}", color)
                    .replace("{TILE_ORIGIN}", self.origin.name)
                    .replace("{TILE_VALUE}", response.accumulated)
                    .replace("{TILE_PERCENTAGE}", response.percentage)
                    .replace("{TILE_DV}", response.dv);

            var $html = $(html);

            if(!self.$html) {
                self.$wrapper.append($html);
            } else {
                self.$html.replaceWith($html);
            }

            self.$html = $html;

            $html.find(".reload").click(function(){ self.loadTile(); });
            $html.find(".remove").click(function(){ $html.remove(); });

            var $animated_number = $html.find('.animate-number');
            var $animated_progress_bar = $html.find('.animate-progress-bar');

            $animated_number.animateNumbers($animated_number.attr("data-value"), true, parseInt($animated_number.attr("data-animation-duration")));
            $animated_progress_bar.css('width', $animated_progress_bar.attr("data-percentage"));
        });
    }

    $.fn.dashboardTile = function(origin) {
        new dashboardTile( this, origin );
        return this;
    };
 
}( jQuery ));