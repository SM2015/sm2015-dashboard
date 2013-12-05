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

		$('#menucountry > li').bind('click', function(e) {
			e.preventDefault();
			var pais = $(this).attr('id').replace('menu', '');
			$.ajax({
				'type': 'GET',
				'data': {
					'country': pais
				},
				'url': 'php/setCountry.php',
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