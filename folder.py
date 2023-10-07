import os,pandas,openpyxl,sys,numpy
read_file = pandas.read_excel(r'./data-folder-name.xlsx')
open(r'./data.txt', 'w')
read_file.to_csv('./data.txt')
data = open(r'./data.txt').readlines()
newList = ''.join(data)
newData = newList.split('\n')
double_NewData = ''.join(newData)
triple_NewData = ''.join([i for i in double_NewData  if not i.isdigit()])
xData = triple_NewData.lstrip(',')
finalData = xData.split(',')

pathRemove = './data.txt'
if os.path.isfile(pathRemove):
    os.remove(pathRemove)
    
path = './YOUR_FOLDERS_HERE/'
os.chdir(path)
for i in range(len(finalData)):
    folder = finalData[i]
    os.makedirs(folder)