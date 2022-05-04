from math import log

import os
import urllib.request
from bs4 import BeautifulSoup

# doc1 = "Ben studies about computers in Computer Lab"
# doc2 = "Steve teaches at Brown university"
# doc3 = "Data scientists work on large datasets"


def term_frequency(term, doc):
    doc_string = doc.lower()
    term_reps = doc_string.count(term.lower())
    len_of_document = float(len(doc_string.split()))
    normalized_tf = term_reps / len_of_document

    return normalized_tf


def inverseDocumentFrequency(term, allDocs):
    num_docs_with_given_term = 0

    # Iterate through all the documents
    for doc in allDocs:
        if term.lower() in doc.lower():
            num_docs_with_given_term += 1

    if num_docs_with_given_term > 0:
        # Total number of documents
        total_num_docs = len(allDocs)

        # Calculating the IDF
        idf_val = log(1 + float(total_num_docs) / num_docs_with_given_term)
        return idf_val
    else:
        return 0


def calculate_tfidf_score(term, doc, allDocs):
    return term_frequency(term, doc) * inverseDocumentFrequency(term, allDocs)


def rank_all_pages(term):
    allDocsDict = retrieve_site_info()
    rank_dict = dict()

    for key, value in allDocsDict.items():
        score = calculate_tfidf_score(term, value, list(allDocsDict.values()))
        rank_dict[key] = score

    return rank_dict


def sentence_wise_rank_generation(sentence):
    allDocsDict = dict()
    terms = sentence.lower().split()
    for term in terms:
        if not allDocsDict:
            allDocsDict = rank_all_pages(term)
        else:
            newDict = rank_all_pages(term)
            for key in allDocsDict.keys():
                allDocsDict[key] += newDict[key]
    allDocsDict = dict(sorted(allDocsDict.items()))
    return allDocsDict


def scrape_text_data(url):

    sentences = []

    html = urllib.request.urlopen(url)
    htmlParse = BeautifulSoup(html, 'html.parser')

    for para in htmlParse.find_all('p'):
        sentences.append(' '.join(para.get_text().strip().split()))

    title = url.split('/')[-1]

    return title, ' '.join(sentences)


def retrieve_site_info():
    text_path = os.path.abspath('.').split(
        'PageRankProject')[0] + '/PageRankProject/internet/scripts/sites.txt'
    with open(text_path, 'r') as f:
        link_list = f.read().split()

    allDocs = dict()

    for url in link_list:
        key, value = scrape_text_data(url)
        allDocs[key] = value

    return allDocs


freq = sentence_wise_rank_generation("lorem ipsum")
# python3 mytfidf.py computers -> mytfidf.py at 0th index and computers at 1st index
print(freq)
