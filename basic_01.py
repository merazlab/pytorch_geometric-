import torch
from torch_geometric.data import Data
from torch_geometric.datasets import TUDataset

dataset = TUDataset(root='./tmp/ENZYMES', name='ENZYMES')