salloc --constraint=gpu-small --exclusive srun /workspace/.conda/envs/tbip/bin/python pytorch/tbip.py --data=tweets_cong_115_116 --max_steps=200000 --batch_size=1024
