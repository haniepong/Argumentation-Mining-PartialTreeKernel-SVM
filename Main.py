import io
import os
import csv

from nltk.parse import stanford
from pydtk.tree import Tree
from pydtk.treekernel import TreeKernel
from pydtk.dtk import DT
from pydtk.operation import fast_shuffled_convolution

if __name__ == '__main__':
    filename = io.open("D:\dataset\essay01.ann", "r", encoding="utf-8")  # datasetnya
    f2 = open("D:\Stanford\TA\hasil.csv", "a")  # hasil

    paragraph = filename.read()
    filename.close()
    lists = paragraph.split("\n")

    os.environ['CLASSPATH'] = "C:\Stanford\stanford-parser-full-2015-04-20"  # folder di c
    java_path = "C:/Program Files/Java/jdk1.8.0_161/bin/java.exe"
    os.environ['JAVAHOME'] = java_path

    for i in range(len(lists)):
        # print lists[i]
        data = lists[i]
        data1 = data.replace("'", " ")
        data2 = data1.replace('"', " ")
        data3 = data2.replace("(", "")
        data4 = data3.replace(")", "")
        try:
            parser = stanford.StanfordParser(model_path='C:/Stanford/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
            sentences = list(parser.raw_parse(str(data4)))
            fix = str(sentences)
            f2.write(fix + "\n")
        except:
            f2.write("KEONG\n")
            #print (lists[i])
            #print (tree.productions())
            #print tree.pretty_print()

    f2.close()


