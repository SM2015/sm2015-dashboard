(function ( $ ) {
    var dashboardTable = function( wrapper, url, opts ) {
        this.$wrapper = wrapper;
        this.url = url;
        this.opts = opts;

        this.drawTable();
    };

    dashboardTable.prototype.bindElements = function(){
        var self = this,
            $textfields = this.$wrapper.find(".editable.text"),
            $textareafields = this.$wrapper.find(".editable.textarea"),
            $selectfields = this.$wrapper.find(".editable.select");

        $textfields.editable(self.opts.url_save, {
            height: 27,
            submitdata : function(value, settings) { 
                var field = $(this).attr("name");
                var data = {};
                data['objid'] = $(this).parent().attr('data-objid');
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
                data['objid'] = $(this).parent().attr('data-objid');
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
                    data['objid'] = $(this).parent().attr('data-objid');
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
            tableElement.dataTable({
                "sDom": "<'row-fluid'<'span6'l T><'span6'f>r>t<'row-fluid'<'span12'p i>>",
                    "oTableTools": {
                    "aButtons": [
                        {
                            "sExtends":    "collection",
                            "sButtonText": "<i class='icon-cloud-download'></i>",
                            "aButtons":    [ "csv", "xls", "pdf", "copy"]
                        }
                    ]
                },
                "sPaginationType": "bootstrap",
                 "aoColumnDefs": [
                  { 'bSortable': false, 'aTargets': [ 0 ] }
                ],
                "aaSorting": [[ 1, "asc" ]],
                "oLanguage": {
                    "sLengthMenu": "_MENU_ ",
                    "sInfo": "Showing <b>_START_ to _END_</b> of _TOTAL_ entries"
                },
                bAutoWidth     : false,
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
            });
        }
    }

    dashboardTable.prototype.drawTable = function(){
        var self = this,
            html_box = ""+
                '<div class="row-fluid">'+
                  '<div class="span12">'+
                    '<div class="grid simple ">'+
                      '<div class="grid-title">'+
                        '<h4>{{TITLE_PLACEHOLDER}}</h4>'+
                        '<div class="tools"> <a href="javascript:;" class="collapse"></a> <a href="#grid-config" data-toggle="modal" class="config"></a> <a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>'+
                      '</div>'+
                      '<div class="grid-body ">'+
                        '<div class="row-fluid column-seperation table-content">'+
                            '{{TABLE_PLACEHOLDER}}'+
                        '</div>'+
                      '</div>'+
                    '</div>'+
                  '</div>'+
                '</div>',
            title = this.opts.title || '';

        html_box = html_box.replace("{{TITLE_PLACEHOLDER}}", title);
        this.loadTable(function(table_html){
            html_box = html_box.replace("{{TABLE_PLACEHOLDER}}", table_html);
            self.$wrapper.html(html_box);
            self.$wrapper.find(".reload").click(function(){
                self.refresh();
            });
            self.bindElements();
            self.bindDataTable();
        });
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
        new dashboardTable( this, url_table, opts );
        return this;
    };
 
}( jQuery ));
