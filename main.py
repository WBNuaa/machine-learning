import similarity as si
import translate as tr

#语种
#法语 fra
#西班牙语 spa
#日语 jp
#俄语 ru
#韩语 kor
#德语 de
#英语 en
#中文 zh
language = ['zh','en','fra','spa','jp','ru','kor','de']

def transform(content,sourse,destination):#蜕变关系
    return

def translate(content,sourse,destination):#翻译
    return

def analyse():#结果对比分析
    return 

if __name__ =='__main__':
    content = "我喜欢你"
    sourse = 'zh'
    destination = 'en'
    tr.translate_baidu(content,sourse,destination)
    tr.translate_youdao(content,sourse,destination)
    tr.translate_google(content,sourse,destination)

