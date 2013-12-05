	(function (window, document, $) {
	var profile = {
		submit: function(opt) {
			var that = this;
			services.profileRequest({
				type: 'POST',
				data: opt,
				success: function(data) {
					var html = '';
					if (data.error.length > 0) {
						html = "[Error] It's not possible to update profile at moment, try again soon.";
						that.showAlertEditUser(html);
						setTimeout(function (e) {
							that.hideAlertEditUser();
						}, 5000);
					} else {
						html = "The profile information was updated.";
						that.showAlertEditUser(html);
						that.updateForm(data);
						setTimeout(function (e) {
							that.hideAlertEditUser();
						}, 5000);
					}
				},
				error: function() {

				}
			});
		},
		updateForm: function(info) {
			$('#formeditfirstname').val(info.fname);
			$('#formeditlastname').val(info.lname);
			$('#formeditpassworduser').val(info.pass);
			$('#formeditphoneuser').val(info.phone);
		},
		showAlertEditUser: function (msg) {
			$('#alert-edit-user-msg').html(msg);
			$('#alert-edit-user').show();
		},
		hideAlertEditUser: function() {
			$('#alert-edit-user-msg').html('');
			$('#alert-edit-user').hide();
		},
		init: function() {
			$('#alert-edit-user').hide();
			var that = this;
			$('#formEditUser').bind('submit', function (e) {
				e.preventDefault();
				var fname = $('#formeditfirstname').val();
				var lname = $('#formeditlastname').val();
				var password = $('#formeditpassworduser').val();
				var phone = $('#formeditphoneuser').val();
				that.submit({
					'fname': fname,
					'lname': lname,
					'pass': password,
					'phone': phone
				});
			});
		}
	};

	profile.init();
})(window, document, jQuery);