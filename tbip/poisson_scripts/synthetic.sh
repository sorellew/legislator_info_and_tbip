salloc --constraint=cpu-med --exclusive srun /workspace/.conda/envs/tbip/bin/python setup/poisson_factorization.py --data=synthetic --num_topics=3 --max_steps=300 --seed=199
