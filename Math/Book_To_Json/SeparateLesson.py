import sys
import os
import json
import re

def GetALesson(Book):
    ALesson = {} # 字典中的Key为课程类型，Value为每种类型课程的具体内容
    # 比如key必修课程，Value为下面的主题一  主题二。。。
    pos = 0
    for text in Book:
        if re.findall('（一）(.+)',text):
            LessonName = re.findall('（一）(.+)',text)[0]
            ALesson.update({LessonName:[]}) # 必修课程的名称为一个key
            while(not re.findall('（二）(.+)',Book[pos])):
                # 必修课程到选修课程之间的内容为  必修课程的value
                if Book[pos] == '普通高中数学课程标准 （２０１７年版）\n' or Book[pos] == "\n":
                    pos += 1
                    continue
                else:
                    ALesson[LessonName].append(Book[pos])
                    pos+=1
            break
        pos += 1
    
    pos = 0
    for text in Book:
        if re.findall('（二）(.+)',text):
            LessonName = re.findall('（二）(.+)',text)[0]
            ALesson.update({LessonName:[]}) # 选择性必修课程的名称为一个key
            while(not re.findall('（三）(.+)',Book[pos])):
                # 选择性必修课程到选修课程之间的内容为  选择性必修课程的value
                if Book[pos] == '普通高中数学课程标准 （２０１７年版）\n' or Book[pos] == "\n":
                    pos += 1
                    continue
                else:
                    ALesson[LessonName].append(Book[pos])
                    pos+=1
            break
        pos += 1

    pos = 0
    for text in Book:
        if re.findall('（三）(.+)',text):
            LessonName = re.findall('（三）(.+)',text)[0]
            ALesson.update({LessonName:[]}) # 选择性必修课程的名称为一个key
            while(not re.findall('（一）学业质量(.+)',Book[pos])):
                # 选择性必修课程到选修课程之间的内容为  选择性必修课程的value
                if Book[pos] == '普通高中数学课程标准 （２０１７年版）\n' or Book[pos] == "\n":
                    pos += 1
                    continue
                else:
                    ALesson[LessonName].append(Book[pos])
                    pos+=1
            break
        pos += 1
    
    return ALesson

if __name__ == '__main__':
    dirname = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dirname,'math.txt') # 读取教科书内容
    with open(filepath,'r',encoding='utf-8',errors='ignore') as f:
        Book = f.readlines() # 整个章节的内容
        ALesson = GetALesson(Book)
    json_file = open('Lesson.json', 'w',encoding='utf-8',errors='ignore')
    json_str = json.dumps(ALesson, indent=4, ensure_ascii=False)
    json_file.write(json_str)
    json_file.close()