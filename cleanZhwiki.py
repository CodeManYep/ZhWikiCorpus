# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:55:05 2020

中文维基百科语料去掉<doc>标签和空行
@author: zhangwz
"""
import logging
import datetime

zhwikiFile = './zhwiki.txt'    #中文维基百科语料本文
zhwiki2File = './zhwiki2.txt' #中文维基百科数据最终版


triple = ''
def cleanZhwiki():
    i = 0       #用于每匹配到1000次输出一次，便于了解匹配进度
    with open(zhwikiFile, encoding='utf-8') as fr:
        for line in fr:
            i = i + 1
            if(i%10000 == 0):
                print('%d:%s' %(i,line))
            
            if('doc' in line or line == '\n'):
                pass
            else:
                with open(zhwiki2File, 'a', encoding='utf-8') as fw:
                    fw.write(line)
                    

    return zhwiki2File

if __name__ == '__main__':
    program = "cleanZhwiki.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    cleanZhwiki()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
