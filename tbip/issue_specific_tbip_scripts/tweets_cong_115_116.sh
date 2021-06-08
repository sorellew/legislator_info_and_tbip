salloc --constraint=gpu-small --exclusive srun /workspace/.conda/envs/tbip/bin/python pytorch/tbip_issue_specific.py --data=tweets_cong_115_116 --max_steps=500000 --batch_size=1024
