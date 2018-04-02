"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

"""
#The way of opening and reading csv files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

telTimeDict = {}
telNum = -1
longestTime = 0
with open('calls.csv', 'r') as file:
    reader = csv.reader(file)
    calls = list(reader)
    #print(calls)
    for call in calls:
        num1 = call[0]
        num2 = call[1]
        during = call[3]
        
        if telTimeDict.get(num1) == None:
            telTimeDict[num1] = int(during)
        else:
            telTimeDict[num1] += int(during)
        if telTimeDict.get(num2) == None:
            telTimeDict[num2] = int(during)
        else:
            telTimeDict[num2] += int(during)
            
        if telTimeDict.get(num1) > longestTime:
            telNum = num1
            longestTime = telTimeDict.get(num1)
        if telTimeDict.get(num2) > longestTime:
            telNum = num2
            longestTime = telTimeDict.get(num2)
            
print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(telNum, longestTime))