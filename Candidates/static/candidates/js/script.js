$(document).ready(function() {
	var $analytics_range = $(".js-analytics-range-slider"),
	instance,
	min = 0,
	max = 60,
	from = 0,
	to = 0;
  
  $analytics_range.ionRangeSlider({
	skin: "round",
	type: "double",
	min: min,
	max: max,
	from: ana_min,
	to: ana_max,
  });
  instance = $analytics_range.data("ionRangeSlider");
  
  var $prof_range = $(".js-professional-range-slider"),
	instance,
	min = 0,
	max = 120,
	from = 0,
	to = 0;
  
  $prof_range.ionRangeSlider({
	skin: "round",
	type: "double",
	min: min,
	max: max,
	from: prof_min,
	to: prof_max,
  });

  $('#memberModal').modal('show');

  instance = $prof_range.data("ionRangeSlider");

  window.onload = function() {
	var patt = /id_\w+_\d+/g;
	var match = id_list.match(patt);

  	for(var i in match){
		  this.console.log(match[i])
		  document.getElementById(match[i]).checked = true;
	  };
	};
});