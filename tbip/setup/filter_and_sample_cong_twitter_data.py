# coding: utf-8
import pandas as pd
import numpy as np
full_df = pd.read_csv('data/tweets_cong_115_116/all_tweets_df.csv')
full_df.info()
removed_retweets_df = full_df[full_df['Text'].apply(lambda x: x[:3] != 'RT ')]
removed_retweets_df.info()
removed_retweets_df.head()
removed_retweets_df.head(10)
removed_retweets_df.tail(10)
removed_retweets_df['Text'].tail(10)
filtered_df = removed_retweets_df[removed_retweets_df['Text'].apply(lambda x: len(x.split()) >= 5)]
filtered_df.info()
filtered_df.tail(10)
filtered_df['Text'].tail(10)
relev_uids = list(np.load('data/tweets_cong_115_116/relevant_twitter_uids.npy'))
relev_uids = list(np.load('data/tweets_cong_115_116/raw/relevant_twitter_uids.npy'))
filtered_df = filtered_df[filtered_df['Author ID'].isin(relev_uids)]
filtered_df.info()
N = len(filtered_df)
from tqdm import tqdm
all_authors = list(set(filtered_df['Author ID']))
author_to_num_tweets = {}
for a in tqdm(all_authors):
    author_to_num_tweets[a] = len(filtered_df[filtered_df['Author ID']==a])
    
list_of_dfs = []
for a in tqdm(all_authors):
    sample_size = max(round(300000 * (author_to_num_tweets[a]/N)), 1)
    temp_df = filtered_df[filtered_df['Author ID']==a]
    list_of_dfs.append(temp_df.sample(n = sample_size, random_state = 1, axis = 0))
    del temp_df
    
len(all_authors)
len(list_of_dfs)
sampled_df = pd.concat(list_of_dfs)
sampled_df = sampled_df.sample(frac=1, random_state = 1, axis = 0)
sampled_df.info()
sampled_df.to_csv('data/tweets_cong_115_116_sampled/sampled_twitter_data.csv', index=False)
