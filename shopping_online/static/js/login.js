$(function () {

    let $login = $('.form-contain');  // 获取登录表单元素

    // 登录逻辑
    $login.submit(function (e) {
        // 阻止默认提交操作
        e.preventDefault();

        // 获取用户输入的账号信息
        let sUserAccount = $("input[name=loginname]").val();  // 获取用户输入的用户名
        // 判断用户输入的账号信息是否为空
        if (sUserAccount === "") {
            message.showError('用户账号不能为空');
            return
        }
        // 获取用户输入的密码
        let sPassword = $("input[name=loginpassword]").val();  // 获取用户输入的密码
        // 判断用户输入的密码是否为空
        if (!sPassword) {
            message.showError('密码不能为空');
            return
        }
        // 判断用户输入的密码是否为3-20位
        if (sPassword.length < 3 || sPassword.length > 20) {
            message.showError('密码的长度需在3～20位以内');
            return
        }

        // 发起登录请求
        // 创建请求参数
        let SdataParams = {
            "user_account": sUserAccount,
            "password": sPassword,
        };

        // 创建ajax请求
        $.ajax({
            // 请求地址
            url: "/login/",
            // 请求方式
            type: "POST",
            data: JSON.stringify(SdataParams),
            // 请求内容的数据类型（前端发给后端的格式）
            contentType: "application/json; charset=utf-8",
            // 响应数据的格式（后端返回给前端的格式）
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "0") {
                    // 注册成功
                    message.showSuccess('恭喜你，登录成功！');
                    setTimeout(function () {
                        // 注册成功之后重定向到打开登录页面之前的页面
                        window.location.href = document.referrer;
                    }, 1000)
                } else {
                    // 登录失败，打印错误信息
                    message.showError(res.errmsg);
                }
            })
            .fail(function () {
                message.showError('服务器超时，请重试！');
            });
    });

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








