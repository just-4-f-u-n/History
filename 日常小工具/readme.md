# 使用Python加速日常办公效率



## 表格处理

- csv文件读写

  ```python
  import csv
  
  #读文件
  file1 = open('1.csv','r') #file1 = open('1.csv','r',encoding='utf-8')
  reader1=csv.reader(file1)
  for line in reader1:
      print(line)
      #line[0],line[1]...可用字典或数组随意处理
  file1.close()
  
  #写文件
  file2 = open('2.csv','w',newline='') #file2 = open('2.csv','w',encoding='utf-8')
  writer = csv.writer(file2)
  writer.writerow(['第一列','第二列'])
  file2.close()
  
  ```

  

- excel文件读写

  *首先要安装xlrd和xlwt库，可直接pip install xlrd和pip install xlwt*

  ```python
  import xlrd,xlwt
  
  #读excel表
  data = xlrd.open_workbook('1.xlsx') #data = xlrd.open_workbook('1.xlsx',encoding='utf-8')
  table = data.sheets()[0] #xlsx文件中的第一个表
  nrows = table.nrows #行数
  ncols = table.ncols #列数
  #print(table.cell(1,0).value)  #打印第一行第零列的值
  
  #写excel表
  workbook = xlwt.Workbook(encoding='utf-8')  #最后再保存！
  #创建一个表
  worksheet = workbook.add_sheet('My Worksheet')
  #写入值
  row = 5
  col = 2
  worksheet.write(row,col,label='test')  #写入行，列，值
  #最后整个保存新建
  workbook.save('new.xlsx') #workbook.save('new.xls')
  ```

  