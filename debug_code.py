
'''
import os
import numpy as np
import lmdb
import torch
from torch.utils.data import Dataset
import tqdm
import pandas as pd
from utils.protein_ligand import PDBProtein, parse_sdf_file
from utils.data import ProteinLigandData, torchify_dict
df = pd.read_pickle('data/crossdocked_pocket10/index.pkl')
sample_index = []
for x in df:
    if x[0] is None:
        continue
    if x[0].split('/')[0] in ['1A1C_MALDO_2_433_0', '1A1D_CYBSA_1_341_0', '1B57_HUMAN_25_300_0', '3HAO_CUPMC_1_172_0']:
        sample_index.append(x)
with open('data/crossdocked_pocket10/sample_index.pkl', 'wb') as f:
    pickle.dump(sample_index, f)

split = torch.load('data/split_by_name.pt')
trs = []
tes = []
for x in split['train']:
    tem = x[0].split('/')[0]
    if tem in ['1A1C_MALDO_2_433_0', '1A1D_CYBSA_1_341_0', '1B57_HUMAN_25_300_0']:
        trs.append(x)
    elif tem in ['3HAO_CUPMC_1_172_0']:
        tes.append(x)
sample_split = {'train': trs, 'test': tes}
torch.save(sample_split, 'data/split_by_name1.pt')




df = pd.read_pickle('data/crossdocked_pocket10/index.pkl')
index = df[0]
i=0
pocket_fn, ligand_fn, _, rmsd_str = index
ligand_dict = parse_sdf_file(os.path.join('./data/crossdocked_pocket10/', ligand_fn))
pocket_dict = PDBProtein(os.path.join('./data/crossdocked_pocket10/', pocket_fn)).to_dict_atom_cutoff(ligand_pos, 8.0)
# numpy版本问题导致的np.long, np.int, np.bool等无法使用，更正为np.longlong, np.int_, np.bool_
# 加工数据的代码：utils/dataset/pl.py 89-104行
'''




'''
C:\Users\xwk\PycharmProjects\funcgroupDD\models\epsnet\MDM_pocket_coor_shared.py 90-91行 num_atom参数，如果不指定，会默认为8，
跑crossdock2020时bug， 需要在参数文件model部分加上num_atom: 10

'''