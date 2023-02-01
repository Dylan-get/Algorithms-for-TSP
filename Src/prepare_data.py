import glob

import tsplib95
import numpy as np
import os.path as osp


class TSPDataset:
    def __init__(self,folder="/Users/xiaohai/Documents/tao_ducument/university/2022秋/高级算法/大作业/Algorithms-for-TSP/tsplib95/archives/problems/tsp"):
        self.folder=folder
        self.file_list=glob.glob(osp.join(folder,'*.tsp'))

    def __getitem__(self, index):
        path=self.file_list[index]
        problem = tsplib95.load(path)
        edge_weights = np.array(problem.edge_weights)
        n = edge_weights.shape[0]
        return n,edge_weights

    def __len__(self):
        return len(self.file_list)


if __name__ == '__main__':

    repo_root='../tsplib95'
    problem = tsplib95.load(osp.join(repo_root,'archives/problems/tsp/bays29.tsp'))

    edge_weights=problem.edge_weights
    edge_weights=np.array(edge_weights)
    print(edge_weights.shape)
    n=edge_weights.shape[0]

    for i in range(n):
        for j in range(n):
            assert edge_weights[i][j]==edge_weights[j][i]

            # print(f"{i} {j} :",edge_weights[i][j],' ',edge_weights[j][i])