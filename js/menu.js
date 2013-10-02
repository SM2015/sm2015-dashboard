(function (window, document, $) {

	$(document).ready(function () {

		$('#menuenglish').bind('click', function(e) {
			e.preventDefault();

			$.ajax({
				'type': 'GET',
				'data': {
					'lang': 'eng'
				},
				'url': 'php/setLang.php',
				success: function(data) {
					window.location.reload();
				},
				complete: function(data) {
					window.location.reload();
				}
			});
		});

		$('#menuspanish').bind('click', function(e) {
			e.preventDefault();
			$.ajax({
				'type': 'GET',
				'data': {
					'lang': 'es'
				},
				'url': 'php/setLang.php',
				success: function(data) {
					//if (data.msg && data.msg == 'success') {
						window.location.reload();
					//}
				},
				complete: function (data) {
					
						window.location.reload();
					
				}
			});
		});
	});

})(window, document, jQuery);