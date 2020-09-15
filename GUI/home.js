$(document).ready(function(){
	$("#open1").hide();
	$("#open2").hide();
	$("#open3").hide();
	let open_moved = false;
	$("#open").click(function(){
		if(open_moved){
			$("#open1, #open2, #open3").animate({
				left: "10px"
			}).hide();
		}else{
			$("#open1, #open2, #open3").show();
			$("#open1").animate({
				left: "75px"
			});
			$("#open2").animate({
				left: "140px"
			});
			$("#open3").animate({
				left: "205px"
			});
		}
		open_moved = !open_moved;
	});
});
