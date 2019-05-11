$(function () {

    /*
     * 1. 得到所有的错误信息，循环遍历之。调用一个方法来确定是否显示错误信息！
     */
    $(".errorClass").each(function () {
        showError($(this));//遍历每个元素，使用每个元素来调用showError方法
    });
    /*
     * 2. 输入框得到焦点时隐藏错误信息
     */
    $(".inputClass").focus(function () {
        var inputName = $(this).attr("name");
        $("#" + inputName + "Error").css("display", "none");
    });

    /*
     * 3. 输入框移动焦点时进行校验
     */
    $(".inputClass").blur(function () {
        var inputName = $(this).attr("name");
        invokeValidateFunction(inputName);
    })
});

/*
 * 输入input名称，调用对应的validate方法。
 * 例如input名称为：loginname，那么调用validateLoginname()方法。
 */
function invokeValidateFunction(inputName) {
    inputName = inputName.substring(0, 1).toUpperCase() + inputName.substring(1);
    var functionName = "validate" + inputName;
    return eval(functionName + "()");
}

/*
 * 校验登录名
 */
function validateLoginname() {
    var bool = true;
    $("#loginnameError").css("display", "none");
    var value = $("#loginname").val();
    if (!value) {// 非空校验
        $("#loginnameError").css("display", "");
        $("#loginnameError").text("用户名不能为空！");
        bool = false;
    } else if (value.length < 3 || value.length > 20) {//长度校验
        $("#loginnameError").css("display", "");
        $("#loginnameError").text("用户名长度必须在3 ~ 20之间！");
        bool = false;
    }
    return bool;
}

/*
 * 校验密码
 */
function validateLoginpassword() {
    var bool = true;
    $("#loginpasswordError").css("display", "none");
    var value = $("#loginpassword").val();
    if (!value) {// 非空校验
        $("#loginpasswordError").css("display", "");
        $("#loginpasswordError").text("密码不能为空！");
        bool = false;
    } else if (value.length < 3 || value.length > 20) {//长度校验
        $("#loginpasswordError").css("display", "");
        $("#loginpasswordError").text("密码长度必须在3 ~ 20之间！");
        bool = false;
    }
    return bool;
}


function showError(ele) {
    var text = ele.text();//获取元素的内容
    if (!text) {//如果没有内容
        ele.css("display", "none");//隐藏元素
    } else {//如果有内容
        ele.css("display", "");//显示元素
    }
}