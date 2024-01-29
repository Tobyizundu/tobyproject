//Decalring the Function
    $(document).ready(function() {
			$('input[type="radio"]').click(function() {
				// uncheck all other radio buttons
				$('input[type="radio"]').not(this).prop('checked', false);
			});
		});





