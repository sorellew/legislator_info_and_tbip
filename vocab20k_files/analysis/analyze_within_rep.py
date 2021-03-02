# coding: utf-8
import os
import numpy as np
import analysis_utils as utils
import pandas as pd

project_dir = os.path.abspath(os.path.join(os.path.dirname('.'), os.pardir))
source_dir = os.path.join(project_dir, "data/republicans_tea_party_vs_rest")
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
get_ipython().run_line_magic('store', 'topic_out >within_rep_topics.txt')
'''
df = pd.read_csv('/workspace/pranav/scholar/data/republican_speeches_tea_party_2005_2012/republican_speeches_tea-party-labelled_cong-111-to-112_thresh95.csv')
names = list(df['name'])
labels = list(df['tea_party_label'])
#set(labels)
tp_names, nontp_names = [], []
for name, label in zip(names, labels):
    if label==1:
        tp_names.append(name + ' {tea-party}')
    else:
        nontp_names.append(name)
    
ideal_point_vals_tp, ideal_point_vals_nontp = [], []
tp_names = list(set(tp_names))
nontp_names = list(set(nontp_names))
for name in tp_names:
    name = name.split(' {')[0]
    ideal_point_vals_tp.append(ideal_point_mean[np.where(author_map == name)[0][0]])
        
for name in nontp_names:
    #name = name.split(' {')[0]
    ideal_point_vals_nontp.append(ideal_point_mean[np.where(author_map == name)[0][0]])
    
print('For Tea-Partiers, MEAN ideal point value is = ' + str(round(np.mean(ideal_point_vals_tp), 4)))
print('For Non-Tea-Party, MEAN ideal point value is = ' + str(round(np.mean(ideal_point_vals_nontp), 4)))
print('\n')
print('For Tea-Partiers, MEDIAN ideal point value is = ' + str(round(np.median(ideal_point_vals_tp), 4)))
print('For Non-Tea-Party, MEDIAN ideal point value is = ' + str(round(np.median(ideal_point_vals_nontp), 4)))
print('\n')
print('For Tea-Partiers, MAX ideal point value is = ' + str(round(np.max(ideal_point_vals_tp), 4)))
print('For Non-Tea-Party, MAX ideal point value is = ' + str(round(np.max(ideal_point_vals_nontp), 4)))
print('\n')
print('For Tea-Partiers, MIN ideal point value is = ' + str(round(np.min(ideal_point_vals_tp), 4)))
print('For Non-Tea-Party, MIN ideal point value is = ' + str(round(np.min(ideal_point_vals_nontp), 4)))
print('\n---\n')

all_names = tp_names + nontp_names
all_ideal_point_vals = ideal_point_vals_tp + ideal_point_vals_nontp
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
    
