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
    report: function(infoMilestone, dataMilestone) {
      var data = {
        'info': infoMilestone,
        'table': {}
      }, i = 0, size = dataMilestone.length;

      for (i; i < size; i++) {
        var aux = dataMilestone[i];
        var key = aux.DT_RowId;
        var activitypoa = (aux.activitypoa === null) ? '' : aux.activitypoa;
        var agreements = (aux.agreements === null) ? '' : aux.agreements;
        var alerts = (aux.alerts === null) ? '' : aux.alerts;
        var recommendation = (aux.recommendation === null) ? '' : aux.recommendation;
        data.table[key] = {
          activitypoa: activitypoa,
          agreements: agreements,
          alerts: alerts,
          audience: aux.audience,
          country: aux.country,
          indicator: aux.indicator,
          milestone: aux.milestone,
          quarter: aux.quarter,
          recommendation: recommendation,
          status: aux.status
        };
      }

      services.milestones.report({
        'type': 'POST',
        data: data,
        success: function(data) {
          window.open(data.url);
        },
        error: function(data, msg) {
          console.log(data);
        }
      });
    },
    addFormDetailData: function(data) {
      $('#formalertsnotes').val(data.alerts);
      $('#formrecommendation').val(data.recommendation);
      $('#formagreements').val(data.agreements);
      $('#formpoa').val(data.activitypoa);
    }
  };

  dashboard.milestones = milestones;
  window.dashboard = dashboard;

}) (window, document, jQuery);