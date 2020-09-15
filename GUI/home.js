$(document).ready(function(){
	$("#open1").hide();
	$("#open2").hide();
	$("#open3").hide();
	let open_moved = false;
	$("#open").click(function(){
		if(open_moved){
			$("#open1, #open2, #open3").animate({
				bottom: "10px"
			},200);
			setTimeout(function(){
				$("#open1, #open2, #open3").hide()
			},500);
		}else{
			$("#open1, #open2, #open3").show();
			$("#open1").animate({
				bottom: "75px"
			});
			$("#open2").animate({
				bottom: "140px"
			});
			$("#open3").animate({
				bottom: "205px"
			});
		}
		open_moved = !open_moved;
	});
	$("#open1").mouseenter(function(){
		$("#open1").removeClass("btn-floating");
		$("#open1").addClass("btn");
	});
	$("#open1").mouseleave(function(){
		$("#open1").addClass("btn-floating");
		$("#open1").removeClass("btn");
	});
	$("#open2").mouseenter(function(){
		$("#open2").removeClass("btn-floating");
		$("#open2").addClass("btn");
	});
	$("#open2").mouseleave(function(){
		$("#open2").addClass("btn-floating");
		$("#open2").removeClass("btn");
	});
	$("#open3").mouseenter(function(){
		$("#open3").removeClass("btn-floating");
		$("#open3").addClass("btn");
	});
	$("#open3").mouseleave(function(){
		$("#open3").addClass("btn-floating");
		$("#open3").removeClass("btn");
	});
});
