salloc --constraint=gpu-small --exclusive srun /workspace/.conda/envs/tbip/bin/python pytorch/tbip.py --data=synthetic --num_topics=3 --max_steps=20000 --counts_transformation=log batch_size=3
