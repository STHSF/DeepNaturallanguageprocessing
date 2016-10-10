#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成词向量空间"""

from gensim.models import Word2Vec
import data_processing
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 生成word2vec模型
def word2vec_model(data, size, min_c):

    w2c_model = Word2Vec(size=size, min_count=min_c, workers=4)
    w2c_model.build_vocab(data)
    w2c_model.train(data)

    return w2c_model


def word2vec_test():

    # 读入数据
    pos_file_path = '/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test3.txt'
    neg_file_path = '/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test2.txt'
    tmp = data_processing.read_data(pos_file_path, neg_file_path)
    res = data_processing.data_split(tmp[0], tmp[1])
    x_train = res[0]
    x_train = data_processing.text_clean(x_train)
    n_dim = 200
    min_count = 2
    w2c_model = word2vec_model(x_train, n_dim, min_count)
    # res = w2c_model.most_similar(positive=['纤维', '批次'], negative=['成分'], topn=1)
    #
    # w2c_model.doesnt_match("我 爱 中国".split())
    #
    # var = w2c_model.similarity('纤维', '批次')
    # print var
    # res = w2c_model.most_similar("纤维")
    # for i in res:
    #     print i[0],
    dd = w2c_model.most_similar("批次")
    for i in dd:
        print i[0],

if __name__ == "__main__":
    word2vec_test()
    pos_file_path = '/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test3.txt'
    neg_file_path = '/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test2.txt'
    tmp = data_processing.read_data(pos_file_path, neg_file_path)
    res = data_processing.data_split(tmp[0], tmp[1])
    x_train = res[0]
    x_train = data_processing.text_clean(x_train)

    n_dim = 200
    min_count = 2
    model_path = '/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/word2vecmodel/mymodel'
    mymodel = word2vec_model(x_train, n_dim, min_count)
    mymodel.save(model_path)



