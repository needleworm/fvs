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
                split = line.split(',')
                source = split[0].strip()
                target = split[1].strip()
                if (source not in self.nodes) or (target not in self.nodes):
                    print("\nError Occured!\nplease check if both " + source + " and " +
                          target + "are listed in your node file.\n")
                    exit(1)
                self.matrix[self.nodes.index(source), self.nodes.index(target)] = True
        f_node.close()
        f_network.close()
        print("Adjacency Matrix Done")

    def remove_nodes(self, combination, size):
        modified_matrix = np.array(self.matrix)
        for i in range(size):
            if combination[i]:
                modified_matrix[i,:] = False
                modified_matrix[:,i] = False
        return modified_matrix
