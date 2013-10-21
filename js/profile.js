(function (window, document, $) {
	var profile = {
		submit: function(opt) {
			services.profileRequest({
				type: 'POST',
				data: opt,
				success: function(data) {
					if (data.error.length > 0) {
						console.log('error');
					} else {
						console.log('success');
					}
				},
				error: function() {

				}
			});
		},
		init: function() {
			var that = this;
			$('#formEditUser').bind('submit', function (e) {
				e.preventDefault();
				var fname = $('#formeditfirstname').val();
				var lname = $('#formeditlastname').val();
				var password = $('#formeditemailuser').val();
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