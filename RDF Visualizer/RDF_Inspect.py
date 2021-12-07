import sys
import rdflib
from rdflib import URIRef, Namespace, Graph, Literal, BNode, plugin, Variable

from optparse import OptionParser

def get_label(graph, uri, predicate_str):
    predicate = rdflib.term.URIRef(u'http://schema.org/' + predicate_str)
    name = rdflib.term.URIRef(u'http://schema.org/name')
    object_list = []
    
    for obj in graph.objects(uri, predicate):
        label = obj
        if graph.Value(obj, name):
            label = graph.value(obj, name)
        object_list.append(label)
        
    object_labels = ('\n'.join(object_list))
    
    return (object_labels)

