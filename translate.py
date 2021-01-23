import urllib.request
import urllib.parse
import json
import hashlib
import random
import time
import uuid
import requests
from google_trans_new import google_translator

# 百度翻译 需要降低访问频率 也即time.sleep(1)
def translate_baidu(content,sourse,destination):
    URL='http://api.fanyi.baidu.com/api/trans/vip/translate'
    From_Data={}  #创建From_Data字典，存储向服务器发送的data
    From_Data['from']=sourse #输入的语种
    From_Data['to']=destination #翻译的语种
    From_Data['q']=content     #要翻译的数据
    From_Data['appid']='20210113000670420'       #申请的APPID
    From_Data['salt']=str(random.randint(32768,65536))        #随机数
    Key='UK9njd0CMJn7xNPbzLT4'                    #平台分配的密匙
    m=From_Data['appid']+content+From_Data['salt']+Key
    m_MD5=hashlib.md5(m.encode("utf-8"))
    From_Data['sign']=m_MD5.hexdigest()
    #print(From_Data)
    data=urllib.parse.urlencode(From_Data).encode('utf-8')  #使用urlencode()方法转换标准格式
    response=urllib.request.urlopen(URL,data)            #传递request对象和转换完格式的数据
    html=response.read().decode('utf-8')          #读取信息并解码
    translate_results=json.loads(html)            #使用JSON
    #print(translate_results)                      #打印出JSON数据
    translate_results=translate_results['trans_result'][0]['dst']   #找到翻译结果
    #print('翻译的结果是: %s'%translate_results)               #打印翻译信息
    return translate_results

#有道翻译
def translate_youdao(content,source,destination):
    youdao_url = 'https://openapi.youdao.com/api' #有道api地址
    input_text = ""# 翻译文本生成sign前进行的处理
    # 当文本长度小于等于20时，取文本
    if(len(content) <= 20):
        input_text = content
    # 当文本长度大于20时，进行特殊处理
    elif(len(content) > 20):
        input_text = content[:10] + str(len(content)) + content[-10:]
    time_curtime = int(time.time())   # 秒级时间戳获取
    app_id = "7874d9822da0ca7a"   # 应用id
    uu_id = uuid.uuid4()   # 随机生成的uuid数，为了每次都生成一个不重复的数。
    app_key = "6eQByh9agdMfG4yqwrQyJQEqN412KXDB"   # 应用密钥
    sign = hashlib.sha256((app_id + input_text + str(uu_id) + str(time_curtime) + app_key).encode('utf-8')).hexdigest()   # sign生成
    data = {
        'q':content,   # 翻译文本
        'from':source,   # 源语言
        'to':destination,   # 翻译语言
        'appKey':app_id,   # 应用id
        'salt':uu_id,   # 随机生产的uuid码
        'sign':sign,   # 签名
        'signType':"v3",   # 签名类型，固定值
        'curtime':time_curtime,   # 秒级时间戳
    }
    r = requests.get(youdao_url, params = data).json()   # 获取返回的json()内容
    #print("翻译后的结果：" + r["translation"][0])   # 获取翻译内容
    return r["translation"][0]

#谷歌翻译
def translate_google(content,sourse,destination):
    translator = google_translator()
    From_Data={}  #创建From_Data字典，存储向服务器发送的data
    From_Data['from']=sourse #输入的语种
    From_Data['to']=destination #翻译的语种
    text = translator.translate(content,lang_src=From_Data['from'],lang_tgt=From_Data['to'])
    #print(text)
    return text



if __name__ == '__main__':
    content = "我喜欢你" #翻译内容
    sourse = 'zh' #源语言
    destination = 'pl' #目标语言
    translate_google(content,sourse,destination)
    translate_youdao(content,sourse,destination)
    translate_baidu(content,sourse,destination)
    #destination = 'ru'
    #translate_google(content,sourse,destination)
    #translate_youdao(content,sourse,destination)
    #time.sleep(1)
    #translate_baidu(content,sourse,destination)






