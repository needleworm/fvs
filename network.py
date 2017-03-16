"""
Author : Byunghyun Ban
sbie.kaist.ac.kr
needleworm@Kaist.ac.kr

Korea Advanced Institute of Science and Technology
"""

import numpy as np


class Network:
    n = 0
    matrix = []
    nodes = []
    none_feedback = []

    def __init__(self, network_file, matrix=False):
        if matrix:
            self._pseudo_update(network_file)
        else:
            self._update(network_file)
        self.trim_none_feedback_nodes()

    def _pseudo_update(self, matrix):
        self.matrix = matrix
        a, b = matrix.shape
        self.n = a

    def _update(self, network_file):
        print("initiation.....")
        f_nodes = open("networks/" + network_file, 'r')
        print("Network Reading...")
        splits = []
        for line in f_nodes:
            if line.strip():
                split = line.strip().split(',')
                splits.append(split)
                if split[0].strip() not in self.nodes:
                    self.nodes.append(split[0].strip())
                if split[1].strip() not in self.nodes:
                    self.nodes.append(split[1].strip())
        f_nodes.close()
        self.n = len(self.nodes)
        print("This network has " + str(self.n) + " Nodes")
        self.matrix = np.zeros((self.n, self.n), dtype="bool")

        for split in splits:
            source = split[0].strip()
            target = split[1].strip()
            if (source not in self.nodes) or (target not in self.nodes):
                print("\nError Occured!\nplease check if both " + source + " and " +
                      target + " are listed in your node file.\n")
                exit(1)
            self.matrix[self.nodes.index(source), self.nodes.index(target)] = True
        print("Adjacency Matrix Done")

    def trim_none_feedback_nodes(self):
        count = 0
        while 1:
            idx = self._is_there_none_feedback_node()
            if idx < 0:
                print("There are " + str(count) + " none-feedback node exist!")
                if count > 0:
                    print("All none-feedback nodes are removed from the network.")
                return
            if self.nodes[idx] not in self.none_feedback:
                self.none_feedback.append(self.nodes[idx])
            self.remove_node_from_network(idx)
            count += 1

    def remove_node_from_network(self, idx):
        self.n -= 1
        new_matrix = np.zeros((self.n, self.n), dtype='bool')
        y = 0
        for i in range(self.n + 1):
            x = 0
            for j in range(self.n + 1):
                if i != idx and j != idx:
                    new_matrix[y][x] = self.matrix[i][j]
                    x += 1
            if i != idx:
                y += 1
        self.nodes.remove(self.nodes[idx])
        self.matrix = new_matrix

    def _is_there_none_feedback_node(self):
        for i in range(self.n):
            if np.sum(self.matrix[:, i]) == 0 or np.sum(self.matrix[i,:]) == 0:
                return i
        return -1

    def remove_nodes(self, combination):
        modified_matrix = np.array(self.matrix, dtype='bool')
        for i in combination:
            modified_matrix[i, :] = False
            modified_matrix[:, i] = False
        return modified_matrix
