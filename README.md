# ZhWIkiCorpus
中文维基百科语料库构建


1、抽取正文文本：

INFO: Finished 5-process extraction of 1093446 articles in 1919.1s (569.8 art/s)

INFO: total of page: 2481078, total of articl page: 1093446; total of used articl page: 1093446

命令：
python WikiExtractor.py -b 3500M -o extracted zhwiki-20200201-pages-articles-multistream.xml.bz2

语料下载地址：

https://dumps.wikimedia.org/zhwiki/


2、正文文本清洗：

手写代码 cleanZhwiki.py 进行清洗


3、opencc繁简转换：

https://github.com/yichen0831/opencc-python 

代码下载下来之后执行安装命令：

python setup.py install

完了之后执行自己手写代码：t2s.py

程序运行时长：14:52:03.997760


3、jieba分词

利用zhwiki词条索引进行繁简转化后作为自定义字典用于分词，

手写代码见：buildSegDict.py

程序结束运行时间：2020-02-08 14:59:09.734440
buildSegDict.py程序运行时长：1:20:24.148532

手写代码 segSentence.py 进行分词
