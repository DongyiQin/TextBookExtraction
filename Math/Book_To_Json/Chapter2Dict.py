import sys
import os
import json
import re

def ExtractChapter(AChapter):
# 提取一个单元中的知识
    Chapter = {}  # 一个主题中 （1）（2）（3） 为key，下面的内容为Value
    pos = 0
    Length = len(AChapter)
    for level in AChapter:
        # 主题下的第一层概念（1）（2）（3）为key（FirstLevel）
        pos += 1
        if re.findall('（１）(.+)',level):
            FirstLevel = re.findall('（１）(.+)',level)[0]
            Chapter.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('（２）(.+)',AChapter[pos1])):
                Chapter[FirstLevel].append(AChapter[pos1])
                pos1+=1
            continue
        
        if re.findall('（２）(.+)',level):
            FirstLevel = re.findall('（２）(.+)',level)[0]
            Chapter.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('（３）(.+)',AChapter[pos1])):
                Chapter[FirstLevel].append(AChapter[pos1])
                pos1+=1
            continue

        if re.findall('（３）(.+)',level):
            FirstLevel = re.findall('（３）(.+)',level)[0]
            Chapter.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('（４）(.+)',AChapter[pos1])):
                Chapter[FirstLevel].append(AChapter[pos1])
                pos1+=1
            continue
        
        if re.findall('（４）(.+)',level):
            FirstLevel = re.findall('（４）(.+)',level)[0]
            Chapter.update({FirstLevel:[]}) #  {集合:[]}, {常用逻辑用语:[]}
            pos1 = pos
            while pos1<Length and (not re.findall('（５）(.+)',AChapter[pos1])):
                Chapter[FirstLevel].append(AChapter[pos1])
                pos1+=1
            continue 

    return Chapter

if __name__ == '__main__':
    json_file = open('AChapter.json', 'w',encoding='utf-8',errors='ignore')
    # 每种Lesson为一个字典，Key为主题，Value为主题下的内容
    AALesson = {}
    TTopic = {}
    CChapter = {}
    with open('ATopic.json','r',encoding = 'utf8') as fp:
        ALesson = json.load(fp)
        # print(ALesson)
        for Lesson in ALesson:
            # print(Lesson)
            AALesson.update({Lesson:[]})
            for Topic in ALesson[Lesson][0]:
                # print(Topic)
                TTopic.update({Topic:[]})
                ATopic = ALesson[Lesson][0][Topic]  # 一个主题的内容 
                # print(ATopic[0])
                for Chapter in ATopic[0]:
                    # print(ATopic[0][Chapter])
                    CChapter.update({Chapter:[]})
                    AChapter = ATopic[0][Chapter]
                    Temp = ExtractChapter(AChapter)
                    CChapter[Chapter].append(Temp)
                    print(Temp)
                TTopic[Topic].append(CChapter)
            AALesson[Lesson].append(TTopic)
    json_str = json.dumps(AALesson, indent = 4, ensure_ascii = False)
    json_file.write(json_str)
    json_file.close()