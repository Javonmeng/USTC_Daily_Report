import os
import requests
import report_info
if __name__=='__main__':
    id = os.environ["STUDENT_ID"]
    password = str(os.environ["PWD"])
    server_key= os.environ["SCKEY"]
    

    sess,my_token=report_info.login(id,password)

    info_name,info_success,info_time=report_info.report(sess,my_token)
    scurl='https://sc.ftqq.com/'+server_key+'.send'
    title=info_name+'('+STUDENT_ID+')'+'今日成功打卡'
    content=f"""
    '{info_success}';
    '{info_time}。
    """

    print(content)
    data={
        'text':title,
        'desp':content
    }
    print(scurl)

    try:
        req = requests.post(scurl, data=data)
        if req.json()["errmsg"] == 'success':
            print("Server酱推送服务成功")
        else:
            print("Server酱推送服务失败")
    except:
        print("微信推送参数错误")


