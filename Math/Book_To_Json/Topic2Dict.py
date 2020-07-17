import sys
import os
import re
from collections import defaultdict, OrderedDict
import json
# 将ALesson作为输入，将1.2.按序号分开，
# 1.为key，之后的内容为Value

def ExtractATopic(ATopic):
# 提取一个主题中的知识
    Topic = {}  # 一个主题中 1.2.3. 为key，下面的内容为Value
    pos = 0
    Length = len(ATopic)
    for level in ATopic:
        # 主题下的第一层概念1.2.3.为key（FirstLevel）
        pos += 1
        if re.findall('１．(.+)',level):
            FirstLevel = re.findall('１．(.+)',level)[0]
            Topic.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('２．(.+)',ATopic[pos1])):
                Topic[FirstLevel].append(ATopic[pos1])
                pos1+=1
            continue
        
        if re.findall('２．(.+)',level):
            FirstLevel = re.findall('２．(.+)',level)[0]
            Topic.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('３．(.+)',ATopic[pos1])):
                Topic[FirstLevel].append(ATopic[pos1])
                pos1+=1
            continue

        if re.findall('３．(.+)',level):
            FirstLevel = re.findall('３．(.+)',level)[0]
            Topic.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('４．(.+)',ATopic[pos1])):
                Topic[FirstLevel].append(ATopic[pos1])
                pos1+=1
            continue
        
        if re.findall('４．(.+)',level):
            FirstLevel = re.findall('４．(.+)',level)[0]
            Topic.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('４．(.+)',ATopic[pos1])):
                Topic[FirstLevel].append(ATopic[pos1])
                pos1+=1
            continue 
    # print(Topic)
    return Topic
        
if __name__ == '__main__':
    json_file = open('ATopic.json', 'w',encoding='utf-8',errors='ignore')
    # 每种Lesson为一个字典，Key为主题，Value为主题下的内容
    AALesson = {}
    TTopic = {}
    with open('ALesson.json','r',encoding = 'utf-8') as fp:
        ALesson = json.load(fp)
        # print(ALesson)
        for Lesson in ALesson:
            AALesson.update({Lesson:[]})
            for Topic in ALesson[Lesson][0]:
                # print(Topic)
                TTopic.update({Topic:[]})
                ATopic = ALesson[Lesson][0][Topic]  # 一个主题的内容
                Temp = ExtractATopic(ATopic)
                TTopic[Topic].append(Temp)

            AALesson[Lesson].append(TTopic)

    json_str = json.dumps(AALesson, indent = 4, ensure_ascii = False)
    json_file.write(json_str)
    json_file.close()