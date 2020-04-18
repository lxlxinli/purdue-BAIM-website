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
	from: 0,
	to: 60,
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
	from: 0,
	to: 120,
  });
  instance = $prof_range.data("ionRangeSlider");
});