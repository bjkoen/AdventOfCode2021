# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 11:09:21 2021

@author: Bouke
"""

with open("input-day12.txt", "r") as f:
    input = f.readlines()

# input = ['dc-end', #slightly larger example
# 'HN-start',
# 'start-kj',
# 'dc-start',
# 'dc-HN',
# 'LN-dc',
# 'HN-end',
# 'kj-sa',
# 'kj-HN',
# 'kj-dc']

# input = ['fs-end', #even larger example
# 'he-DX',
# 'fs-he',
# 'start-DX',
# 'pj-DX',
# 'end-zg',
# 'zg-sl',
# 'zg-pj',
# 'pj-he',
# 'RW-he',
# 'fs-DX',
# 'pj-RW',
# 'zg-RW',
# 'start-pj',
# 'he-WI',
# 'zg-he',
# 'pj-fs',
# 'start-RW']

  
import networkx as nx
# load input data into network x graph object; alternatively: use pyvis.network 
G = nx.read_edgelist(input, delimiter='-')
nx.draw_networkx(G) # visualize network

nodes_dict = nx.to_dict_of_lists(G)

#%% Part1 
# valid_paths = []
# def crawl(path=['start']):
#     if path[-1] == "end":
#         global valid_paths
#         valid_paths += [path]
#     elif path[-1].islower() and path.count(path[-1]) > 1:
#         pass
#     else:
#         for nextnode in nodes_dict[path[-1]]:
#             crawl(path+[nextnode])
    
# crawl()
# print('Answer part 1 is', len(valid_paths))


#%% Part 2

valid_paths = []
def crawl2(path=['start']):
    if path[-1] == "end":
        global valid_paths
        valid_paths += [path]
    elif path[-1] == "start" and len(path) > 1:
        pass
    elif path[-1].islower() and path.count(path[-1]) > 1 and path[0] == "start":
        path[0] = "start_first_strike"
        for nextnode in nodes_dict[path[-1]]:
            crawl2(path+[nextnode])
    elif path[-1].islower() and path.count(path[-1]) > 1 and not path[0] == "start":  
        pass
    else:
        for nextnode in nodes_dict[path[-1]]:
            crawl2(path+[nextnode])
    
crawl2()
print('Answer part 2 is', len(valid_paths))