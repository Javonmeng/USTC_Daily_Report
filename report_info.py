import requests
from lxml import etree

login_url='https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin'
report_url='https://weixine.ustc.edu.cn/2020/daliy_report'
header={
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
login_post_data = {
    'model': 'uplogin.jsp',
    'service': 'https://weixine.ustc.edu.cn/2020/caslogin',
    'warn':'',
    'showCode':'',
    'username': '',
    'password': '',
    'button':''
}
report_post_data = {
    '_token' : '',
    'now_address' : '1',
    'gps_now_address' : '',
    'now_province' : '340000',
    'gps_province' : '',
    'now_city' : '340100',
    'gps_city' : '',
    'now_detail' : '',
    'is_inschool' : '0',
    'body_condition' : '1',
    'body_condition_detail' :'',
    'now_status' : '2',
    'now_status_detail' : '',
    'has_fever' : '0',
    'last_touch_sars' : '0',
    'last_touch_sars_date' : '',
    'last_touch_sars_detail' : '',
    'other_detail' : ''
}
sess = requests.Session()
def login(STUDENT_ID,PWD):
    login_post_data['username']=STUDENT_ID
    login_post_data['password']=PWD
    r=sess.post(url=login_url,headers=header,data=login_post_data)
    if(r.status_code==200):
        html = r.text
        doc = etree.HTML(html)
        #提取input标签中名为auth的值
        #auth = html.xpath('//input[@name="auth"]/@value')
        # 提取_token值
        print(html)
        #print(doc.xpath('//input'))
        #info_name=doc.xpath('//input[@name="name"]/@value')[0]
        #print("111",info_name)
        my_token=doc.xpath('//input[@name="_token"]/@value')[0]
    return sess,my_token

def report(sess,my_token):
    report_post_data['_token']=my_token
    r=sess.post(url=report_url,headers=header,data=report_post_data)
    html = r.text
    doc = etree.HTML(html)


    info_name=doc.xpath('//input[@name="name"]/@value')[0]
    #print(info_name)

    info=doc.xpath('//p[@class="alert alert-success"]')
    info_success=info[0].xpath('string(.)').strip()
    info_success=info_success[:-2]

    info=doc.xpath('//strong')
    info_time=info[1].xpath('string(.)').strip()
    info_time=info_time[3:]
    return info_name,info_success,info_time

if __name__ == "__main__":
    # Test
    sess,my_token=login('SA18006111','11111')
    info_success,info_time=report(sess,my_token)
    print(info_success,info_time)
