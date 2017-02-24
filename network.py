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
        f_node = open(node_file)
        f_network = open(network_file)

        for line in f_node:
            node = line.strip()
            if node:
                self.nodes.append(node)

        n = len(self.nodes)
        self.matrix = np.zeros((n, n), dtype="bool")



