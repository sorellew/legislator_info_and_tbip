# coding: utf-8
import os
import numpy as np
import analysis_utils as utils
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) 
project_dir = os.path.abspath(os.path.join(os.path.dirname('.'), os.pardir)) 
project_dir
source_dir = os.path.join(project_dir, "data/republicans_tea_party_vs_rest_2009_2012")
source_dir_rep = os.path.join(project_dir, "data/republicans_tea_party_vs_rest_2009_2012")
del source_dir
source_dir_dem = os.path.join(project_dir, "data/democrats_progressive_vs_rest")
data_dir_rep = os.path.join(source_dir_rep, "clean")
data_dir_dem = os.path.join(source_dir_dem, "clean")
(counts_rep, vocabulary_rep, author_indices_rep, author_map_rep, raw_documents_rep) = utils.load_text_data(data_dir_rep) 
import scipy.sparse as sparse
from scipy.stats import bernoulli, poisson
counts_rep = sparse.load_npz(os.path.join(data_dir_rep, "counts.npz"))
vocabulary_rep = np.loadtxt(os.path.join(data_dir_rep, "vocabulary.txt"), dtype=str, delimiter="\n", comments="<!-")
author_indices_rep = np.load(os.path.join(data_dir_rep, "author_indices.npy")).astype(np.int32) 
author_map_rep = np.loadtxt(os.path.join(data_dir_rep, "author_map.txt"), dtype=str, delimiter="\n")
counts_dem = sparse.load_npz(os.path.join(data_dir_dem, "counts.npz"))
vocabulary_dem = np.loadtxt(os.path.join(data_dir_dem, "vocabulary.txt"), dtype=str, delimiter="\n", comments="<!-")
author_indices_dem = np.load(os.path.join(data_dir_dem, "author_indices.npy")).astype(np.int32) 
author_map_dem = np.loadtxt(os.path.join(data_dir_dem, "author_map.txt"), dtype=str, delimiter="\n")
param_dir_rep = os.path.join(source_dir_rep, "tbip-fits/params/")
(document_loc_rep, document_scale_rep, objective_topic_loc_rep, objective_topic_scale_rep, 
ideological_topic_loc_rep, ideological_topic_scale_rep, ideal_point_loc_rep, 
ideal_point_scale_rep) = utils.load_tbip_parameters(param_dir_rep)
param_dir_dem = os.path.join(source_dir_dem, "tbip-fits/params/")
(document_loc_dem, document_scale_dem, objective_topic_loc_dem, objective_topic_scale_dem, 
ideological_topic_loc_dem, ideological_topic_scale_dem, ideal_point_loc_dem, 
ideal_point_scale_dem) = utils.load_tbip_parameters(param_dir_dem)
document_mean_rep = np.exp(document_loc_rep + document_scale_rep ** 2 / 2)
objective_topic_mean_rep = np.exp(objective_topic_loc_rep + objective_topic_scale_rep ** 2 / 2)
ideological_topic_mean_rep = ideological_topic_loc_rep
ideal_point_mean_rep = ideal_point_loc_rep
document_mean_dem = np.exp(document_loc_dem + document_scale_dem ** 2 / 2)
objective_topic_mean_dem = np.exp(objective_topic_loc_dem + objective_topic_scale_dem ** 2 / 2)
ideological_topic_mean_dem = ideological_topic_loc_dem
ideal_point_mean_dem = ideal_point_loc_dem
len(ideal_point_mean_dem)
len(ideal_point_mean_rep)
ideal_point_mean_dem
ideal_point_mean_rep
prog_index = np.where(author_map_dem == "progressive")[0][0]
prog_index
ideal_point_mean_dem[prog_index]
get_ipython().run_line_magic('clear', '')
ideal_point_mean_dem[np.where(author_map_dem == "progressive")[0][0]]
ideal_point_mean_dem[np.where(author_map_dem == "not_progressive")[0][0]]
ideal_point_mean_rep[np.where(author_map_rep == "teaparty")[0][0]]
ideal_point_mean_rep[np.where(author_map_rep == "not_teaparty")[0][0]]
utils.print_topics(objective_topic_loc_dem, objective_topic_scale_dem, ideological_topic_loc_dem, ideological_topic_scale_dem, vocabulary_dem)
get_ipython().run_line_magic('save', '../tbip/within_dem_topics.txt _')
get_ipython().run_line_magic('save', '../tbip/within_dem_topics.txt _oh[48]')
utils.print_topics(objective_topic_loc_dem, objective_topic_scale_dem, ideological_topic_loc_dem, ideological_topic_scale_dem, vocabulary_dem)
get_ipython().run_cell_magic('capture', 'dem_output', 'utils.print_topics(objective_topic_loc_dem, objective_topic_scale_dem, ideological_topic_loc_dem, ideological_topic_scale_dem, vocabulary_dem)\n\n')
dem = dem_output.stdout
get_ipython().run_line_magic('store', 'dem > ../tbip/within_dem_topics.txt')
get_ipython().system('pwd')
get_ipython().run_line_magic('store', 'dem > "../tbip/within_dem_topics.txt"')
get_ipython().run_line_magic('store', 'dem > within_dem_topics.txt')
get_ipython().run_line_magic('store', 'dem >within_dem_topics.txt')
get_ipython().run_cell_magic('capture', 'rep_output', 'utils.print_topics(objective_topic_loc_rep, objective_topic_scale_rep, ideological_topic_loc_rep, ideological_topic_scale_rep, vocabulary_rep)\n\n\n\n')
rep = rep_output.stdout
get_ipython().run_line_magic('store', 'rep >within_rep_topics.txt')
get_ipython().run_line_magic('clear', '')
ideal_point_mean_dem[np.where(author_map_dem == "progressive")[0][0]]
ideal_point_mean_dem[np.where(author_map_dem == "not_progressive")[0][0]]
ideal_point_mean_rep[np.where(author_map_rep == "teaparty")[0][0]]
ideal_point_mean_rep[np.where(author_map_rep == "not_teaparty")[0][0]]
get_ipython().run_cell_magic('capture', 'rep_output', 'utils.print_topics(objective_topic_loc_rep, objective_topic_scale_rep, ideological_topic_loc_rep, ideological_topic_scale_rep, vocabulary_rep, 15)\n\n\n\n\n\n')
rep = rep_output.stdout
get_ipython().run_line_magic('store', 'rep >within_rep_topics.txt')
