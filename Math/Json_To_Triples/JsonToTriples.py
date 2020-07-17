##  将json格式的数学教材转化为三元组形式

import json

if __name__ == '__main__':
    triples_file = open('MathKG1.triples', 'w',encoding='utf-8',errors='ignore')
    with open('MathKG.json','r',encoding = 'utf8') as js:
        json_file = json.load(js)
        for Lesson in json_file:
            triples_file.write('高中数学'+'\t\t'+'包括课程'+'\t\t'+Lesson+'\n')
            triples_file.write(Lesson+'\t\t'+'type'+'\t\t'+'课程'+'\n')
            for chapter in json_file[Lesson][0]:
                triples_file.write(Lesson+'\t\t'+'包括主题'+'\t\t'+chapter+'\n')
                triples_file.write(chapter+'\t\t'+'type'+'\t\t'+'主题'+'\n')
                for unit in json_file[Lesson][0][chapter][0]:
                    # triples_file.write(chapter+'\t\t'+'包括知识单元'+'\t\t'+unit+'\n')
                    # triples_file.write(unit+'\t\t'+'type'+'\t\t'+'知识单元'+'\n')
                    
                    if (unit == '拓展视野') or (unit == '日常生活') or (unit == '地方特色的数学课程') \
                        or (unit == '大学数学的先修课程'):
                            triples_file.write(unit+'\t\t'+'包括要求'+'\t\t'+json_file[Lesson][0][chapter][0][unit][0]+'\n')
                            triples_file.write(json_file[Lesson][0][chapter][0][unit][0]+'\t\t'+'type'+'\t\t'+'内容要求'+'\n')
                    elif (unit != '拓展视野') and (unit != '日常生活') and (unit != '地方特色的数学课程') \
                        and (unit != '大学数学的先修课程'):
                            for unit1 in json_file[Lesson][0][chapter][0][unit][0]:
                                # t = 0
                                for detail in json_file[Lesson][0][chapter][0][unit][0][unit1]:
                                    # t += 1
                                    triples_file.write(unit1+'\t\t'+'包括要求'+'\t\t'+detail+'\n')
                                    triples_file.write(detail+'\t\t'+'type'+'\t\t'+'内容要求'+'\n')
                    else:
                        for unit1 in json_file[Lesson][0][chapter][0][unit][0]:
                            triples_file.write(unit+'\t\t'+'包含知识单元'+'\t\t'+unit1+'\n')
                            triples_file.write(unit1+'\t\t'+'type'+'\t\t'+'知识单元'+'\n')
                    
    triples_file.close()