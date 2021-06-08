salloc --constraint=gpu-small --exclusive srun /workspace/.conda/envs/tbip/bin/python pytorch/tbip.py --data=senate-speeches-114 --max_steps=150000 --counts_transformation=log --batch_size=512
