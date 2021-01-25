import distance
import re

#数据预处理，按空格分割字符串
def datafilter(content):
    #正则匹配
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    s = re.split(pattern, content)
    #除去空字符
    s = [x.strip() for x in s if x.strip()!='']
    return s
#距离
def jacc_distance(s1,s2):
    first = set(s1).intersection(set(s2))
    second = set(first).union(set(s2))
    return len(first)/len(second)
#print(jacc_distance(x,y))
#杰卡德系数计算
#用于比较样本之间的相似性与差异性，系数越大相似度越高
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
def add_space(s):
    return ' '.join(list(s))
def jacc_similarity(s1,s2):
    s1, s2 = add_space(s1), add_space(s2)#将字中间加入空格
    #转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda  s:s.split())
    corpus = [s1,s2]
    vectors = cv.fit_transform(corpus).toarray()
    #求交集
    numerator = np.sum(np.min(vectors, axis = 0))
    #求并集
    denominator = np.sum(np.max(vectors, axis = 0))
    #计算杰卡德系数
    return 1.0*numerator / denominator

#print(jacc_similarity(s1,s2))

#TF 计算TF矩阵中两个向量的相似度，实际上就是求解两个向量夹角的余弦值
    #就是点乘积以二者的模长，公式如下 cos = a*b/|a|*|b|

from scipy.linalg import norm
def tf_similarity(s1,s2):
    #将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    #转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda  s:s.split())
    corpus = [s1,s2]
    vectors = cv.fit_transform(corpus).toarray()
    #计算TF系数
    return np.dot(vectors[0],vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))

#print(tf_similarity(s1,s2))

#TFIDF 在词频TF的基础上再加入IDF的信息，IDF称为逆文档频率
from sklearn.feature_extraction.text import TfidfVectorizer
def tfidf_similarity(s1,s2):
    #加入空格
    s1, s2 =add_space(s1), add_space(s2)
    #转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda  s:s.split())
    corpus = [s1,s2]
    vectors = cv.fit_transform(corpus).toarray()
    #计算TFIDF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
#print(tfidf_similarity(s1,s2))

def callfunction(s1,s2):
    info = {}
    s1 = datafilter(s1)
    s2 = datafilter(s2)
    #print(s1)
    #print(s2)
    x = set(list(s1))
    y = set(list(s2))
    dis = jacc_distance(x,y)
    #print("向量距离:%f"%dis)
    info['向量距离'] = dis
    jacc = jacc_similarity(s1,s2)
    #print("杰卡德系数:%f"%jacc)
    info["杰卡德系数"] = jacc
    tf = tf_similarity(s1,s2)
    #print("TF:%f"%tf)
    info['TF'] = tf
    tfdf = tfidf_similarity(s1,s2)
    #print("TFDF:%f"%tfdf)
    info['TFDF'] = tfdf
    if (dis>=0.95 and jacc>=0.95 and tf>=0.95 and tfdf >=0.95):
        result = '测试通过'.
    else:
        result = '测试不通过'
    info['结果'] = result
    print(info)
    return info
if __name__ == '__main__':
    s1 = 'I love you, too.'
    s2 = 'I like you too!'
    callfunction(s1,s2)
