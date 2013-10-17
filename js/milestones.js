( function (window, document, $) {

  var dashboard = window.dashboard || {};
  var milestones = {
    update: function (opt) {
      if (opt) {
        var id = opt.id.split('_')[1];
        opt.id = id;
        services.milestones.updateRequest({
            type: 'POST',
            data: opt,
            success: function (data) {
              if (data.error.length > 0) {
                console.log('error update');
              } else {
               console.log(data.msg);
              }
            },
            error: function (data) {
              console.log(data);
            }
          });
      }
    },
    updateDetail: function(opt) {
      if (opt) {
        services.milestones.updateDetail({
            type: 'POST',
            data: opt,
            success: function (data) {
              if (data.error.length > 0) {
                console.log('error update');
              } else {
               console.log(data.msg);
              }
            },
            error: function (data) {
              console.log(data);
            }
          });
      }
    },
    delete: function(opt) {
      if (opt) {
        services.milestones.deleteRequest({
            type: 'POST',
            data: opt,
            success: function (data) {
              if (data.error.length > 0) {
                console.log('error update');
              } else {
                console.log(data.msg);
              }
            },
            error: function (data) {
              console.log(data);
            }
          });
      }
    },
    addSubmit: function(rowID) {
      var alerts = $('#formalertsnotes').val();
      var recommendation = $('#formrecommendation').val();
      var agreements = $('#formagreements').val();
      var poa = $('#formpoa').val();


      var params = {
          id: rowID,
          alerts: alerts,
          recommendation: recommendation,
          agreements: agreements,
          activitypoa: poa
      };
      dashboard.milestones.updateDetail(params);
    },
    report: function(country) {
      var url = 'php/report.php?country=' + encodeURIComponent(country);
      window.open(url);
    },
    exportExcel: function(country) {
      var url = 'php/exportExcel.php?country=' + encodeURIComponent(country);
      console.log(url);
      window.open(url);
    },
    addFormDetailData: function(data) {
      var id = data["DT_RowId"].replace('row_', '');
      services.milestones.getDetail({
        data: {
          'rowid': id
        },
        success: function(data) {
          if (data.error.length > 0) {
            console.log('Error');
          } else {
            $('#formalertsnotes').val(data.alerts);
            $('#formrecommendation').val(data.recommendation);
            $('#formagreements').val(data.agreements);
            $('#formpoa').val(data.activitypoa);
          }
        },
        error: function(data, msg) {
          console.log(data);
        }

      });
      // $('#formalertsnotes').val(data.alerts);
      // $('#formrecommendation').val(data.recommendation);
      // $('#formagreements').val(data.agreements);
      // $('#formpoa').val(data.activitypoa);
    }
  };

  dashboard.milestones = milestones;
  window.dashboard = dashboard;

}) (window, document, jQuery);