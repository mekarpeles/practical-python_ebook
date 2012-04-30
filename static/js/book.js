$(function () {
    $(document).keydown(function (evt) {
	if (evt.keyCode == 37) { // left arrow
	    parent.location="http://127.0.0.1:8080/practical-python/chapters/1"
	} else if (evt.keyCode == 39) { // right arrow
	    parent.location="http://127.0.0.1:8080/practical-python/chapters/2"
	}
    });
});