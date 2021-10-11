#encoding:utf-8

from gensim import corpora

corpus = [

          'This is the first document.',
          'This is the second second document.',
          'And the third one.',
          'Is this the first document?'
]
#1.分词处理
word_list = []
for i in range(len(corpus)):
    word_list.append(corpus[i].split(''))
print(word_list)
#2.得到每个词的id值及词频
#赋给语料库的每个词（不重复的词）一个整数id
dictionary = corpora.Dictionary(word_list)
new_corpus = [dictionary.doc2bow(text) for text in word_list]
print(new_corpus)
#元组中第一个元素是词语在词典中对应的id，第二个元素是词语在玩当中出现的次数
#通过下面的方法可以看到语料库中每个词对应的id
print(dictionary.token2id)
#3.训练gensim模型并且保存它以便后面的使用
#训练模型并保存
from gensim import models
tfidf = models.TfidModel(new_corpus)
tfidf.save("my_model.tfidf")

#载入模型
tfidf  = models.TfidfModel.load("my_model.tfidf")

#使用这个训练好的模型得到的单词的tfidf值
tfidf_vec = []
for i in range(len(corpus)):
    string = corpus[i]
    string_bow = dictionary.doc2bow(string.lower().split())
    string_tfidf = tfidf[string_bow]
    tfidf_vec.append(string_tfidf)
print(tfidf_vec)
#测试
string = 'the i first second name'

sting_bow = dictionary.doc2bow(string.lower().split())
string_tfidf = tfidf[string_bow]

print(string_tfidf)

"""
gensim训练出来的tf-idf值左边是词的id，右边是词的tfidf值
gensim有自动去除停用词的功能，比如the
gensim会自动去除单个字母，比如i
gensim会去除没有被训练到的词，比如name
所以通过gensim并不能计算每个单词的tfidf值
"""




