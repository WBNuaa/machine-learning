import similarity as si
import translate as tr

#语种

##俄语 ru
#希腊语 el
##英语 en
##中文 zh
##苗语 hmn
##葡萄牙语 pt
##泰语 th
##德语 de

language = ['zh','en','ru','el','hmn','pt','th','de']
software = ['baidu','youdao','google']

def sample(sourse,destination,layer):
    #测试用例生成（语种的选择）
    info = {}
    list = []   #蜕变语种
    #info['target'] = target
    info['sourse'] = sourse
    info['destination'] = destination
    #info['transform_relationship'] = transform_relationship
    info['layer'] = int(layer)
    #print(info)
    if info['layer'] == 1:
      # for i in range (info[layer]):
          for j in range(len(language)):
              
              if language[j] != info['sourse'] and language[j] != info['destination']:
                  temp1_1 = language[j]
                  list.append({temp1_1})

    elif info['layer'] == 2:
        # for i in range(info[layer]):
            for j in range(len(language)):

                if language[j] != info['destination'] and language[j] != info['sourse']:
                    temp2_1 = language[j]
                    for k in range(len(language)):
                        if language[k] != info['destination'] and language[k] != info['sourse'] and language[k] != temp2_1:
                            temp2_2 = language[k]
                            list.append({temp2_1,temp2_2})

    elif info['layer'] == 3:
        # for i in range(info[layer]):
            for j in range(len(language)):
                if language[j] != info['destination'] and language[j] != info['sourse']:
                    temp3_1 = language[j]
                    for k in range(len(language)):
                        if language[k] != info['destination'] and language[k] != info['sourse'] and language[k] != temp3_1:
                            temp3_2 = language[k]
                            for l in range(len(language)):
                                if language[l] != info['destination'] and language[l] != info['sourse'] and language[l] != temp3_1 and language[l] != temp3_2:
                                    temp3_3 = language[l]
                                    list.append({temp3_1,temp3_2,temp3_3})
    

    else:
        print("蜕变层数错误请重新检查!")


    #print(list)
    return list

#蜕变关系
def transform(content,target,sourse,destination,transform_relationship,layer):
    translateresult = []#存放翻译的结果
    result = translate(content,sourse,destination,target)
    translateresult.append(result)

    result = sample(sourse,destination,layer)#获取蜕变测试用例
    #翻译
    for tmp in result:
        #将字典转化为列表
        tmp = list(tmp)
        print(tmp[0])
        content_m = translate(content,sourse,tmp[0],transform_relationship)
        print(content_m)
        i = 0
        for i in range(1,len(tmp)):
            content_m = translate(content_m,tmp[i-1],tmp[i],transform_relationship)
        content_m = translate(content_m,tmp[i],destination,transform_relationship)
        translateresult.append(content_m)

    print(translateresult)
    return translateresult

#翻译
def translate(content,sourse,destination,tool):
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
    target = 'google' #测试系统
    transform_relationship = 'google' #蜕变关系
    layer = 2 #蜕变层数
    transform(content,target,sourse,destination,transform_relationship,layer)

