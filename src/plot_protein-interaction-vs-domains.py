# USAGE:
# python plot_protein-interaction-vs-domains.py
#
# AIM: 
# generates basic statistics and a basic boxplot comparing the number of protein
# interactions and the number of protein domains
# 
#required pandas, numpy, matplotlib, seaborn, operator, networkx modules


# loading modules


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from operator import itemgetter
import networkx as nx

# loading data
network_data_frame = pd.read_csv('data/9606.protein.links.v11.0.txt.gz', compression='gzip',
                                  sep=' ')
network_data_frame = network_data_frame[network_data_frame['combined_score'] >= 500]

protein_domain = pd.read_csv('data/proteins_w_domains.txt', sep='\t').rename(columns = {'Pfam ID': 'domain_ID', 'Protein stable ID': 'protein_ID'}, inplace = False)

# generating network data
network = nx.from_pandas_edgelist(network_data_frame, source = 'protein1', target = 'protein2')

def grouping_by_degree(network):
    """funtion to separed a network between larger or smaller than 100 node degrees and return 
    a data_frame with their names
    """
    degree_dict = dict(network.degree(network.nodes()))
    nx.set_node_attributes(network, degree_dict, 'degree')
    sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
    df_group = pd.DataFrame(columns=['node_degree', 'protein_ID', 'degree_value']) 

    for key, value in degree_dict.items():
        key = key.replace('9606.','')
        if value > 100:
            df_group = df_group.append({'node_degree' : 'larger_100', 'protein_ID' : key, 'degree_value' : value}, ignore_index=True)
        else:
            df_group = df_group.append({'node_degree' : 'smaller_100', 'protein_ID' : key, 'degree_value' : value}, ignore_index=True)
    
    return df_group

grouped_by_degree = grouping_by_degree(network)

# merging dataframes

prot_degree_domain = pd.merge(grouped_by_degree, protein_domain.dropna(), on = 'protein_ID')

prot_domain_count = prot_degree_domain.groupby(['protein_ID','node_degree','degree_value']).count().reset_index()

# plotting
def plotting_degre_x_domains(dataframe): 
    """funtion to plot a boxplot of proteins domains counts with node degree larger than 100 and smaller than 100 
    """
    plot = sns.boxplot(y = 'domain_ID', x = 'node_degree', data = dataframe)
    plt.xlabel('Node degree')
    plt.ylabel('# protein domains')
    plot.set(yscale="log")
    plt.savefig('results/protein_domains_vs_string_degree.png')
    
plotting_degre_x_domains(prot_domain_count)

# basic statistics summary saved
def basic_statistics(dataframe, file_output):
    """
    Basic statistics groupped by larger than 100 node degrees and less or equal than 100 node degree 
    and saved as csv on the results folder
    """
    stats_by_node = dataframe.groupby('node_degree').describe()
    stats_by_node.to_csv(file_output)
    

basic_statistics(prot_domain_count, 'results/basic_statistics.csv')