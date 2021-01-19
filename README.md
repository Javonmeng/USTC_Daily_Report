一个很简陋的依靠github action的每天USTC自动健康打卡脚本，并把打卡结果通过server酱推送到微信。

fork后需要在settings创建STUDENT_ID,PWD_KEY,SCKEY三个secrets key，STUDENT_ID即学号，PWD_KEY为统一身份认证密码，SCKEY为server酱的SCKEY。

获取server酱的SCKEY的具体方法见http://sc.ftqq.com/3.version

每日上报的数据在report_info.py的report_post_data中，目前是打卡在西区，其他数据一切正常。若要修改打卡内容，可以先在浏览器手动健康上报(https://weixine.ustc.edu.cn/2020/ ),F12可以看到post form data，将其覆盖report_info.py代码中的report_post_data即可。(请注意保留_token为空，_token与打卡内容无关)
