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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

with open('texts.csv', 'r') as file:
    reader = csv.reader(file)
    texts = list(reader)
    #print(texts)
    firstRecord = texts[0]
    incomNum = firstRecord[0]
    answerNum = firstRecord[1]
    timeStamp = firstRecord[2]
    print ("First record of texts, {incomNum} texts {answerNum} at time {timeStamp}"
           .format(incomNum=incomNum, answerNum=answerNum, timeStamp=timeStamp))
    
with open('calls.csv', 'r') as file:
    reader = csv.reader(file)
    calls = list(reader)
    lastRecord = calls[-1]
    incomNum = lastRecord[0]
    answerNum = lastRecord[1]
    timeStamp = lastRecord[2]
    during = lastRecord[3]
    print("Last record of calls, {incomNum} calls {answerNum} at time {timeStamp}, lasting {during} seconds"
          .format(incomNum=incomNum, answerNum=answerNum, timeStamp=timeStamp, during=during))