$(function () {

    let $username = $('#registname');
    let $register = $('.form-contain');  // 获取注册表单元素

    $username.blur(function () {
        fn_check_username();
    });

    function fn_check_username() {
        let sUsername = $username.val();  // 获取用户名字符串


        // 发送ajax请求，去后端查询用户名是否存在
        $.ajax({
            url: '/username/' + sUsername + '/',
            type: 'GET',
            dataType: 'json',
        })
            .done(function (res) {
                if (res.data.count !== 0) {
                    message.showError(res.data.username + '已注册，请重新输入！')
                } else {
                    message.showInfo(res.data.username + '能正常使用！')
                }
            })
            .fail(function () {
                message.showError('服务器超时，请重试！');
            });
    }

    $register.submit(function (e) {
        // 阻止默认提交操作
        e.preventDefault();

        // 获取用户输入的内容
        let sUsername = $username.val();  // 获取用户输入的用户名字符串
        let sPassword = $("input[name=registpassword]").val();
        let sPasswordRepeat = $("input[name=reregistpassword]").val();

        // 判断用户名是否已注册
        if (fn_check_username() !== "success") {
            return
        }

        // 判断用户输入的密码是否为空
        if ((!sPassword) || (!sPasswordRepeat)) {
            message.showError('密码或确认密码不能为空');
            return
        }

        // 判断用户输入的密码和确认密码长度是否为3-20位
        if ((sPassword.length < 3 || sPassword.length > 20) ||
            (sPasswordRepeat.length < 3 || sPasswordRepeat.length > 20)) {
            message.showError('密码和确认密码的长度需在6～20位以内');
            return
        }

        // 判断用户输入的密码和确认密码是否一致
        if (sPassword !== sPasswordRepeat) {
            message.showError('密码和确认密码不一致');
            return
        }


        // 发起注册请求
        // 1、创建请求参数
        let SdataParams = {
            "username": sUsername,
            "password": sPassword,
            "password_repeat": sPasswordRepeat,
        };

        // 2、创建ajax请求
        $.ajax({
            // 请求地址
            url: "register/",  // url尾部需要添加/
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
                    message.showSuccess('恭喜你，注册成功！');
                    setTimeout(function () {
                        // 注册成功之后重定向到主页
                        window.location.href = document.referrer;
                    }, 1000)
                } else {
                    // 注册失败，打印错误信息
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
     * 3. 输入框得到焦点隐藏错误信息
     */
    $(".inputClass").focus(function () {
        var labelId = $(this).attr("id") + "Error";//通过输入框找到对应的label的id
        $("#" + labelId).text("");//把label的内容清空！
        showError($("#" + labelId));//隐藏没有信息的label（同时也把前面的红色x隐藏
    });

    /*
     * 4. 输入框失去焦点进行校验
     */
    $(".inputClass").blur(function () {
        var id = $(this).attr("id");//获取当前输入框的id
        var funName = "validate" + id.substring(0, 1).toUpperCase() + id.substring(1) + "()";//得到对应的校验函数名
        eval(funName);//执行函数调用


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
        if (!value) {
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
        if (value.length < 3 || value.length > 20) {
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
        if (!value) {
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
        if (value != $("#registpassword").val()) {
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





});
