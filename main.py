import similarity as si
import translate as tr
import time
#语种

##俄语 ru
#希腊语 el
##英语 en
##中文 zh
##波兰语 pl
##葡萄牙语 pt
##泰语 th
##德语 de

language = ['zh','en','ru','el','pl','pt','th','de']
software = ['baidu','youdao','google']

def sample(sourse,destination,layer):
    #测试用例生成（语种的选择）
    info = {}
    case = []   #蜕变语种
    result1 = []
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
                info1 = {}
                info1['first'] = temp1_1
                case.append(info1)
        for i in range(len(case)):
            first = case[i]['first']
            result1.append([first])
        
#language = ['zh','en','ru','el','pl','pt','th','de']
    elif info['layer'] == 2:
        # for i in range(info[layer]):
           
            for j in range(len(language)):

                if language[j] != info['destination'] and language[j] != info['sourse']:
                    temp2_1 = language[j]
                    for k in range(len(language)):
                        if language[k] != info['destination'] and language[k] != info['sourse'] and language[k] != temp2_1:
                            temp2_2 = language[k]
                            info1 = {} 
                            info1['first'] = temp2_1
                            info1['second'] = temp2_2
                            case.append(info1)
            for i in range(len(case)):
                first = case[i]['first']
                second = case[i]['second']
                result1.append([first,second])

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
                                    info1 = {}
                                    info1['first'] = temp3_1
                                    info1['second'] = temp3_2
                                    info1['third'] = temp3_3
                                    case.append(info1)
            for i in range(len(case)):
                first = case[i]['first']
                second = case[i]['second']
                third = case[i]['third']
                result1.append([first,second,third])

    else:
        print("蜕变层数错误请重新检查!")


    #print(list)
    return result1

#蜕变关系
def transform(content,target,sourse,destination,transform_relationship,layer):
    translateresult = []#存放翻译的结果
    result = translate(content,sourse,destination,target)
    translateresult.append(result)

    result = sample(sourse,destination,layer)#获取蜕变测试用例
    #翻译
    print(result)

    for tmp in result:
        #将字典转化为列表
        print(tmp[0])
        #翻译成中间语言
        content_m = translate(content,sourse,tmp[0],transform_relationship)
        print(content_m)
        i = 0
        for i in range(1,len(tmp)):
            content_m = translate(content_m,tmp[i-1],tmp[i],transform_relationship)
        #翻译成目标语言
        content_m = translate(content_m,tmp[i],destination,target)
        translateresult.append(content_m)

    print(translateresult)
    return translateresult

#翻译
def translate(content,sourse,destination,tool):
    if tool == 'baidu':
        result = tr.translate_baidu(content,sourse,destination)
        time.sleep(1)#降低访问频率
    elif tool == 'youdao':
        result = tr.translate_youdao(content,sourse,destination)
    else:
        result = tr.translate_google(content,sourse,destination)
    return result

#调用蜕变关系进行翻译，而后进行结果对比
def analyse(content,target,sourse,destination,transform_relationship,layer):#结果对比分析
    result = transform(content,target,sourse,destination,transform_relationship,layer)
    for i in range(1,len(result)):
        print("第%d个测试用例:"%i)
        si.callfunction(result[0],result[i])
    return 

#读取文件测试用例
def example(path):
    fo = open(path,"r+",encoding='utf-8')
    test = []
    while 1:
      line = fo.readline()
      if not line:
           break
      else:
          #sample(list[2],list[3],list[5])
          line = line.strip('\n')
          test.append(line)
    fo.close()
    return test


if __name__ =='__main__':
    sourse = 'zh' #源语言
    destination = 'en' #目标语言
    target = 'baidu' #测试系统
    transform_relationship = 'google' #蜕变关系
    layer = 1 #蜕变层数
    #transform(content,target,sourse,destination,transform_relationship,layer)
    #print(content)
    flag = 1
    if flag == 1:#用户直接输入翻译内容
        content = '我喜欢你' #翻译内容
        analyse(content,target,sourse,destination,transform_relationship,layer)
    elif flag == 2:#用户输入文件
        path = 'example.txt'
        test = example(path)
    #print(sample)
        for i in range(len(test)):
            print(test[i])
            content = test[i]
            analyse(content,target,sourse,destination,transform_relationship,layer)