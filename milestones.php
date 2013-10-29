<?php 
    include('./php/signin.php');
    require_once('./php/trans.php');

    $country = _t('Country', $_SESSION['SESS_LANG']);
    $paymentindicador = _t('Payment Indicador', $_SESSION['SESS_LANG']);
    $milestone = _t('Milestone', $_SESSION['SESS_LANG']);
    $quarter = _t('Quarter', $_SESSION['SESS_LANG']);
    $audience = _t('Audience', $_SESSION['SESS_LANG']);
    $status = _t('Status', $_SESSION['SESS_LANG']);
    $alertnotes = _t('Alerts/Notes', $_SESSION['SESS_LANG']);
    $recommendation = _t('Recommendation TL', $_SESSION['SESS_LANG']);
    $agreements = _t('Agreements', $_SESSION['SESS_LANG']);
    $activitypoa = _t('Activity in POA', $_SESSION['SESS_LANG']);
    $userCountries = $_SESSION["SESS_COUNTRIES"];
    $update = _t('Updated', $_SESSION['SESS_LANG']);
    $executed = _t('Executed', $_SESSION['SESS_LANG']);
    $financial = _t('Financial Executed', $_SESSION['SESS_LANG']);
    $alerts = _t('Alerts', $_SESSION['SESS_LANG']);
    $fund = _t('Fund', $_SESSION['SESS_LANG']);
    $physicalprogress = _t('Physical Progress', $_SESSION['SESS_LANG']);
    $financialprogress = _t('Financial Progress', $_SESSION['SESS_LANG']);
    $inforecommendation = _t('Recommendation', $_SESSION['SESS_LANG']);
    $montocomprometido = _t('Monto Comprometido', $_SESSION['SESS_LANG']);

    
?>
<!DOCTYPE html>
<html lang="en">
    
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Dashboard Web</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <!-- Le styles -->


        <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
            <script src="../assets/js/html5shiv.js"></script>
        <![endif]-->
        <!-- Fav and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="./ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="./ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="./ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="./ico/apple-touch-icon-57-precomposed.png">
        <link rel="shortcut icon" href="./ico/favicon.png">

    <style type="text/css">
                @import "./css/bootstrap.css";
                @import "./css/dataTables.bootstrap.css";

        #container {
            padding-top: 60px !important;
            width: 940px !important;
        }
        #dt_example .big {
            font-size: 1.3em;
            line-height: 1.45em;
            color: #111;
            margin-left: -10px;
            margin-right: -10px;
            font-weight: normal;
        }
        #dt_example {
            font: 85%/1.40em "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
            color: #111;
        }
        div.dataTables_wrapper, table {
            font: 13px/1.40em "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
        }
        #dt_example h1 {
            font-size: 16px !important;
            color: #111;
        }
        #footer {
            line-height: 1.45em;
        }
        div.examples {
            padding-top: 1em !important;
        }
        div.examples ul {
            padding-top: 1em !important;
            padding-left: 1em !important;
            color: #111;
        }
      table {
        margin: 1em 0;
        clear: both;
        width: 80%;
        float: center;
        margin-left: 10px;
      }
    
    </style>

        <link rel="stylesheet" type="text/css" href="./css/style.css">
        <link rel="stylesheet" type="text/css" href="./css/bootstrap-responsive.css">


    <script type="text/javascript" charset="utf-8" src="./js/DataTables/jquery.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/jquery.dataTables.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/TableTools.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/dataTables.editor.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/jquery.dataTables.editable.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/bootstrap.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/dataTables.bootstrap.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/dataTables.editor.bootstrap.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/DataTables/ZeroClipboard.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/numeral.min.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/utils.js"></script>

    
   <script type="text/javascript" charset="utf-8">


    function getContriesList() {
        var aCountriesList = new Array();

        aCountriesList[0] = { "label": "Belize", "value": "Belize" };
        aCountriesList[1] = { "label": "Costa Rica", "value": "Costa Rica" };
        aCountriesList[2] = { "label": "El Salvador", "value": "El Salvador" };
        aCountriesList[3] = { "label": "Guatemala", "value": "Guatemala" };
        aCountriesList[4] = { "label": "Honduras", "value": "Honduras" };
        aCountriesList[5] = { "label": "Mexico", "value": "Mexico" };
        aCountriesList[6] = { "label": "Nicaragua", "value": "Nicaragua" };
        aCountriesList[7] = { "label": "Panama", "value": "Panama" };

        return aCountriesList;
    }

    function getStatusList() {
        var aStatusList = [{
            'label': '<?= _t("Completed", $_SESSION["SESS_LANG"])?>',
            'value': '<?= _t("Completed", $_SESSION["SESS_LANG"])?>'
        }, {
            'label': '<?= _t("In Process", $_SESSION["SESS_LANG"])?>',
            'value': '<?= _t("In Process", $_SESSION["SESS_LANG"])?>'
        }, {
            'label': '<?= _t("Delayed", $_SESSION["SESS_LANG"])?>',
            'value': '<?= _t("Delayed", $_SESSION["SESS_LANG"])?>'
        }];
        // aStatusList[0] = { "label": "Completado", "value": "Completado" };
        // aStatusList[1] = { "label": "En Proceso", "value": "En Proceso" };
        // aStatusList[2] = { "label": "Pendiente", "value": "Pendiente" };
        // Na coluna de status, nao deveriamos permitir a entrada de qualquer
        // valor. Por isso, a ideia e' de colocar um combo box com as opcoes
        // pre-definidas: Complido, En Proceso, Retrasado (em ingles: Completed,
        // In process, Delayed).
        return aStatusList;
    }
    
    $.extend( $.fn.dataTableExt.oStdClasses, {
        "sWrapper": "dataTables_wrapper form-inline"
    } );

    var oTable;
    var iTable; //datatable first form - INFO FORM
    var infoeditor;
    var editor; // use a global for the submit and return data rendering in the examples
    var dataDelete = null;
    var noDelete = null;
    //var countryForm =  ['Belize', 'Costa Rica', 'El Salvador', 'Honduras', 'Guatemala', 'Mexico', 'Nicaragua', 'Panama'];
    var countryForm = '<?= $userCountries; ?>'.split(',');
    var countriesHash = createCountryObj(countryForm);
    var statusForm = ['<?= _t("Completed", $_SESSION["SESS_LANG"])?>', '<?= _t("In Process", $_SESSION["SESS_LANG"])?>', '<?= _t("Pending", $_SESSION["SESS_LANG"])?>'];
    var audienceForm = ['<?= _t("Donors", $_SESSION["SESS_LANG"])?>', '<?= _t("Country", $_SESSION["SESS_LANG"])?>'];
    var dataDetailUpdate = '';
    var countrySelect = '<?= $_SESSION["SESS_COUNTRY"]?>';
    var userLevel = '<?= $_SESSION['SESS_LEVEL']; ?>';

    function filterCountry(param) {
        var country = utils.removeEmpty(param);
        if (countriesHash[country] != undefined) {
            return countriesHash[country];
        }

        return false;
    }

    /**
     * Convert array of countries for JSON Object
     */
    function createCountryObj(vector) {
        var obj = {};
        for (var i = 0; i < vector.length; i++) {
            var key = utils.removeEmpty(vector[i]);
            obj[key] = vector[i];
        }
        return obj;
    }

    /* Formating function for row details */
    function fnFormatDetails ( oTable, nTr )
    {
        var aData = oTable.fnGetData( nTr );
        var sOut = aData[1]+' '+aData[4];
        return sOut;
    }

    function filterCountries ( country ) {
        var response = false;
        for (var key in countriesHash) {
            if (country.toLowerCase() == countrySelect.toLowerCase()) {//countriesHash[key].toLowerCase()) {
                response = true;
                break;
            }
        }
        return response;
    }
  
    var Editor = $.fn.dataTable.Editor;
    Editor.display.details = $.extend( true, {}, Editor.models.displayController, {
        "init": function ( dte ) {
            // No initialisation needed - we will be using DataTables' API to display items
            return Editor.display.details;
        },

        "open": function ( dte, append, callback ) {
            var table = $(dte.s.domTable).dataTable();

            // Close any rows which are already open
            Editor.display.details.close( dte );

            // Call fnOpen on the DataTable
            table.fnOpen( dte.s.editRow, append, 'DTE_EditorDetails' );
            table.fnUpdate( '<img src="/release/DataTables/examples/examples_support/details_close.png">', dte.s.editRow, 0, false );

            if ( callback ) {
                callback();
            }
        },

        "close": function ( dte, callback ) {
            var table = $(dte.s.domTable).dataTable();
            var openRows = table.fnSettings().aoOpenRows;

            // Call fnClose on the DataTable
            if ( openRows.length > 0 ) {
                var openRow = openRows[0].nParent;

                table.fnClose( openRow );
                table.fnUpdate( '<img src="/release/DataTables/examples/examples_support/details_open.png">', openRow, 0, false );
            }

            if ( callback ) {
                callback();
            }
        }
    } );

    $(document).ready(function() {

        infoeditor = new $.fn.dataTable.Editor({
            "ajaxUrl": 'php/process-info-milestones.php',
            "domTable": '#info_milestone',
            "fields": [{
                "label": '<?php echo($country); ?>:',
                "name": 'country',
                "required": true
            }, {
                "label": '<?php echo($update); ?>:',
                "name": 'updated',
                "required": true,
            }, {
                "label": '<?php echo($executed); ?>:',
                "name": 'executed',
                "required": true
            }, {
                "label": '<?php echo($financial); ?>:',
                "name": 'planned',
                "required": true
            }, {
                "label": '<?php echo($montocomprometido); ?>:',
                "name": 'montocomprometido',
                "required": true
            }, {
                "label": '<?php echo($alerts); ?>:',
                "name": 'alerts',
                "type": "textarea",
                "required": true
            }, {
                "label": '<?php echo($fund); ?>:',
                "name": 'expended',
                "required": true
            }, {
                "label": '<?php echo($physicalprogress); ?>:',
                "name": 'pep',
                "required": true
            }, {
                "label": '<?php echo($financialprogress); ?>:',
                "name": 'progression',
                "required": true
            }, {
                "label": '<?php echo($recommendation); ?>:',
                "name": 'recommendation',
                "type": "textarea",
                "required": true
            }],
            "events": {
                "onPreOpen": function() {
                    //TODO: Refactory
                    setTimeout(function () {
                        //executed
                        $('#DTE_Field_executed').focus( function(e) {
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            $(this).val(executed);
                        });

                        $('#DTE_Field_executed').bind('keyup', function (e) {
                            e.preventDefault();
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            if (utils.isNumber(executed)) {
                                $(this).val(executed);
                            } else {
                                var last = executed[executed.length - 1];
                                executed = executed.replace(last, '');
                                $(this).val(executed);
                            }
                        });

                        $('#DTE_Field_executed').blur( function(e) {
                            var executed = $(this).val();
                            if (executed.indexOf('%') == (-1)) {
                                $(this).val(executed + '%');
                            }
                        });
                        //planned
                        $('#DTE_Field_planned').focus( function(e) {
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            $(this).val(executed);
                        });

                        $('#DTE_Field_planned').bind('keyup', function (e) {
                            e.preventDefault();
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            if (utils.isNumber(executed)) {
                                $(this).val(executed);
                            } else {
                                var last = executed[executed.length - 1];
                                executed = executed.replace(last, '');
                                $(this).val(executed);
                            }
                        });

                        $('#DTE_Field_planned').blur( function(e) {
                            var executed = $(this).val();
                            if (executed.indexOf('%') == (-1)) {
                                $(this).val(executed + '%');
                            }
                        });
                        //pep
                        $('#DTE_Field_pep').focus( function(e) {
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            $(this).val(executed);
                        });

                        $('#DTE_Field_pep').bind('keyup', function (e) {
                            e.preventDefault();
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            if (utils.isNumber(executed)) {
                                $(this).val(executed);
                            } else {
                                var last = executed[executed.length - 1];
                                executed = executed.replace(last, '');
                                $(this).val(executed);
                            }
                        });

                        $('#DTE_Field_pep').blur( function(e) {
                            var executed = $(this).val();
                            if (executed.indexOf('%') == (-1)) {
                                $(this).val(executed + '%');
                            }
                        });
                        //progression
                        $('#DTE_Field_progression').focus( function(e) {
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            $(this).val(executed);
                        });

                        $('#DTE_Field_progression').bind('keyup', function (e) {
                            e.preventDefault();
                            var executed = $(this).val();
                            executed = utils.removePerc(executed);
                            if (utils.isNumber(executed)) {
                                $(this).val(executed);
                            } else {
                                var last = executed[executed.length - 1];
                                executed = executed.replace(last, '');
                                $(this).val(executed);
                            }
                        });

                        $('#DTE_Field_progression').blur( function(e) {
                            var executed = $(this).val();
                            if (executed.indexOf('%') == (-1)) {
                                $(this).val(executed + '%');
                            }
                        });
                    }, 1000);
                }   
            }
        });

        iTable = $('#info_milestone').dataTable( {
            "sDom": "<'row-fluid'<'span6'T><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
            "sAjaxSource": "php/process-info-milestones.php",
            "bAutoWidth": false,
            "iDisplayLength": 1,
            "bPaginate": false,
            "bFilter": false,
            "bSort": false,
            "bInfo": false,
            "fnServerData": function(sSource, aoData, fnCallback, oSettings ) {
                oSettings.jqXHR = $.ajax( {
                    "dataType": 'json',
                    "type": "POST",
                    "url": sSource,
                    "data": 's',
                    "success": function(obj) {                        
                        var aaData = obj.aaData;
                        var newData = [];
                        for (var i =0; i < aaData.length; i++) {
                            if (filterCountries(aaData[i].country)) {
                                newData.push(aaData[i]);
                            }
                        }
                        obj.aaData = newData;
                        fnCallback(obj);
                    }
              });
            },
            "aoColumns": [
                { "mData": "country", "bSortable": false, "bSearchable": false, "sClass": "center"},
                { "mData": "updated", "bSortable": false, "bSearchable": false, "sClass": "center" },
                { "mData": "executed", "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function(obj) {
                    var executed = obj.aData.executed;
                    if (executed.indexOf('%') == (-1)) {
                        return executed.concat('%');
                    } else {
                        return executed;
                    }
                } },
                { "mData": "planned", "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function(obj) {
                    var planned = obj.aData.planned;
                    if (planned.indexOf('%') == (-1)) {
                        return planned.concat('%');
                    } else {
                        return planned;
                    }
                } },
                { "mData": "montocomprometido", "bSortable": false, "bSearchable": false, "sClass": "center" },
                { "mData": null, "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function(obj) {
                    var alerts = obj.aData.alerts;
                    // alerts = utils.paddingText(alerts, 75);
                    return alerts;
                } },
                { "mData": "expended", "bSortable": false, "bSearchable": false, "sClass": "center" },
                { "mData": "pep", "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function(obj) {
                    var pep = obj.aData.pep;
                    if (pep.indexOf('%') == (-1)) {
                        return pep.concat('%');
                    } else {
                        return pep;
                    }
                } },
                { "mData": "progression","bSortable": false, "bSearchable": false, "sClass": "center" , "fnRender": function(obj) {
                    var progression = obj.aData.progression;
                    if (progression.indexOf('%') == (-1)) {
                        return progression.concat('%');
                    } else {
                        return progression;
                    }
                }},
                { "mData": "recommendation", "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function(obj) {
                    var recommendation = obj.aData.recommendation;
                    // recommendation = utils.paddingText(recommendation, 75);
                    return recommendation;
                }}],
                "oLanguage": {
                    "sLengthMenu": "_MENU_ records per page"
                },
                "oTableTools": {
                    "aButtons": [
                    {"sExtends": 'text',
                        "sButtonText": "<?=_t('Edit', $_SESSION['SESS_LANG']); ?>",
                        "fnClick": function ( button, config ) {
                            infoeditor.edit($('#info_milestone').find('tbody tr')[0],
                                'Edit',
                                {
                                    "label": "<?=_t('Save', $_SESSION['SESS_LANG']); ?>",
                                    "className": "btn btn-primary",
                                    "fn": function () {
                                        infoeditor.submit()
                                    }
                                }
                            );
                        }
                    }
                ]
            }
        });

        /*EDITOR MILESTONES*/

        editor = new $.fn.dataTable.Editor( {
            "ajaxUrl": "php/process-milestones.php",
            "domTable": "#example",
            "events": {
                "onPreOpen": function() {
                    setTimeout(function () {
                        $('#DTE_Field_country').typeahead({source: countryForm});
                        $('#DTE_Field_audience').typeahead({source: audienceForm});
                        $('#DTE_Field_status').typeahead({source: statusForm});
                    }, 2000);
                },
                "onPreSubmit": function(o) {
                    
                },
                "onSubmitSuccess": function(data) {
                    console.log('sucesso');
                },
                "onSubmitError": function(data) {
                  console.log('error');
                }
            },
            "fields": [ {
                    "label": "<?php echo($country); ?>:",
                    "name": "country",
                    "required": true
                }, {
                    "label": "<?php echo($paymentindicador); ?>:",
                    "name": "indicator",
                    "type": "textarea",
                    "required": true
                }, {
                    "label": "<?php echo($milestone); ?>:",
                    "name": "milestone",
                    "type": "textarea",
                    "required": true
                }, {
                    "label": "<?php echo($quarter); ?>:",
                    "name": "quarter",
                    "required": true
                }, {
                    "label": "<?php echo($audience); ?>:",
                    "name": "audience",
                    "required": true
                }, {
                    "label": "<?php echo($status); ?>:",
                    "name": "status",
                    "type": "select",
                    "ipOpts": getStatusList(),
                    "required": true
                }
            ]
        } );

        oTable = $('#example').dataTable( {
            "sDom": "<'row-fluid'<'span6'T><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
            "sAjaxSource": "php/process-milestones.php",
            "aaSorting":[[0, "desc"]],
            "bAutoWidth": false,
            "iDisplayLength": 10,
            "fnServerData": function(sSource, aoData, fnCallback, oSettings ) {
                oSettings.jqXHR = $.ajax( {
                    "dataType": 'json',
                    "type": "POST",
                    "url": sSource,
                    "data": 's',
                    "success": function(obj) {
                        var aaData = obj.aaData;
                        var newData = [];
                        for (var i =0; i < aaData.length; i++) {
                            if (filterCountries(aaData[i].country)) {
                                newData.push(aaData[i]);
                            }
                        }
                        obj.aaData = newData;
                        fnCallback(obj);
                    }
              });
            },
            "aoColumns": [
                { "mData": "country"},
                { "mData": "indicator" },
                { "mData": "milestone" },
                { "mData": "quarter", "sClass": "center" },
                { "mData": "audience", "sClass": "center" },
                { "mData": "status", "sClass": "center" },
                { "mData": null, "bSortable": false, "bSearchable": false, "sClass": "center",
                "fnRender": function(obj) {
                    var sReturn = obj.aData[ obj.iDataColumn ];
                    var returnButton = "<a class='btn btn-small btn-primary' id='add-detail' href='#' name='" + sReturn + "'><i class='icon-plus icon-white'></i> Detail</a>";
                    return returnButton;
                }},
                {"mData": null, "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function() {
                    return '<a class="btn btn-small btn-primary" name="edit" href=""><?php echo(_t("Edit", $_SESSION["SESS_LANG"])); ?></a>';
                }},
                { "mData": null, "bSortable": false, "bSearchable": false, "sClass": "center", "fnRender": function() {
                    if (userLevel == 'admin') {
                        return '<button class="btn btn-small btn-primary" name="delete" type="button"><?php echo(_t("Delete", $_SESSION["SESS_LANG"])); ?></button>';
                    } else {
                        return '<button class="btn btn-small btn-primary" name="delete" type="button" disabled="true"><?php echo(_t("Delete", $_SESSION["SESS_LANG"])); ?></button>';
                    }
                }
            }],
            "oLanguage": {
                    "sLengthMenu": "_MENU_ records per page"
                },
                "oTableTools": {
                    "aButtons": [
                        {"sExtends": "text",
                            "sButtonText": "<?=_t('New', $_SESSION['SESS_LANG']); ?>",
                            "fnClick": function ( button, config ) {
                                editor.create(
                                    'Create New Report',
                                    {
                                        "label": "New",
                                        "className": "btn btn-primary",
                                        "fn": function () {
                                            editor.submit()
                                        }
                                    }
                                );
                            }
                        },
                        {"sExtends": "text", "sButtonText": "Word", "fnClick": function() {
                            // var infoMilestone = iTable.fnGetData();
                            // var milestonesData = oTable.fnGetData();
                            dashboard.milestones.report(countrySelect);
                            //window.open("php/report.php");
                            }
                        },
                        {"sExtends": "text", "sButtonText": "CSV", "fnClick": function() {
                            dashboard.milestones.exportExcel(countrySelect);
                        }}
                    ]
            }
        });


    var nEditing = null;

    $('#example a[name="edit"]').live('click', function (e) {
        e.preventDefault();

        var editing = '<?= _t("Save", $_SESSION[SESS_LANG]);?>';

        /* Get the row as a parent of the link that was clicked on */
        var nRow = $(this).parents('tr')[0];

        if ( nEditing !== null && nEditing != nRow ) {
            /* A different row is being edited - the edit should be cancelled and this row edited */
            restoreRow( oTable, nEditing );
            editRow( oTable, nRow );
            nEditing = nRow;
        }
        else if ( nEditing == nRow && this.innerHTML == editing ) {
            /* This row is being edited and should be saved */
            saveRow( oTable, nEditing );
            nEditing = null;
        }
        else {
            /* No row currently being edited */
            editRow( oTable, nRow );
            nEditing = nRow;
        }
    } );

    $('#example button[name="delete"]').live('click', function (e) {
        e.preventDefault();
        dataDelete = $(this).parents('tr')[0];
        //oTable.fnDeleteRow( nRow );
        noDelete = dataDelete;
        $('#modalDeleteMilestones').modal({
            keyboard: false
        });
    });

    $('#modalDeleteButton').live('click', function (e) {
        e.preventDefault();
        var id = dataDelete.getAttribute('id').split('_')[1];
        var params = {
            id: id
        };
        dashboard.milestones.delete(params);
        oTable.fnDeleteRow( noDelete );
        setTimeout(function () {
            $('#modalDeleteMilestones').modal('hide');
        }, 1000);
    });


      $(window).scroll(function () {
            // code will go here

        });


        $("#add-detail").live('click', function (e) {
            //var nTr = this.parentNode.parentNode.id;
            e.preventDefault();
            var nTr = $(this).parents('tr')[0];
            var aData = oTable.fnGetData( nTr );
            
            dataDetailUpdate = aData.DT_RowId.split('_')[1];
            dashboard.milestones.addFormDetailData(aData);
            $('#modalReportDetail').modal({
                keyboard: false
            });
        });

        $('#addReportDetail').bind('click', function (e) {
            e.preventDefault();
            dashboard.milestones.addSubmit(dataDetailUpdate);
            utils.cleanInputs('#modalReportDetail');
            $('#modalReportDetail').modal('hide');
        });

    });

    function getSelectHTMLEdit(select) {
        var status = getStatusList();
        var html = ['<select>'];
        for (var i = 0, size = status.length; i < size; i++) {
            if (status[i].value.toLowerCase() == select.toLowerCase()) {
                html.push('<option value="' + status[i].value + '" selected="true"> ' + status[i].label + '</option>');
            } else {
                html.push('<option value="' + status[i].value + '"> ' + status[i].label + '</option>');
            }
        }
        html.push('</select>');
        return html.join('');
    }

    function editRow ( oTable, nRow )
    {
        var aData = oTable.fnGetData(nRow);
        var jqTds = $('>td', nRow);
        var status = getSelectHTMLEdit(aData.status);
        //jqTds[0].innerHTML = '<input name="contry" style="width: 67px;" value="'+aData.country+'" type="text">';
        if (userLevel != 'user') {
            jqTds[1].innerHTML = '<textarea style="height: 300px; width: 95%;">' + aData.indicator + '</textarea>';
            jqTds[2].innerHTML = '<textarea style="height: 300px; width: auto;">' + aData.milestone + '</textarea>';
            jqTds[3].innerHTML = '<input style="width: 68px;" value="'+aData.quarter+'" type="text">';
        }
        jqTds[4].innerHTML = '<input name="audience" style="width: 68px;" value="'+aData.audience+'" type="text">';
        jqTds[5].innerHTML = status;
        jqTds[7].innerHTML = '<a class="btn btn-small btn-primary" name="edit" href="#"><?= _t("Save", $_SESSION["SESS_LANG"]); ?></a>';

        var inputsAutocomplete = $('>td>input', nRow);

        //country
        $(inputsAutocomplete[0]).typeahead({source: countryForm});
        $(inputsAutocomplete[2]).typeahead({source: audienceForm});
    }

    function saveRow ( oTable, nRow )
    {
        var jqTds = $('>td', nRow);
        var jqInputs = $('input', nRow);
        var jqTextareas = $('textarea', nRow);
        var jqSelects = $('select', nRow);
        var options = jqSelects[0].options;
        var statusValue = '';
        for (var i = 0; i < options.length; i++) {
            if (options[i].selected) {
                statusValue = options[i].value;
            }
        }

        if (userLevel == 'user') {
            var audience = jqInputs[0].value;
            jqTds[4].innerHTML = audience;
            jqTds[5].innerHTML = statusValue;
            oTable.fnUpdate( jqInputs[0].value, nRow, 0, false );
            oTable.fnUpdate( statusValue, nRow, 5, false );
        } else {
            oTable.fnUpdate( jqInputs[0].value, nRow, 0, false );
            oTable.fnUpdate( jqInputs[1].value, nRow, 3, false );
            //oTable.fnUpdate( jqInputs[2].value, nRow, 4, false );
            oTable.fnUpdate( statusValue, nRow, 5, false );
            oTable.fnUpdate( jqTextareas[0].value, nRow, 1, false);
            oTable.fnUpdate( jqTextareas[1].value, nRow, 2, false);
            jqTds[1].innerHTML = jqTextareas[0].value;
            jqTds[2].innerHTML = jqTextareas[1].value;
            jqTds[3].innerHTML = jqInputs[0].value;
            jqTds[4].innerHTML = jqInputs[1].value;
            jqTds[5].innerHTML = statusValue;
        }
        var buttonText = '<?= (_t("Edit", $_SESSION["SESS_LANG"])); ?>';
        
        oTable.fnUpdate( '<a class="btn btn-small btn-primary" name="edit" href="">' + buttonText + '</a>', nRow, 7, false );
        oTable.fnDraw();
        var aData = oTable.fnGetData(nRow);
        
        var params = {
            id: aData.DT_RowId,
            audience: aData.audience,
            country: aData.country,
            indicator: aData.indicator,
            milestone: aData.milestone,
            quarter: aData.quarter,
            status: statusValue
        };

        dashboard.milestones.update(params);
    }

    </script>

    </head>
    
    <body>
        <!-- Part 1: Wrap all page content here -->
        <div id="wrap">
            <!-- NAVBAR -->
      <?php include 'menu.php'; ?>
            <!-- /.navbar-wrapper -->

            <!-- Begin page content -->
            <div class="container">
                <div class="page-header" id="follow">
                     <h2>Hitos técnicos del Tablero de Control</h2>
                  <p>Seguimiento Mensual de la Ejecución. Se solicita informar los hitos programados para todos los trimestres del año en curso con fuente en el Tablero de Control en línea y vinculados a indicadores de pago.</p>
                </div>
                <!-- INFO Milestone -->

                    <div id="info_wrapper" class="dataTables_wrapper" role="grid">

                        <div class="row">
                            <table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="info_milestone" width="90%">
                                <thead>
                                    <tr role="row">
                                        <th class="header headerSortDown" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-sort="ascending" aria-label="Country: activate to sort column descending"><?php echo($country); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 400px;" aria-label="Indicator: activate to sort column ascending"><?php echo($update); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 208px;" aria-label="Milestone: activate to sort column ascending"><?php echo($executed); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 60px;" aria-label="Quarter: activate to sort column ascending"><?php echo($financial); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 60px;" aria-label="Monto Comprometido: activate to sort column ascending"><?php echo($montocomprometido); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Audience: activate to sort column ascending"><?php echo($alerts); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Status: activate to sort column ascending"><?php echo($fund); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Status: activate to sort column ascending"><?php echo($physicalprogress); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Edit: activate to sort column ascending"><?php echo($financialprogress); ?></th>
                                        <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Delete: activate to sort column ascending"><?php echo($inforecommendation); ?></th>
                                    </tr>
                                </thead>                  
                            </table>
                        </div>
                    </div>
                <hr />
                <!-- Milestones -->
                <div id="example_wrapper" class="dataTables_wrapper" role="grid">

                    <div class="row">
            <table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="example" width="90%">
                            <thead>
                                <tr role="row">
                                    <th class="header headerSortDown" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-sort="ascending" aria-label="Country: activate to sort column descending"><?php echo($country); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 400px;" aria-label="Indicator: activate to sort column ascending"><?php echo($paymentindicador); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 208px;" aria-label="Milestone: activate to sort column ascending"><?php echo($milestone); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 60px;" aria-label="Quarter: activate to sort column ascending"><?php echo($quarter); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Audience: activate to sort column ascending"><?php echo($audience); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Status: activate to sort column ascending"><?php echo($status); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Status: activate to sort column ascending">Report</th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Edit: activate to sort column ascending"><?php echo(_t('Edit', $_SESSION["SESS_LANG"])); ?></th>
                                    <th class="header" role="columnheader" tabindex="0" aria-controls="example" rowspan="1" colspan="1" style="width: 80px;" aria-label="Delete: activate to sort column ascending"><?php echo(_t('Delete', $_SESSION["SESS_LANG"])); ?></th>
                                </tr>
                            </thead>

                    <tfoot>
                      <tr>
                          <th><?php echo($country); ?></th>
                          <th><?php echo($paymentindicador); ?></th>
                          <th><?php echo($milestone); ?></th>
                          <th><?php echo($quarter); ?></th>
                          <th><?php echo($audience); ?></th>
                          <th><?php echo($status); ?></th>
                          <th>Report</th>
                          <th><?php echo(_t('Edit', $_SESSION["SESS_LANG"])); ?></th>
                          <th><?php echo(_t('Delete', $_SESSION["SESS_LANG"])); ?></th>
                      </tr>
                  </tfoot>
              
                        </table>
                    </div>
                </div>
            </div>
            <div id="push"></div>
            <br/>
            <br>
            <div id="modalDeleteMilestones" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="modalDeleteMilestones" aria-hidden="true">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3><?php echo(_t('Delete', $_SESSION["SESS_LANG"])); ?></h3>
          </div>
          <div class="modal-body">
                <p>Are you sure to <strong>delete</strong> this?</p>
          <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true"><?php echo(_t('Cancel', $_SESSION["SESS_LANG"])); ?></button>
            <button id="modalDeleteButton" class="btn btn-primary"><?php echo(_t('Delete', $_SESSION["SESS_LANG"])); ?></button>
          </div>
        </div>
        </div>
        <div id="modalReportDetail" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="modalReportDetail" aria-hidden="true">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3>Report - Detail</h3>
          </div>
          <form id="formReportDetail">
          <div class="modal-body">
                <p class="formReportDetail">
                    <label for="formAlertsNotes"><?php echo($alertnotes); ?>:</label>
                        <!-- <input style="width:77%;" id="formalertsnotes" value="" name="formAlertsNotes" type="text" required /> -->
                        <textarea id="formalertsnotes" value="" name="formAlertsNotes" rows="10" cols="50"></textarea>
                    <label for="formRecommendation"><?php echo($recommendation);?>:</label>
                        <textarea id="formrecommendation" value="" name="formRecommendation" rows="10" cols="50"></textarea>
                        <!-- <input style="width: <?php if ($_SESSION["SESS_LANG"] == "en") { echo("67%"); } else { echo("69%"); } ?>;" id="formrecommendation" value="" name="formRecommendation" type="text" required /> -->
                    <label for="formAgreements"><?php echo($agreements);?>: </label>
                        <!-- <input style="width: <?php if ($_SESSION["SESS_LANG"] == "en") { echo("78%"); } else { echo("81%"); } ?>;" id="formagreements" value="" name="formAgreements" type="text" required /> -->
                        <textarea id="formagreements" value="" name="formAgreements" rows="10" cols="50"></textarea>
                    <label for="formPOA"><?php echo($activitypoa); ?>: </label>
                        <!-- <input style="width:<?php if ($_SESSION["SESS_LANG"] == "en") { echo("75%"); } else { echo("72%"); } ?>;" id="formpoa" value="" name="formPOA" type="text" required /> -->
                        <textarea id="formpoa" value="" name="formPOA" rows="10" cols="50"></textarea>
                </p>
          </div>
          <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true"><?php echo(_t('Close', $_SESSION["SESS_LANG"])); ?></button>
            <button id="addReportDetail" type="submit" class="btn btn-primary"><?php echo(_t('Add', $_SESSION["SESS_LANG"])); ?></button>
          </div>
          </form>
        </div>
        <div id="footer">
            <div class="container">
                <p class="muted credit">© Copyright 2013. Banco Interamericano de Desarrollo, como administrador del Fondo Mesoamericano de Salud - <a href="http://sm2015.org">Salud Mesoamérica 2015</a>.</p>
            </div>
        </div>

        <!-- Le javascript==================================================- ->
        <!-- Placed at the end of the document so the pages load faster -->
    </body>
    <script type="text/javascript" charset="utf-8" src="./js/services.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/milestones.js" ></script>
    <script type="text/javascript" charset="utf-8" src="./js/dashboard.js"></script>
    <script type="text/javascript" charset="utf-8" src="./js/menu.js"></script>
</html>