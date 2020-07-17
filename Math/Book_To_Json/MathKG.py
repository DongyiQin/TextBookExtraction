import sys
import os
import json
import re

def ExtractKnowledgePoint(KnowledgePoint):
    # 将一个知识点中的知识细节抽取出来
    DetailAll = [] # 知识点下面的细节①②...分为列表中的一个个元素
    Detail = '' # 一个知识细节为一个字符串
    pos = 0 # pos存储当前位置的下一个位置，以便于找到知识点结束的地方
    length = len(KnowledgePoint)
    # print(KnowledgePoint)
    while pos < length:
        if re.findall('①(.+)',KnowledgePoint[pos]):
            Detail +=  re.findall('①(.+)',KnowledgePoint[pos])[0]

        elif re.findall('②(.+)',KnowledgePoint[pos]):
            DetailAll.append(Detail)
            Detail= ''
            Detail += re.findall('②(.+)',KnowledgePoint[pos])[0] 

        elif re.findall('③(.+)',KnowledgePoint[pos]):
            DetailAll.append(Detail)
            Detail= ''
            Detail += re.findall('③(.+)',KnowledgePoint[pos])[0]

        elif re.findall('④(.+)',KnowledgePoint[pos]):
            DetailAll.append(Detail)
            Detail= ''
            Detail += re.findall('④(.+)',KnowledgePoint[pos])[0]
        
        elif re.findall('⑤(.+)',KnowledgePoint[pos]):
            DetailAll.append(Detail)
            Detail= ''
            Detail += re.findall('⑤(.+)',KnowledgePoint[pos])[0]

        elif re.findall('⑥(.+)',KnowledgePoint[pos]):
            DetailAll.append(Detail)
            Detail= ''
            Detail += re.findall('⑥(.+)',KnowledgePoint[pos])[0]
        else:
            Detail += KnowledgePoint[pos]
        pos += 1
    DetailAll.append(Detail)
    return DetailAll

if __name__ == '__main__':
    json_file = open('MathKG2.json', 'w',encoding='utf-8',errors='ignore')
    # 每种Lesson为一个字典，Key为主题，Value为主题下的内容
    AALesson = {}
    TTopic = {}
    CChapter = {}
    AAknowledge = {}
    with open('AChapter2.json','r',encoding = 'utf8') as fp:
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
                    AChapter = ATopic[0][Chapter][0]
                    # print(AChapter)
                    for Knowledge in AChapter:
                        Aknowledge = AChapter[Knowledge]
                        Temp = ExtractKnowledgePoint(Aknowledge)
                        AChapter[Knowledge] = Temp
                    CChapter[Chapter].append(AChapter)
                TTopic[Topic].append(CChapter)
            AALesson[Lesson].append(TTopic)
              
    json_str = json.dumps(AALesson, indent = 4, ensure_ascii = False)
    json_file.write(json_str)
    json_file.close()