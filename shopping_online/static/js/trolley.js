
        $(function () {
            showSmallTotal();
            showTotal();

            /*
             给全选添加click事件
             */
            $("#selectAll").click(function () {
                /*
                 1. 获取全选的状态
                 */
                var bool = $("#selectAll").is(":checked");
                /*
                 2. 让所有条目的复选框与全选的状态同步
                 */
                setItemCheckBox(bool);
                /*
                 3. 让结算按钮与全选同步
                 */
                setJieSuan(bool);
                /*
                 4. 重新计算总计
                 */
                showTotal();
            });


            /*
             给减号添加click事件
             */
            $(".jian").click(function () {
                var quantity = $("#Quantity").val();
                // 判断当前数量是否为1，如果为1,那就不是修改数量了，而是要删除了。
                if (quantity == 1) {
                    alert("删除此条记录")
                }
                else {
                    $("#Quantity").val(Number(quantity) - 1);
                }
                showSmallTotal();
                showTotal();
            });

            // 给加号添加click事件
            $(".jia").click(function () {
                var quantity = $("#Quantity").val();
                $("#Quantity").val(Number(quantity) + 1);
                showSmallTotal();
                showTotal();

            });
            /*
             给所有条目的复选框添加click事件
             */
            $(":checkbox[name=checkboxBtn]").click(function () {
                var all = $(":checkbox[name=checkboxBtn]").length;//所有条目的个数
                var select = $(":checkbox[name=checkboxBtn]:checked").length;//获取所有被选择条目的个数
                if (all == select) {//全都选中了
                    $("#selectAll").prop("checked", true);//勾选全选复选框
                    setJieSuan(true);//让结算按钮有效
                } else if (select == 0) {//谁都没有选中
                    $("#selectAll").prop("checked", false);//取消全选
                    setJieSuan(false);//让结算失效
                } else {
                    $("#selectAll").prop("checked", false);//取消全选
                    setJieSuan(true);//让结算有效
                }
                showTotal();//重新计算总计
            });


        });
        /*计算小计*/
        function showSmallTotal() {
            var quantity = $("#Quantity").val();
            var danjia = $("#danjia").text();
            var sum = quantity * danjia;
            $("#Subtotal").text(round(sum, 2));

        }
        /*
         * 计算总计
         */
        function showTotal() {
            var total = 0;
            /*
             1. 获取所有的被勾选的条目复选框！循环遍历之
             */
            $(":checkbox[name=checkboxBtn]:checked").each(function () {
                //2. 找到小计元素，获取其文本
                var text = $("#Subtotal").text();
                //3. 累加计算
                total += Number(text);
            });
            // 4. 把总计显示在总计元素上
            $("#total").text(round(total, 2));//round()函数的作用是把total保留2位
        }

        /*
         * 统一设置所有条目的复选按钮
         */
        function setItemCheckBox(bool) {
            $(":checkbox[name=checkboxBtn]").prop("checked", bool);
        }


        /*
         * 设置结算按钮样式
         */
        function setJieSuan(bool) {
            if (bool) {
                $("#jiesuan").removeClass("kill").addClass("jiesuan");
                $("#jiesuan").unbind("click");//撤消当前元素止所有click事件
            } else {
                $("#jiesuan").removeClass("jiesuan").addClass("kill");
                $("#jiesuan").click(function () {
                    return false;
                });
            }

        }
