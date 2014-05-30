(function ( $ ) {
    var dashboardTable = function( wrapper, url, opts, callback ) {
        this.$wrapper = wrapper;
        this.url = url;
        this.opts = opts;
        this.callback_user = callback;

        this.drawTable();
    };

    dashboardTable.prototype.bindElements = function(){
        var self = this,
            $textfields = this.$wrapper.find(".editable.text"),
            $textareafields = this.$wrapper.find(".editable.textarea"),
            $selectfields = this.$wrapper.find(".editable.select"),
            $datefields = this.$wrapper.find(".editable.date");

        $datefields.editable(self.opts.url_save, {
            type: 'datepicker',
            submitdata : function(value, settings) { 
                var field = $(this).attr("name");
                var data = {};
                data['objid'] = $(this).closest("[data-objid]").attr("data-objid");
                data['model'] = $(this).closest("[data-model]").attr("data-model");
                data[field] = $(this).find("input").val();
                return data;
            }
        });

        $textfields.editable(self.opts.url_save, {
            height: 27,
            submitdata : function(value, settings) { 
                var field = $(this).attr("name");
                var data = {};
                data['objid'] = $(this).closest("[data-objid]").attr("data-objid");
                data['model'] = $(this).closest("[data-model]").attr("data-model");
                data[field] = $(this).find("input").val();
                return data;
            }
        });

        $textareafields.editable(self.opts.url_save, {
            type: 'textarea',
            cancel: 'Cancel',
            submit: 'OK',
            submitdata : function(value, settings) { 
                var field = $(this).attr("name");
                var data = {};
                data['objid'] = $(this).closest("[data-objid]").attr("data-objid");
                data['model'] = $(this).closest("[data-model]").attr("data-model");
                data[field] = $(this).find("textarea").val();
                return data;
            }
        });

        $selectfields.each(function(){
            var data = $(this).attr("data-options");

            $(this).editable(self.opts.url_save, { 
                type      : 'select',
                cancel    : 'Cancel',
                submit    : 'OK',
                data      : data,
                submitdata : function(value, settings) { 
                    var field = $(this).attr("name");
                    var data = {};
                    data['objid'] = $(this).closest("[data-objid]").attr("data-objid");
                    data['model'] = $(this).closest("[data-model]").attr("data-model");
                    data[field] = $(this).find("select :selected").val();
                    return data;
                }
            });
        });
    };

    dashboardTable.prototype.bindDataTable = function(){
        if(!this.opts.vertical){
            var responsiveHelper = undefined;
            var breakpointDefinition = {
                tablet: 1024,
                phone : 480
            };
            var tableElement = this.$wrapper.find("table");
            var options = {
                "sPaginationType": "bootstrap",
                 "aoColumnDefs": [
                  { 'bSortable': false, 'aTargets': [ 0 ] }
                ],
                "aaSorting": [[ 0, "asc" ]],
                "oLanguage": {
                    "sLengthMenu": "_MENU_ ",
                    "sInfo": "Showing <b>_START_ to _END_</b> of _TOTAL_ entries"
                },
                bAutoWidth     : true,
                fnPreDrawCallback: function () {
                    if (!responsiveHelper) {
                        responsiveHelper = new ResponsiveDatatablesHelper(tableElement, breakpointDefinition);
                    }
                },
                fnRowCallback  : function (nRow) {
                    responsiveHelper.createExpandIcon(nRow);
                },
                fnDrawCallback : function (oSettings) {
                    responsiveHelper.respond();
                }
            }
            tableElement.dataTable(options);
        }
    }

    dashboardTable.prototype.drawTable = function(){
        var self = this,
            html_box = ""+
                '<div class="row-fluid">'+
                  '<div class="span{{COLUMNS}}">'+
                    '<div class="grid simple ">'+
                      '<div class="grid-title">'+
                        '<h4>{{TITLE_PLACEHOLDER}}</h4>'+
                        '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
                      '</div>'+
                      '<div class="grid-body ">'+
                        '<p>{{DESCRIPTION_PLACEHOLDER}}</p>'+
                        '{{CONTENT_TOP_TO_APPEND}}' +
                        '<div class="row-fluid column-seperation table-content" style="{{SCROLL}}">'+
                            '{{TABLE_PLACEHOLDER}}'+
                        '</div>'+
                      '</div>'+
                    '</div>'+
                  '</div>'+
                '</div>',
            title = this.opts.title || '';

        html_box = html_box.replace("{{TITLE_PLACEHOLDER}}", title);
        html_box = html_box.replace("{{COLUMNS}}", this.opts.columns_size || '12')
        if(this.opts.scroll == true){
          html_box = html_box.replace("{{SCROLL}}", "overflow-x: auto");
        } else{
          html_box = html_box.replace("{{SCROLL}}", "");
        }

        if(this.opts.element_top){
          $elem = $(this.opts.element_top);
          html_box = html_box.replace("{{CONTENT_TOP_TO_APPEND}}", $elem.clone().html());
        } else {
          html_box = html_box.replace("{{CONTENT_TOP_TO_APPEND}}", '');
        }

        if(this.opts.description){
          html_box = html_box.replace("{{DESCRIPTION_PLACEHOLDER}}", this.opts.description);
        } else {
          html_box = html_box.replace("{{DESCRIPTION_PLACEHOLDER}}", '');
        }

        this.loadTable(function(table_html){
            html_box = html_box.replace("{{TABLE_PLACEHOLDER}}", table_html);
            self.$wrapper.html(html_box);
            self.$wrapper.find(".reload").click(function(){
                self.refresh();
            });
            self.bindElements();
            self.bindDataTable();
            if(self.opts.url_export){
                self.insertExportLinkInTable();
            }
            if(self.callback_user){
              self.callback_user();
            }
        });
    }

    dashboardTable.prototype.insertExportLinkInTable = function(){
        var html_link = '<a href="'+this.opts.url_export+'" style="margin-left:20px; line-height:30px; color: #555">Click to Export to Word</a>';
        this.$wrapper.find('.dataTables_length').append(html_link);
    }

    dashboardTable.prototype.refresh = function(){
        var self = this;
        this.loadTable(function(table_html){
            self.$wrapper.find(".table-content").html(table_html);
            self.bindElements();
            self.bindDataTable();
        });
    }

    dashboardTable.prototype.loadTable = function(callback){
        $.get(this.url, function(table){
            callback(table);
        })
    }


    $.fn.dashboardTable = function(url_table, opts, callback) {
        new dashboardTable( this, url_table, opts, callback );
        return this;
    };
 
}( jQuery ));
