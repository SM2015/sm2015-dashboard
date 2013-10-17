(function (window, document, undefined, $) {

	var services = {

		loginRequest: function(options) {
			if (options) {
				options.url = 'php/login';
				services.request.call(this, options);
			}
		},

        passwordRequest: function(options) {
            if (options) {
                options.url = '../php/login';
                services.request.call(this, options);
            }
        },

        addUserRequest: function(options) {
            if (options) {
                options.url = 'php/register';
                services.request.call(this, options);
            }
        },

        milestones: {
            updateRequest: function (options) {
                if (options) {
                    options.url = 'php/milestones';
                    options.data.action = 'update';
                    services.request.call(this, options);
                }
            },
            deleteRequest: function (options) {
              if (options) {
                    options.url = 'php/milestones';
                    options.data.action = 'delete';
                    services.request.call(this, options);
                }
            },
            updateDetail: function(options) {
                if (options) {
                    options.url = 'php/milestones';
                    options.data.action = 'detail';
                    services.request.call(this, options);
                }
            },
            report: function(options) {
                if (options) {
                    options.url = 'php/report';
                    services.request.call(this, options);
                }
            },
            getDetail: function(options) {
                if (options) {
                    options.url = 'php/getDetailMilestone';
                    services.request.call(this, options);
                }
            }
        },

		request: function (options) {
            var instance = this;
            if (options !== undefined && typeof options == 'object') {
                var dataRequest = (options.data && typeof options.data == 'object') ? options.data: false;
                var typeRequest = (options.type && typeof options.type == 'string') ? options.type : 'GET';
                var dataTypeRequest = (options.dataType && typeof options.dataType == 'string') ? options.dataType : 'json';
                //precisa ter dataRequest para ser GET. Por isso de verificar
                if (dataRequest === false && typeRequest == 'POST') {
                    var msg = errorModule.getAjaxError.call(this, 'data');
                    instance.errorCallbackDefault.call(this, msg);
                    if (options.error) {
                        options.error.call(this, msg);
                    }
                } else {
                    var urlRequest = options.url;
                    var params = {
                        url: urlRequest,
                        type: typeRequest,
                        dataType: dataTypeRequest,
                        success: function(data) {
                            options.success.call(this, data);
                        },
                        error: function(data, msg) {
                            if (options.error) {
                                options.error.call(this, msg);
                            }
                        }
                    };
                    //adiciona os dados como parametros caso seja POST
                    if (dataRequest !== false) {
                        params.data =  dataRequest;
                    }
                    $.ajax(params);
                }
            }
		}

	};

	window.services = services;

})(window, document, undefined, jQuery);