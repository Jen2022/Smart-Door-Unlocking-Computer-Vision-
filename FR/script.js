$(function () {
	$(".content").click(function () {

		var value = $(this).find(".number").text();
		//alert(value)
		if (value !== "<" && value !=="GO") {
			$(".numberinput").each(function () {
				var a = $(this).text();
				
				if (!a) {
					$(this).text(value);
					$(this).addClass("nocircle");
					return false;
				}
			});
		}
		 if (value == "<") {
			$($(".numberinput").get().reverse()).each(function () {
				var a = $(this).text();
				if (a) {
					$(this).text("");
					$(this).removeClass("nocircle");
					return false;
				}
			});
		}

		if(value=="GO"){
		var otp=($(".numberinput").text());
		console.log(otp);
		window.location.replace("test.html");
		}
		

		// <?php
		 
		// $age=$_POST['age']; 
		// echo "<strong>".$nm." is $age years old.</strong>"; 
		// ?> 


	});

});