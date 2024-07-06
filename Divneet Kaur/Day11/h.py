import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace

# Load CSV data into a DataFrame
df = pd.read_csv('Book1.csv')

# Create an RDF graph
g = Graph()

# Define a namespace
n = Namespace('http://example.org/')

# Iterate over the DataFrame and add triples to the graph
for index, row in df.iterrows():
    subj = URIRef(n[str(row['id'])])  # Assume 'id' is a column in your CSV
    for col in df.columns:
        if col != 'id':  # Skip the id column for predicates
            g.add((subj, n[col], Literal(row[col])))

# Save the graph in RDF format
g.serialize('output.rdf', format='xml')
