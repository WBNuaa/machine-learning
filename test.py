import requests  
import string  
import time  
import hashlib  
import json 
import re 
import numpy as np  
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"  
my_appid = '20210113000670420'  #你的APP ID
cyber = 'UK9njd0CMJn7xNPbzLT4'  #你的秘钥
lower_case = list(string.ascii_lowercase)  
  
def requests_for_dst(word,sourse,des):  
    #init salt and final_sign  
    salt = str(time.time())[:10]  
    final_sign = str(my_appid)+word+salt+cyber  
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()  
    #区别en,zh构造请求参数  
    paramas = {  
            'q':word,  
            'from':sourse,  # 源语言
            'to':des,   # 目标语言
            'appid':'%s'%my_appid,  
            'salt':'%s'%salt,  
            'sign':'%s'%final_sign  
            }  #翻译请求参数
    #my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'en'+'&to='+'spa'+'&salt='+salt+'&sign='+final_sign
    response = requests.get(api_url,params = paramas).content  
    content = str(response,encoding = "utf-8")  
    json_reads = json.loads(content)
    print(json_reads['trans_result'][0]['dst']) 
    return json_reads['trans_result'][0]['dst']

content = '我喜欢你'
source = 'zh'
des = 'en'
requests_for_dst(content,source,des)
time.sleep(1)
requests_for_dst(content,source,des)

