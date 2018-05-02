import csv


from pydtk.tree import Tree
from pydtk.treekernel import TreeKernel
from pydtk.dtk import DT
from pydtk.operation import fast_shuffled_convolution


if __name__ == '__main__':

    filetk = open("D:\Stanford\TA\hasiltk.csv", "a")

    tree_kernel = []
    with open('hasil.csv') as File:
        reader = csv.reader(File)
        for row in reader:
            if (reader == "KEONG"):
                tree_kernel.remove(row)
            else:
                tree_kernel.append(row)
            #print (tree_kernel)

    txt = []
    with open('hasiltk.csv') as File:
        reader = csv.reader(File)
        for row in reader:
            if (reader == 'KEONG'):
                txt.remove(row)
            else:
                txt.append(row)
            print (txt)

    for j in range(len(tree_kernel)):
        print(j)
        s1 = (str(tree_kernel[j]))
        s2 = (str(txt[2]))

        print (s1)
        print (s2)

        t1 = Tree(string=s1)
        t2 = Tree(string=s2)

        dtCalculator = DT(dimension=8192, LAMBDA=0.6, operation=fast_shuffled_convolution)

        distributedTree = dtCalculator.dt(t1)
        print ("distributed tree = ", distributedTree)

        tk = TreeKernel()

        dtk = DT(dimension=8192)
        for tt in t1.allNodes():
            hasil = (tt.root, tk.evaluate(tt, tt), dtk.kernel(tt, tt))
            filetk.write(str(hasil) + "\n")
            print(hasil)

        print("evaluate = ", tk.evaluate(t1, t2))

        print("dtk = ", dtk.kernel(t1, t2))

    File.close()


    







