# coding:utf-8
import rdflib
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
def create(MathBook):
    g = rdflib.Graph()
    
    ContentNum = {}
    for line in AllTriples:
        Entity1 = ''
        Property = ''
        Entity2 = ''

        Tap = 0
        for ch in line:
            if ch == '\t':
                Tap += 1
            elif Tap == 0 and ch!= ' ':
                Entity1 += ch
                continue
            elif Tap == 2 and ch!= ' ':
                Property += ch
                continue
            elif Tap == 4 and ch!= ' ':
                Entity2 += ch
        if Property == '包括主题':
            Course = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + Entity1)
            HasTopic = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/property/' + Property)
            Topic = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + Entity2)
            g.add((Course, HasTopic, Topic))

            TypeTitle = rdflib.URIRef('/Type')
            Type = rdflib.Literal("Course", datatype = XSD.string)
            LabelTitle = rdflib.URIRef('/Label')
            Label = rdflib.Literal("课程", datatype = XSD.string)
            g.add((Course, TypeTitle , Type))
            g.add((Course, LabelTitle, Label))
                
            

        elif Property == '包括知识单元':
            Topic = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + Entity1)
            HasKnowledgeUnit = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/property/' + Property)
            KnowledgeUnit = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + Entity2)
            g.add((Topic, HasKnowledgeUnit, KnowledgeUnit))

            TypeTitle = rdflib.URIRef('/Type')
            Type = rdflib.Literal("Topic", datatype = XSD.string)
            LabelTitle = rdflib.URIRef('/Label')
            Label = rdflib.Literal("主题", datatype = XSD.string)
            g.add((Topic, TypeTitle , Type))
            g.add((Topic, LabelTitle, Label))
                
        
        elif Property == '包括要求':
            if Entity1 not in ContentNum:
                ContentNum[Entity1] = 1
            else:
                ContentNum[Entity1] += 1
            
            KnowledgeUnit = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + Entity1)
            HasContent = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/property/' + Property)
            Content = rdflib.URIRef('http://kg.bnu.edu.cn/coursestandard/resource/' + 'Content' + str(ContentNum[Entity1]))
            g.add((KnowledgeUnit, HasContent, Content))

            TypeTitle = rdflib.URIRef('/Type')
            Type = rdflib.Literal("KnowledgeUnit", datatype = XSD.string)
            LabelTitle = rdflib.URIRef('/Label')
            Label = rdflib.Literal("知识单元", datatype = XSD.string)
            g.add((KnowledgeUnit, TypeTitle , Type))
            g.add((KnowledgeUnit, LabelTitle, Label))
                

    g.serialize("Math.rdf", format = 'xml')

if __name__ == "__main__":
    File = open('MathKG.triples', encoding = 'utf-8')
    AllTriples = File.readlines( )
    create(AllTriples)
    File.close( )

    
   
