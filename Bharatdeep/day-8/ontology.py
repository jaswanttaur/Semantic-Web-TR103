import rdflib
from rdflib import RDF, RDFS, OWL
from pyvis.network import Network

# Load your OWL ontology file
g = rdflib.Graph()
# Adjust the path and format as needed
g.parse("./gtfs.rdf", format="xml")

# Create a PyVis network
net = Network(directed=True)

# Define node styles based on OWL entities
node_styles = {
    'Class': {'color': 'lightblue', 'shape': 'box'},
    'ObjectProperty': {'color': 'lightgreen', 'shape': 'ellipse'},
    'DatatypeProperty': {'color': 'orange', 'shape': 'triangle'},
    'Individual': {'color': 'pink', 'shape': 'dot'}
}

# Track added nodes to avoid duplicates
added_nodes = set()

# Add nodes and edges from OWL ontology with custom styles
for s, p, o in g:
    # Adding subject node if not already added and not a literal
    if isinstance(s, rdflib.URIRef) or isinstance(s, rdflib.BNode):
        if str(s) not in added_nodes:
            node_type = 'Class'  # Default to Class
            if (s, RDF.type, OWL.Class) in g:
                node_type = 'Class'
            elif (s, RDF.type, OWL.ObjectProperty) in g:
                node_type = 'ObjectProperty'
            elif (s, RDF.type, OWL.DatatypeProperty) in g:
                node_type = 'DatatypeProperty'
            elif (s, RDF.type, OWL.NamedIndividual) in g:
                node_type = 'Individual'

            net.add_node(str(s), label=str(s), title=node_type,
                         **node_styles.get(node_type, {}))
            added_nodes.add(str(s))

    # Adding object node if not already added and not a literal
    if isinstance(o, rdflib.URIRef) or isinstance(o, rdflib.BNode):
        if str(o) not in added_nodes:
            node_type = 'Class'  # Default to Class
            if (o, RDF.type, OWL.Class) in g:
                node_type = 'Class'
            elif (o, RDF.type, OWL.ObjectProperty) in g:
                node_type = 'ObjectProperty'
            elif (o, RDF.type, OWL.DatatypeProperty) in g:
                node_type = 'DatatypeProperty'
            elif (o, RDF.type, OWL.NamedIndividual) in g:
                node_type = 'Individual'

            net.add_node(str(o), label=str(o), title=node_type,
                         **node_styles.get(node_type, {}))
            added_nodes.add(str(o))

    # Adding edge if both nodes exist
    if isinstance(s, rdflib.URIRef) or isinstance(s, rdflib.BNode):
        if isinstance(o, rdflib.URIRef) or isinstance(o, rdflib.BNode):
            if str(s) in added_nodes and str(o) in added_nodes:
                net.add_edge(str(s), str(o), title=str(p))

# Visualize the graph
net.show("ontology_graph.html", notebook=False)
