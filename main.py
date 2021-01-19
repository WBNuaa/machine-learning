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

def sample():
    #测试用例生成（语种的选择）
    return 

#蜕变关系
def transform(content,sourse,destination,relationship):
    return

def translate(content,sourse,destination,tool):#翻译
    if tool == 'baidu':
        result = tr.translate_baidu(content,sourse,destination)
    elif tool == 'youdao':
        result = tr.translate_youdao(content,sourse,destination)
    else:
        result = tr.translate_google(content,sourse,destination)
    return result

def analyse():#结果对比分析
    return 

if __name__ =='__main__':
    content = "我喜欢你" #翻译内容
    sourse = 'zh' #源语言
    destination = 'en' #目标语言
    target = 'baidu' #测试系统
    transform_relationship = 'baidu' #蜕变关系
    layer = 2 #蜕变层数

