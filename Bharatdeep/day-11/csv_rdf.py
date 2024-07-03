import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace

data = pd.read_csv('./data.csv')
data['id'] = data['id'].apply(lambda x: f'http://example.org/{x}')


g = Graph()
ex = Namespace('http://example.org/')

for _, row in data.iterrows():
    subject = URIRef(row['id'])
    g.add((subject, ex.hasName, Literal(row['name'])))
    g.add((subject, ex.hasAge, Literal(row['age'])))

g.serialize(destination='output.rdf', format='xml')
