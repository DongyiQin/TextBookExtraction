import sys
import os
import re
from collections import defaultdict, OrderedDict
import json

def ExtractLesson(book):
    # 提取主题，每个主题为Lesson字典中的一个key
    # 每个主题后的全部内容作为主题Key下的Value存储
    pos = 0
    ALesson = {}
    Length = len(book)
    for text in book:
        if re.findall('主题一(.+)',text):
            TopicName = re.findall('主题一\u3000(.+)',text)
            ALesson.update({TopicName[0]:[]}) # 主题一的名称为一个key
            while pos<Length and book[pos] != '【教学提示】\n':
                # 主题一到主题二之间的内容为  主题一的value
                ALesson[TopicName[0]].append(book[pos])
                pos+=1
            break
        pos += 1

    pos = 0
    for text in book:
        if re.findall('主题二(.+)',text):
            TopicName = re.findall('主题二\u3000(.+)',text)
            ALesson.update({TopicName[0]:[]})
            while pos<Length and book[pos] != '【教学提示】\n':
                ALesson[TopicName[0]].append(book[pos])
                pos+=1
            break
        pos += 1

    pos = 0
    for text in book:
        if re.findall('主题三(.+)',text):
            TopicName = re.findall('主题三\u3000(.+)',text)
            ALesson.update({TopicName[0]:[]})
            while pos<Length and book[pos] != '【教学提示】\n':
                ALesson[TopicName[0]].append(book[pos])
                pos+=1
            break
        pos += 1

    pos = 0
    for text in book:
        if re.findall('主题四(.+)',text):
            TopicName = re.findall('主题四\u3000(.+)',text)
            ALesson.update({TopicName[0]:[]})
            while pos<Length and book[pos] != '【教学提示】\n':
                ALesson[TopicName[0]].append(book[pos])
                pos+=1
            break
        pos += 1
                
    pos = 0
    for text in book:
        if re.findall('主题五(.+)',text):
            TopicName = re.findall('主题五\u3000(.+)',text)
            ALesson.update({TopicName[0]:[]})
            while pos<Length and (book[pos] != '【教学提示】\n'):
                ALesson[TopicName[0]].append(book[pos])
                pos+=1
            # print(TopicName[0]])
            break
        pos += 1
    return ALesson 

if __name__ == '__main__':
    json_file = open('ALesson.json', 'w',encoding='utf-8',errors='ignore')
    # 每种Lesson为一个字典，Key为主题，Value为主题下的内容
    AALesson = {}
    with open('Lesson.json','r',encoding = 'utf8') as fp:
        AllLesson = json.load(fp)
        # 必修课程、选修课程为Key，内容为Value
        for Lesson in AllLesson:
            # print(AllLesson[Lesson])
            if Lesson != '选修课程':
                ALesson = ExtractLesson(AllLesson[Lesson]) 
            # 获取必修、选修课程，返回一种课程的一个字典，
            # Key为主题，Value为每个主题的内容
                temp = []
                temp.append(ALesson)
                AALesson.update({Lesson:[]})
                AALesson[Lesson] = temp
        json_str = json.dumps(AALesson, indent = 4, ensure_ascii = False)
        json_file.write(json_str)
    json_file.close()
             