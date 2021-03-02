# coding: utf-8
import os
import numpy as np
import analysis_utils as utils
import pandas as pd
get_ipython().run_line_magic('cd', 'analysis/')
import analysis_utils as utils
author_info = pd.read_csv('../data/senate-speeches-114/author_info.csv')
author_info.info()
(counts, vocabulary, author_indices, author_map) = utils.load_text_data(data_dir)
source_dir = os.path.join(project_dir, "data/senate-speeches-114")
project_dir = os.path.abspath(os.path.join(os.path.dirname('.'), os.pardir))
source_dir = os.path.join(project_dir, "data/senate-speeches-114")
data_dir = os.path.join(source_dir, "clean")
(counts, vocabulary, author_indices, author_map) = utils.load_text_data(data_dir)
param_dir = os.path.join(source_dir, "tbip-pytorch-fits/params/")
(document_loc, document_scale, objective_topic_loc, objective_topic_scale,
 ideological_topic_loc, ideological_topic_scale, ideal_point_loc,
   ideal_point_scale) = utils.load_tbip_parameters(param_dir)
document_mean = np.exp(document_loc + document_scale ** 2 / 2)
objective_topic_mean = np.exp(objective_topic_loc +
                              objective_topic_scale ** 2 / 2)
ideological_topic_mean = ideological_topic_loc
ideal_point_mean = ideal_point_loc
ideal_point_vals = []
author_names = list(author_info['Name (Party)'])
for x in author_names:
    ideal_point_vals.append(ideal_point_mean[np.where(author_map == x)[0][0]])
    
len(ideal_point_vals)
author_info['speeches_based_ideal_point_val'] = ideal_point_vals
author_info.info()
author_info.to_csv('../data/senate-speeches-114/author_info_plus_tbip.csv', index=False)
nominate_scores = list(author_info['DW-Nom 1'])
state_pres_vs_2012 = list(author_info['State Democrat Presidential VoteShare 2012'])
state_pres_vs_2016 = list(author_info['State Democrat Presidential VoteShare 2016'])
nominate_speeches_corr = np.corrcoef(nominate_scores, ideal_point_vals)[0][1]
nominate_speeches_corr
author_info.head()
author_names[0]
ideal_point_mean[np.where(author_map == "Alan Franken (D)")[0][0]]
ideal_point_mean[np.where(author_map == "Bernard Sanders (I)")[0][0]]
ideal_point_mean[np.where(author_map == "Jefferson Sessions (R)")[0][0]]
ideal_point_vals = []
for x in author_names:
    ideal_point_vals.append(ideal_point_mean[np.where(author_map == x)[0][0]])
    
ideal_point_vals = []
for x in author_names:
    ideal_point_vals.append(-1*ideal_point_mean[np.where(author_map == x)[0][0]])
    
author_info['speeches_based_ideal_point_val'] = ideal_point_vals
author_info.head()
author_info.to_csv('../data/senate-speeches-114/author_info_plus_tbip.csv', index=False)
nominate_speeches_corr = np.corrcoef(nominate_scores, ideal_point_vals)[0][1]
nominate_speeches_corr
nominate_state_2012_corr = np.corrcoef(nominate_scores, state_pres_vs_2012)[0][1]
nominate_state_2012_corr
nominate_state_2012_corr = np.corrcoef(nominate_scores, state_pres_vs_2016)[0][1]
nominate_state_2016_corr = np.corrcoef(nominate_scores, state_pres_vs_2016)[0][1]
nominate_state_2016_corr
speeches_state_2012_corr = np.corrcoef(ideal_point_vals, state_pres_vs_2012)[0][1]
speeches_state_2012_corr
speeches_state_2016_corr = np.corrcoef(ideal_point_vals, state_pres_vs_2016)[0][1]
speeches_state_2016_corr
