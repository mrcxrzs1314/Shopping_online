$(function() {
	/*
	 * 1. 得到所有的错误信息，循环遍历之。调用一个方法来确定是否显示错误信息！
	 */
	$(".errorClass").each(function() {
		showError($(this));//遍历每个元素，使用每个元素来调用showError方法
	});


	/*
	 * 3. 输入框得到焦点隐藏错误信息
	 */
	$(".inputClass").focus(function() {
		var labelId = $(this).attr("id") + "Error";//通过输入框找到对应的label的id
		$("#" + labelId).text("");//把label的内容清空！
		showError($("#" + labelId));//隐藏没有信息的label（同时也把前面的红色x隐藏
	});

	/*
	 * 4. 输入框失去焦点进行校验
	 */
	$(".inputClass").blur(function() {
		var id = $(this).attr("id");//获取当前输入框的id
		var funName = "validate" + id.substring(0,1).toUpperCase() + id.substring(1) + "()";//得到对应的校验函数名
		eval(funName);//执行函数调用
	});

});

/*
 * 登录名校验方法
 */
function validateRegistname() {
    var id = "registname";
    var value = $("#" + id).val();//获取输入框内容
    /*
     * 1. 非空校验
     */
    if (!value) {
        /*
         * 获取对应的label
         * 添加错误信息
         * 显示label
         */
        $("#" + id + "Error").text("用户名不能为空！");
        showError($("#" + id + "Error"));
        return false;
    }
    /*
     * 2. 长度校验
     */
    if (value.length < 3 || value.length > 20) {
        /*
         * 获取对应的label
         * 添加错误信息
         * 显示label
         */
        $("#" + id + "Error").text("用户名长度必须在3 ~ 20之间！");
        showError($("#" + id + "Error"));
        return false;
    }
    return true;
}

/*
 * 登录密码校验方法
 */
function validateRegistpassword() {
	var id = "registpassword";
	var value = $("#" + id).val();//获取输入框内容
	/*
	 * 1. 非空校验
	 */
	if(!value) {
		/*
		 * 获取对应的label
		 * 添加错误信息
		 * 显示label
		 */
		$("#" + id + "Error").text("密码不能为空！");
		showError($("#" + id + "Error"));
		return false;
	}
	/*
	 * 2. 长度校验
	 */
	if(value.length < 3 || value.length > 20) {
		/*
		 * 获取对应的label
		 * 添加错误信息
		 * 显示label
		 */
		$("#" + id + "Error").text("密码长度必须在3 ~ 20之间！");
		showError($("#" + id + "Error"));
		false;
	}
	return true;
}

/*
 * 确认密码校验方法
 */
function validateReregistpassword() {
	var id = "reregistpassword";
	var value = $("#" + id).val();//获取输入框内容
	/*
	 * 1. 非空校验
	 */
	if(!value) {
		/*
		 * 获取对应的label
		 * 添加错误信息
		 * 显示label
		 */
		$("#" + id + "Error").text("确认密码不能为空！");
		showError($("#" + id + "Error"));
		return false;
	}
	/*
	 * 2. 两次输入是否一致校验
	 */
	if(value != $("#registpassword").val()) {
		/*
		 * 获取对应的label
		 * 添加错误信息
		 * 显示label
		 */
		$("#" + id + "Error").text("两次输入不一致！");
		showError($("#" + id + "Error"));
		return false;
	}
	return true;
}


/*
 * 判断当前元素是否存在内容，如果存在显示，不存在不显示！
 */
function showError(ele) {
    var text = ele.text();//获取元素的内容
    if (!text) {//如果没有内容
        ele.css("display", "none");//隐藏元素
    } else {//如果有内容
        ele.css("display", "");//显示元素
    }
}

