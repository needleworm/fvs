"""
Author : Byunghyun Ban
SBIE
needleworm@Kaist.ac.kr
"""

import numpy as np


class Network:
    n = 0
    matrix = []
    nodes = []

    def __init__(self, node_file, network_file):
        self.matrix = []
        self.nodes = []
        self._update(node_file, network_file)
        self._trim_none_feedback_nodes()

    def _update(self, node_file, network_file):
        print("initiation.....")
        f_node = open("networks/" + node_file)
        f_network = open("networks/" + network_file)
        print("Network Reading...")
        for line in f_node:
            node = line.strip()
            if node:
                self.nodes.append(node)
        self.n = len(self.nodes)
        self.matrix = np.zeros((self.n, self.n), dtype="bool")

        for line in f_network:
            if line.strip():
                split = line.strip().split(',')
                source = split[0].strip()
                target = split[1].strip()
                if (source not in self.nodes) or (target not in self.nodes):
                    print("\nError Occured!\nplease check if both " + source + " and " +
                          target + " are listed in your node file.\n")
                    exit(1)
                self.matrix[self.nodes.index(source), self.nodes.index(target)] = True
        f_node.close()
        f_network.close()
        print("Adjacency Matrix Done")

    def _trim_none_feedback_nodes(self):
        count = 0
        while 1:
            idx = self._is_there_none_feedback_node()
            if idx < 0:
                print("There are " + str(count) + " none-feedback node exist!")
                if count > 0:
                    print("All none-feedback nodes are removed from the network.")
                return
            self._remove_node_from_network(idx)
            count += 1

    def _remove_node_from_network(self, idx):
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

    def remove_nodes(self, combination, size):
        modified_matrix = np.array(self.matrix)
        for i in range(size):
            if combination[i]:
                modified_matrix[i,:] = False
                modified_matrix[:,i] = False
        return modified_matrix
