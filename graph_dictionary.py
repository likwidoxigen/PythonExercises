import csv
from matplotlib import pyplot as plt
import numpy as np

example = {
    '1': {
        'a': {
            'Highly Effective': 0,
            'Effective': 0,
            'Partially Effective': 0,
            'Ineffective': 0
        }
    }
}

counts = {}

def verify_domain(domain, dictionary):
    if domain not in dictionary:
        dictionary[domain] = {}

def verify_subdomain(domain, subdomain, dictionary):
    if subdomain not in dictionary[domain]:
        dictionary[domain][subdomain] = {}

def increment_eval_score_count(domain, subdomain, eval_score, dictionary):
    if eval_score not in dictionary[domain][subdomain]:
        dictionary[domain][subdomain][eval_score] = 1
    else:
        dictionary[domain][subdomain][eval_score] += 1

def graph_data(dictionary):
    fig, axs = plt.subplots(2,2)
    plot_list = []
    fig.suptitle("This is a test")
    for domain in dictionary.keys():
        xvalues, he_counts, e_counts, pe_counts, ie_counts = [], [], [], [], []
        for subdomain in dictionary[domain].keys():
            xvalues.append(domain + subdomain)
            he_counts = build_he_list(dictionary, domain, subdomain, he_counts)
            e_counts = build_e_list(dictionary, domain, subdomain, e_counts)
            pe_counts = build_pe_list(dictionary, domain, subdomain, pe_counts)
            ie_counts = build_ie_list(dictionary, domain, subdomain, ie_counts)
            print(he_counts)
        plot_list.append(build_graph(xvalues, he_counts, e_counts, pe_counts, ie_counts, domain))
    axs[0,0] = plot_list.pop()
    axs[1,0] = plot_list.pop()
    axs[0,1] = plot_list.pop()
    axs[1,1] = plot_list.pop()
    plt.show()


def build_he_list(dictionary, domain, subdomain, list):
    try:
        list.append(dictionary[domain][subdomain]['Highly&nbsp;Effective'])
    except KeyError:
        list.append(0)
    return list

def build_e_list(dictionary, domain, subdomain, list):
    try:
        list.append(dictionary[domain][subdomain]['Effective'])
    except KeyError:
        list.append(0)
    return list

def build_pe_list(dictionary, domain, subdomain, list):
    try:
        list.append(dictionary[domain][subdomain]['Partially Effective'])
    except KeyError:
        list.append(0)
    return list

def build_ie_list(dictionary, domain, subdomain, list):
    try:
        list.append(dictionary[domain][subdomain]['Ineffective'])
    except KeyError:
        list.append(0)
    return list

def build_graph(xvalues, y1values, y2values, y3values, y4values, domain):
    """Creates the graph based on passed lists"""
    x = np.arange(len(xvalues))
    #set the width of all of the bars (combined width)
    width = 0.25

    #create the bars that will be displayed
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - (width + width/2), y1values, width, label="Highly Effective")
    rects2 = ax.bar(x - width/2, y2values, width, label="Effective")
    rects3 = ax.bar(x + width/2, y3values, width, label="Partially Effective")
    rects4 = ax.bar(x + (width + width/2), y4values, width, label="Ineffective")

    #format graph axes
    ax.set_title(f'Domain {domain} Scores', fontsize=32)
    ax.set_xlabel('Subdomain', fontsize=24)
    ax.set_ylabel('No. of Scores', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(xvalues)

    #create a legend
    ax.legend()

    #display graph
    #plt.show()
    return fig

#print('Enter the file name for the csv file: ')
#filename = input()

filename='Anon_Teacher_Raw_Data.csv'

#Open file and get headers
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        domain = row[header_row.index('Criteria')][0]
        subdomain = row[header_row.index('Criteria')][1]
        eval_score = row[header_row.index('Value')]
        verify_domain(domain, counts)
        verify_subdomain(domain, subdomain, counts)
        increment_eval_score_count(domain, subdomain, eval_score, counts)

graph_data(counts)
