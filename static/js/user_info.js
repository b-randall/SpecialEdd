var user_info = (function () {

var exports = {};

exports.show_avatar = function(){
	// retrieveds information about the user and passes it to the user-info
	// handlbar
	var user_avatar = page_params.avatar_url;
	var template = templates.render("user-info", {user_avatar: user_avatar,
												  name: name});
	var $avatar = $("#user_avatar");

	 $avatar.append(template);
};

$(function () {
    exports.show_avatar();
});


return exports;

}());
