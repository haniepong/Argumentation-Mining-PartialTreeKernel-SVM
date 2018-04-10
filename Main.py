import io
import os

from nltk.parse import stanford
from pydtk.tree import Tree
from pydtk.treekernel import TreeKernel
from pydtk.dtk import DT
from pydtk.operation import fast_shuffled_convolution

if __name__ == '__main__':
    filename = io.open("D:\dataset\essay01.ann", "r", encoding="utf-8")  # datasetnya
    f2 = open("D:\dataset\hasilcoba2.txt", "a")  # hasil

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
            parser = stanford.StanfordParser(
                model_path='C:/Stanford/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
            sentences = list(parser.raw_parse(str(data4)))
            tree = sentences[0]
            fix = str(tree.productions)
            f2.write(fix + "\n")
        except:
            f2.write("KEONG\n")
        #print (lists[i])
        #print (tree.productions())
        #print tree.pretty_print()

    f2.close()

    print (str(sentences[0]))

    s1 = (str(sentences[0]))
    s2 = ("(@S)")

    t1 = Tree(string=s1)
    t2 = Tree(string=s2)
    #print (t1)
    #print (t2)

    dtCalculator = DT(dimension=8192, LAMBDA=0.6, operation=fast_shuffled_convolution)

    distributedTree = dtCalculator.dt(t1)

    print (distributedTree)

    tk = TreeKernel()

    dtk = DT(dimension=8192)
    for tt in t1.allNodes():
        print(tt.root, tk.evaluate(tt, tt), dtk.kernel(tt, tt))

    print(tk.evaluate(t1, t2))

    print(dtk.kernel(t1, t2))



