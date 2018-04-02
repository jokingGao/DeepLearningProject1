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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""


nums = set()
with open('texts.csv', 'r') as file:
    reader = csv.reader(file)
    texts = list(reader)
    #print(texts)
    for text in texts:
        nums.add(text[0])
        nums.add(text[1])


with open('calls.csv', 'r') as file:
    reader = csv.reader(file)
    calls = list(reader)
    for call in calls:
        nums.add(call[0])
        nums.add(call[1])
    
    
print("There are {} different telephone numbers in the records.".format(len(nums)))