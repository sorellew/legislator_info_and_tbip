# Text-Based Ideal Points Model (Code and Data)

**First, please read the README at the original TBIP repo (https://github.com/keyonvafa/tbip) to get the required overview, and install the required libraries (pip install -r requirements.txt) in your environment. It is important to understand the data files and basic structure from the original TBIP code as this directory directly builds from that!** 

## Data

There are four datasets currently included. Let them be denoted by the variable \<dataset\>, which can take on four values: 
  
  1. **floor_speeches_congs_115_116**
  2. **senate-speeches-114**
  3. **synthetic**
  4. **tweets_cong_115_116**

Each of the four data/\<dataset\> directories contain the data/\<dataset\>/clean/ folders that are the input directories for running the TBIP code. 
  
Note that the results of running TBIP code (whether it is the initial step of running poisson factorization, or the main tbip code) also gets stored in the respective data/\<dataset\> directory. 
  
#### From raw data to clean data
  
  For the floor_speeches_congs_115_116 and tweets_cong_115_116 datasets, the raw data file and the code to use it and produce the preprocessed data stored in the respective clean/ directory can be found in the respective data directories (the code is present as a jupyter notebook). 
  
  For the senate-speeches-114 dataset, the clean/ and pf-fits/ (result of running poisson factorization code on the clean data) directory are provided by the authors directly. 
  
  For the synthetic dataset, the code for producing this synthetic data is included as a jupyter notebook. 
  

## Running TBIP
  
  There are two steps involved: 
  
  1. Running poisson factorization
  2. Running the TBIP main code (either original or issue-specific variant)
  
  (The commands used are provided as scripts and run on specific aws cluster, but the commands themselves can be run starting from python ... essentially, to run it anywhere other than aws or a different aws, just use the part of the command starting from python ...)
  
  For a specific \<dataset\>, run poisson_scripts/\<dataset\>.sh first
  
  Then, run original_tbip_scripts/\<dataset\>.sh and/or issue_specific_tbip_scripts/\<dataset\>.sh for the original TBIP code or the issue-specific TBIP code respectively. 
  
**All scripts must be run so that the command is running from the main project directory (i.e. this tbip directory, not from a subdirectory).**
  
  The --max_steps can be modified for running quicker, it is not clear that having a lot of steps is beneficial. 
  
  
  ## Analysis/looking at the results
  
  These four jupyter notebooks show how to look at topics including getting the interactive visualization: analysis/analyze_floor_speeches_ideal_points.ipynb and analysis/analyze_floor_speeches_congs115-116_issue_specific.ipynb for floor speeches; analysis/analyze_tweet_ideal_points.ipynb and analysis/analyze_tweets_congs115-116_issue_specific.ipynb for tweets. 
  
  In particular, analyze_floor_speeches_ideal_points and analyze_tweet_ideal_points go all the way producing the different kinds of files in the final speech and tweet results in the parent directory. 
  
  ## Note on Stability of the Model
  
  The poisson factorization code is crucial in getting the topics, and in my observation, the topics do not change all that much (in terms of the themes discovered) when tbip code is run after it. That is, poisson factorization code is influential in issue discovery from the data. 
  It seems clear that for a fixed --seed, the results of poisson factorization are extremely stable - however, I have seen much better topics being discovered across seed settings. I used this to get better looking topics for a dataset, but a systemic investigation is pending. 
  
  While a systemic test needs to be carried out, my current thoughts are that after poisson factorization is run, the tbip or issue specific tbip values learned for authors are relatively stable across runs. This is only based on some runs on the same dataset and not noticing much difference, but definitely needs to be checked thoroughly. 
  
  
  
  
  
