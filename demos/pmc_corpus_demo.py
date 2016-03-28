from ddlite import *
from datasets import PubMedCentralCorpus

#
# PubMedCentral Corpus
#
inputdir = "/Users/fries/Desktop/pmc/"
parser = SentenceParser()
corpus = PubMedCentralCorpus(inputdir, parser, cache_path="/tmp")

# we iterate through documents
for i,doc in enumerate(corpus):
    for sentence in doc["sentences"]:
        print sentence
    break

# look at specific metadata
for i,doc in enumerate(corpus):
    for attribute in doc["metadata"]:
        print "%s: %s" % (attribute, doc["metadata"][attribute])
    break

# PMC articles also have structure which is useful to consider
# e.g., only looking at text from the "Methods and Materials" section 
for i,doc in enumerate(corpus):
    for title,section in zip(doc["section-titles"],doc["sections"]):
        for sentence in section:
            print "******%s******" % title, sentence 
    break