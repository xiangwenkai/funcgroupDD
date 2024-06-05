# Function group based drug design

### Create environment
```
# create in wsl unbtun-20.4
conda create -n fgdd python==3.9
conda activate fgdd
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia
pip install torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-2.1.0+cu121.html
pip install torch_geometric
pip install rdkit
conda install -c conda-forge openbabel=3.1.1 -y
pip install rdkit
pip install easydict
pip install tensorboard
pip install lmdb
pip install einops
pip install oddt

# copy to slurm
conda create -n fgddc --clone /cluster/home/wenkai/envs/fgdd
```


### dataset  
#### crossDOCK2020  
https://github.com/gnina/models/tree/master/data/CrossDocked2020

### note
code: IFG.py  
reference: An algorithm to identify functional groups in organic molecules  
usage: find function groups and draw them  

### train command
```
python -u train.py --config configs/crossdock_epoch.yml
```

