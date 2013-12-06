(function (window, document, $) {


	var dashboard = window.dashboard || {};

	/******* LOGIN *****/

	dashboard.login = dashboard.login || {};

	dashboard.login = {
		'loginButton': '#form-signin',
		'activitybutton': '#form-activity',
		bind: function () {
			var instance = this;
			var loginButton = $(instance.loginButton);
			$(".alert").alert();
			
			loginButton.bind('submit', function (evt) {
				evt.preventDefault();
				var loginEmailVal = $('#signin-email').val();
				var passwordVal = $('#signin-password').val();
				if (!utils.checkEmail(loginEmailVal)) {
					instance.errorcallback.call(this, 'Email is not valid.');
				}
				else {
					instance.submit.call(this, {
						user: loginEmailVal,
						pass: passwordVal,
						active: false
					});
				}
			});
			$('#alert-error').bind('closed', function () {
				$('#alert-error').hide();
			});

			var activitybutton = $(instance.activitybutton);

			activitybutton.bind('submit', function (evt) {
				evt.preventDefault();
				var password = $('#activity-password').val();
				var confirm = $('#activity-password-confirm').val();
				if (utils.isEmpty(password) && utils.isEmpty(confirm)) {
					$('#alert-error-activity').show();
				} else {
					if ($.trim(password) != $.trim(confirm)) {
						$('#alert-error-activity').show();
					} else {
						var url = window.location.href;
						var email = unescape(url.split('email=')[1].split('&')[0]);
						instance.submitPassword.call(this, {
							user: email,
							pass: password,
							active: true
						});
					}
				}
			});

			$('#alert-error-activity').bind('closed', function () {
				$('#alert-error-activity').hide();
			});
		},
		submit: function (opt) {
			if (opt) {
				var param = {
					username: opt.user,
					password: opt.pass,
					active: opt.active
				};
				services.loginRequest({
					type: 'POST',
					data: param,
					success: function (data) {
						if (data.error.length > 0) {
							dashboard.login.errorcallback.call(this, data.error.join(''));
						} else {
							window.location.href = "main.php";
						}
					},
					error: function (data) {
						$('#alert-error-activity').show();
					}
				});
			}
		},
		submitPassword: function (opt) {
			if (opt) {
				var param = {
					username: opt.user,
					password: opt.pass,
					active: opt.active
				};
				services.passwordRequest({
					type: 'POST',
					data: param,
					success: function (data) {
						if (data.error.length > 0) {
							$('#alert-error-activity').show();
						} else {
							window.location.href = "../main.php";
						}
					},
					error: function (data) {
						if (opt.active === false) {
							dashboard.login.errorcallback.call(this, data.error.join(''));
						} else {
							$('#alert-error-activity').show();
						}
					}
				});
			}
		},
		errorcallback: function(msg) {
			$('#alert-msg').html(msg);
			$('#alert-error').show();
		}
	};

	/***** MAIN.PHP *****/
	dashboard.main = dashboard.main || {};
	dashboard.main = {
		bind: function () {
			$('#formAddUser').bind('submit', function (evt) {
				evt.preventDefault();
				//formfirstname
				//formlastname
				//formemailuser
				//formpassworduser
				//formphoneuser
				var fname = $('#formfirstname').val();
				var lname = $('#formlastname').val();
				var email = $('#formemailuser').val();
				var pass = $('#formpassworduser').val();
				var phone = $('#formphoneuser').val();
				var level = 'user';
				$( "#formleveluser select option:selected" ).each(function() {
					level = $( this ).text();
				});
				var countries = dashboard.main.countries();
				dashboard.main.addUser({
					fname: fname,
					lname: lname,
					email: email,
					phone: phone,
					countries: countries,
					level: level
				});
			});
		},
		countries: function() {
			var checked = [];
			$('#formAddUser input:checkbox').each(function () {
				if (this.checked) {
					checked.push(this.value);
				}
			});
			
			return checked;
		},
		addUser: function(opt) {
			var error = [];
			if (opt) {
				if (opt.fname && typeof opt.fname != 'undefined' && !utils.isEmpty(opt.name)) {
					if (opt.lname && typeof opt.lname != 'undefined' && !utils.isEmpty(opt.lname)) {
						if (opt.email && typeof opt.email !='undefined' && !utils.isEmpty(opt.email) && utils.checkEmail(opt.email)) {
							if (opt.countries && typeof opt.countries != 'undefined' && opt.countries.length > 0) {
								dashboard.main.requestAddUser(opt);
							} else {
								error.push('Country must be filled.');
							}
						} else {
							error.push('A valid email must be filled.');
						}
					} else {
						error.push('Last Name must be filled.');
					}
				} else {
					error.push('First Name must be filled.');
				}
			}

			if (error.length > 0) {
				// console.log(error);
				dashboard.main.showAlertAddUser(error.join(' '));
			}
		},
		requestAddUser: function(opt) {
			services.addUserRequest({
				type: 'POST',
				data: {
					fname: opt.fname,
					lname: opt.lname,
					email: opt.email,
					countries: opt.countries.join(','),
					phone: opt.phone,
					level: opt.level
				},
				success: function (data) {
					if (data.error && data.error.length > 0) {
						dashboard.main.showAlertAddUser(data.error.join(' '));
					} else {
						if (data.msg && data.msg == 'success') {
							dashboard.main.showAlertAddUser('The user was added successfully and an email was sent with the activation link.');
							setTimeout(function () {
								dashboard.main.hideAlertAddUser();
							}, 5000);
							dashboard.main.cleanFormAddUser();
						}
					}
				},
				error: function (data) {
					dashboard.main.showAlertAddUser('An error happened when the system tried to add the user. Please, try again soon.');
				}
			});
		},
		cleanFormAddUser: function () {
			$('#formfirstname').val('');
			$('#formlastname').val('');
			$('#formemailuser').val('');
			$('#formpassworduser').val('');
			$('#formphoneuser').val('');
		},
		showAlertAddUser: function (msg) {
			$('#alert-create-user-msg').html(msg);
			$('#alert-create-user').show();
		},
		hideAlertAddUser: function() {
			$('#alert-create-user').hide();
		}
	};

	$(document).ready(function() {

		//bind events for LOGIN
		dashboard.login.bind();

		//bind events for MAIN
		dashboard.main.bind();

		dashboard.main.hideAlertAddUser();
	});

	window.dashboard = dashboard;

})(window, document, jQuery);