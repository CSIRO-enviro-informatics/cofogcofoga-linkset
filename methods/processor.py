import rdflib
import Levenshtein

COFOG = {}
COFOG_A = {}
cleaning_pairs = [
    ('  (IS)', ''),  # artefacts in COFOG I don't understand
    ('  (CS)', ''),  # artefacts in COFOG I don't understand
    (' (IS)', ''),  # artefacts in COFOG I don't understand
    (' (CS)', ''),  # artefacts in COFOG I don't understand
    (' and ', ' '),
    (' - ', ' '),
    (',', ''),
    ('(', ''),
    (')', ''),
]


# replaces all the first item in a list of pairs of items with the second, for all occurrences in text
def replace_all(text, pairs):
    for p in pairs:
        text = text.replace(p[0], p[1])
    return text


# loads COFOG into a Python dict
def load_cofog():
    global COFOG

    # load COFOG
    g = rdflib.Graph().parse('imports/cofog.ttl', format='ttl')

    # get all concepts and prefLabels, in English
    q = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            ?c  a skos:Concept ;
                skos:prefLabel ?pl .
            FILTER langMatches( lang(?pl), "en" )
        }
        ORDER BY ?pl
    '''

    # load all Concepts and prefLabels into a dict for comparison

    for r in g.query(q):
        # print('{}, {}'.format(str(r['s']), r['pl']))
        COFOG[str(r['c'])] = {'pl': str(r['pl'])}


# loads COFOG-A into a Python dict
def load_cofog_a():
    global COFOG_A
    # load COFOG-A
    g2 = rdflib.Graph().parse('imports/cofog-a.ttl', format='ttl')

    # get all concepts and prefLabels, in English
    q2 = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT *
        WHERE {
            ?c  a skos:Concept ;
                skos:prefLabel ?pl .
            FILTER langMatches( lang(?pl), "en" )
        }
        ORDER BY ?pl
    '''

    # load all Concepts and prefLabels into a dict for comparison
    COFOG_A = {}
    for r in g2.query(q2):
        # print('{}, {}'.format(str(r['s']), r['pl']))
        COFOG_A[str(r['c'])] = {'pl': str(r['pl'])}


# loop through COFOG-A
#   for each Concept's prefLabel
#       remove a set of useless words and characters ['and', ' - ', ',']
#       compute the L distance to each Concept in COFOG's prefLabel, useless stuff removed too
#       store each URI of COFOG-A concepts in an ordered array (Python list), smallest to largest distance

load_cofog_a()
load_cofog()

# FOR TESTING
# COFOG_A = {
#     'http://linked.data.gov.au/def/cofog-a/01': {'pl': 'General Public Services'},
# }

for c, v in COFOG_A.items():
    distances = []  # to store the distance from this COFOG-A item to each COFOG item
    pl_clean = replace_all(v['pl'], cleaning_pairs).lower()

    for c2, v2 in COFOG.items():
        pl2_clean = replace_all(v2['pl'], cleaning_pairs).lower()
        d = Levenshtein.distance(pl_clean, pl2_clean)
        distances.append((c2, d, v2['pl']))

    # order the distances, smallest to largest
    distances.sort(key=lambda tup: tup[1])

    COFOG_A[c]['distances'] = distances

# get matches of a certain distance
with open('matches.csv', 'w') as f:
    for c, v in COFOG_A.items():
        for d in v['distances']:
            if d[1] < 5:
                # use hash to separate files as there are commas in text
                f.write('{}#{}#{}#{}#{}\n'.format(c, v['pl'], d[0], d[2], d[1]))



# Excel Methods
'''
Place all matches into Excel
Sort by L distance
Considering all 0-length latches:
    Remove only cross level duplicates (e.g. 01 == 010 if also 01 == 01)
    
Considering all 1+ length matches:
    Manually removed obvious errors (there weren't too many)
'''