# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:24:57 2020

将zhwiki词条索引进行繁简转化后作为字典用于jieba分词
@author: zhangwz
"""
from opencc import OpenCC
import logging
import datetime

zhwikiIndexFile = './zhwiki-20200201-pages-articles-multistream-index.txt' #词条索引文件
segDictFile = './segDict.txt' #词典

def buildSegDict():
    cc = OpenCC('t2s')  # convert from Traditional Chinese to Simplified Chinese
    with open(zhwikiIndexFile, encoding='utf-8') as fr:
        for line in fr:
            #to_convert = '香菸（英語：Cigarette），爲菸草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。'
            converted = cc.convert(line)
            print(converted)
            conArr = converted.split(':')
            if(len(conArr) > 3):
                pass
            else:
                entity = conArr[2]
                with open(segDictFile, 'a', encoding='utf-8') as fw:
                    fw.write(entity)

if __name__ == '__main__':
    program = "cleanZhwiki.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    buildSegDict()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
