# coding: utf-8
import os
import numpy as np
import analysis_utils as utils
import pandas as pd

project_dir = os.path.abspath(os.path.join(os.path.dirname('.'), os.pardir))
source_dir = os.path.join(project_dir, "data/democrats_progressive_vs_rest")
data_dir = os.path.join(source_dir, "clean")
(counts, vocabulary, author_indices, author_map, raw_documents) = utils.load_text_data(data_dir)

param_dir = os.path.join(source_dir, "tbip-pytorch-fits/params/")
(document_loc, document_scale, objective_topic_loc, objective_topic_scale, 
 ideological_topic_loc, ideological_topic_scale, ideal_point_loc, 
  ideal_point_scale) = utils.load_tbip_parameters(param_dir)

document_mean = np.exp(document_loc + document_scale ** 2 / 2)
objective_topic_mean = np.exp(objective_topic_loc + 
                              objective_topic_scale ** 2 / 2)
ideological_topic_mean = ideological_topic_loc
ideal_point_mean = ideal_point_loc

''' save output of topics in ipython 
get_ipython().run_cell_magic('capture', 'topic_print_out', 'utils.print_topics(objective_topic_loc, objective_topic_scale, ideological_topic_loc, ideological_topic_scale, vocabulary, 20)\n\n')
topic_out = topic_print_out.stdout
get_ipython().run_line_magic('store', 'topic_out >within_dem_topics.txt')
'''
df = pd.read_csv('/workspace/pranav/scholar/data/democrats_progressive_vs_rest/democrats_prog_vs_rest_prog_label_consistent.csv')
names = list(df['name'])
labels = list(df['label'])
#set(labels)
prog_names, nonprog_names = [], []
for name, label in zip(names, labels):
    if label==1:
        prog_names.append(name + ' {prog}')
    else:
        nonprog_names.append(name)
    
ideal_point_vals_prog, ideal_point_vals_nonprog = [], []
prog_names = list(set(prog_names))
nonprog_names = list(set(nonprog_names))
for name in prog_names:
    name = name.split(' {')[0]
    ideal_point_vals_prog.append(ideal_point_mean[np.where(author_map == name)[0][0]])
        
for name in nonprog_names:
    #name = name.split(' {')[0]
    ideal_point_vals_nonprog.append(ideal_point_mean[np.where(author_map == name)[0][0]])
    
print('For Progressives, MEAN ideal point value is = ' + str(round(np.mean(ideal_point_vals_prog), 4)))
print('For Non-Progressives, MEAN ideal point value is = ' + str(round(np.mean(ideal_point_vals_nonprog), 4)))
print('\n')
print('For Progressives, MEDIAN ideal point value is = ' + str(round(np.median(ideal_point_vals_prog), 4)))
print('For Non-Progressives, MEDIAN ideal point value is = ' + str(round(np.median(ideal_point_vals_nonprog), 4)))
print('\n')
print('For Progressives, MAX ideal point value is = ' + str(round(np.max(ideal_point_vals_prog), 4)))
print('For Non-Progressives, MAX ideal point value is = ' + str(round(np.max(ideal_point_vals_nonprog), 4)))
print('\n')
print('For Progressives, MIN ideal point value is = ' + str(round(np.min(ideal_point_vals_prog), 4)))
print('For Non-Progressives, MIN ideal point value is = ' + str(round(np.min(ideal_point_vals_nonprog), 4)))
print('\n---\n')

all_names = prog_names + nonprog_names
all_ideal_point_vals = ideal_point_vals_prog + ideal_point_vals_nonprog
assert len(all_ideal_point_vals) == len(all_names)

top_20_inds = np.argsort(all_ideal_point_vals)[::-1][:20]
bottom_20_inds = np.argsort(all_ideal_point_vals)[:20]

print('Highest Ideal Points\n')
for i in top_20_inds:
    print(all_names[i] + '\t' + str(all_ideal_point_vals[i]))
print('\n--\n')    
print('Lowest Ideal Points\n')
for i in bottom_20_inds:
    print(all_names[i] + '\t' + str(all_ideal_point_vals[i]))
    
