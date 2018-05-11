import pandas as pd
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter,OrderedDict
import xlsxwriter

excel_file = "D:\Stanford\TA\dataset.xlsx"

df = pd.ExcelFile(excel_file).parse('Sheet1')
txt = df['Argument'].tolist()
label = df['Label'].tolist()

#print(txt)
#print(label)

x = []

for i in range(len(txt)):
    #print(txt[i])
    data = txt[i]
    data = data.replace("'", "")
    data = data.replace('"', "")
    data = data.replace("(", "")
    data = data.replace(")", "")
    data = data.replace(",", "")
    data = data.replace(".", "")
    data = data.replace("$", "")
    data = data.replace(":", "")
    data = data.replace(";", "")
    b = dict(Counter([j for i,j in pos_tag(word_tokenize(str(data)))]))
    #print(b)
    x.append(b)

keylist = {}
for i in x:
    keylist = {**keylist, **i}
keylist = {key:0 for key in keylist.keys()}
#print(keylist.items())

workbook = xlsxwriter.Workbook('new_dataset.xlsx')
worksheet = workbook.add_worksheet()

ordered_keylist = list(OrderedDict(sorted(keylist.items())))
for i,key in enumerate(ordered_keylist):
    worksheet.write(0,i, key)

worksheet.write(0, len(ordered_keylist), "Label")

row = 1
for i in range(len(x)):
    x[i] = {**keylist, **x[i]}
    #print(i, label[i])
    #print([j for j in x[i]])
    col = 0
    for key in ordered_keylist:
        worksheet.write(row, col, x[i][key])
        col +=1
    worksheet.write(row, col, label[i])
    row += 1
workbook.close()


