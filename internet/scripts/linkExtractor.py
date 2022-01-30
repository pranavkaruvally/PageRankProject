from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
import re

universal_link_set = {
    "http://127.0.0.1:8000/cats/1": 0,
    "http://127.0.0.1:8000/cats/2": 1,
    "http://127.0.0.1:8000/cats/3": 2,
    "http://127.0.0.1:8000/cats/4": 3,
}

def extract_links(url):
    req = Request(url) # "http://127.0.0.1:8000/cats/1"
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = set()
    for link in soup.findAll('a'):
        hyperlink = link.get('href')
        if (hyperlink is not None) and (hyperlink != url):
            links.add(hyperlink)

    #print(links)
    return links

def probability_calc(links):
    prob_vector = [0] * len(universal_link_set)
    try:
        prob_value = 1/(len(links))
        for link in links:
            prob_vector[universal_link_set[link]] = prob_value
        return np.array(prob_vector)
    except ZeroDivisionError: #To address cases where a website has no hyperlinks
        return prob_vector

def generate_transitional_matrix():
    transitional_space = []
    for link in universal_link_set.keys():
        extracted_link_list = extract_links(link)
        prob = probability_calc(extracted_link_list)
        transitional_space.append(prob)
    return np.column_stack(transitional_space)

def add_damping_factor(P):
    beta = 0.85
    n = len(universal_link_set)
    v = np.array([1] * n).T
    e = np.array([1/n] * n)

    #R = beta*P + (1-beta)*(np.dot(v, e.T))
    R = beta*P + (1-beta) * 1/n
    return R

def generate_converged_rank_vector(transitional_matrix): # We use the power method
    size = transitional_matrix.shape[0]
    initial_rank = np.ones(size) * 1/size
    previous_ranking = initial_rank
    iterations = 1
    new_rank = transitional_matrix @ initial_rank

    while np.linalg.norm(previous_ranking - new_rank) > 1e-4:
        previous_ranking = new_rank
        new_rank = transitional_matrix @ new_rank
        iterations += 1

    return new_rank, iterations

if __name__ == '__main__':
    transitional_matrix = generate_transitional_matrix()
    new_transitional_matrix = add_damping_factor(transitional_matrix)
    rank = generate_converged_rank_vector(new_transitional_matrix)
    print(rank)