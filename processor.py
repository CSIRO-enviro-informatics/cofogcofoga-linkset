import rdflib


# g = rdflib.Graph().parse('imports/cofog.ttl', format='ttl')
#
# q = '''
#     PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
#     SELECT *
#     WHERE {
#         ?s  a skos:Concept ;
#             skos:prefLabel ?pl .
#         FILTER langMatches( lang(?pl), "en" )
#     }
#     ORDER BY ?pl
# '''
#
# for r in g.query(q):
#     print('{}, {}'.format(str(r['s']), r['pl']))


g2 = rdflib.Graph().parse('imports/cofog-a.ttl', format='ttl')

q2 = '''
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT * 
    WHERE {
        ?s  a skos:Concept ;
            skos:prefLabel ?pl .
        FILTER langMatches( lang(?pl), "en" )
    }
    ORDER BY ?pl
'''

for r in g2.query(q2):
    print('{}, {}'.format(str(r['s']), r['pl']))
