"""
Author : Byunghyun Ban
SBIE
needleworm@Kaist.ac.kr
"""
import numpy as np
import network as nt

class FVSFinder:
    feedback_vertex_set = []
    n = 0
    current_size = 0
    network = None
    nodes = []

    def __init__(self, node_file, anno_file):
        self.network = nt.Network(node_file, anno_file)
        self.n = self.network.n
        self.nodes = self.network.nodes

    def _combinations(self, k):
        combinations = []
        comb_max = 2 ** self.n
        for i in range(comb_max):
            combination = self._dec_2_binary_combination(i)
            if sum(combination) == k:
                combinations.append(combination)
        return combinations

    def _dec_2_binary_combination(self, k):
        if not self.n:
            return []
        binary = str(bin(k))[2:]
        on_off = np.zeros(self.n, dtype="bool")
        for i in range(len(binary)):
            on_off[-i - 1] = int(binary[-i - 1])
            # nodes to be removed are marked as True
        return on_off

    def _is_there_self_cycle(self, matrix):
        for i in range(self.n):
            if matrix[i, i]:
                return True

    def _is_there_cycle(self, matrix):
        if self._is_there_self_cycle(matrix):
            return True
        for i in range(self.n):
            matrix[i, i] = False
        graph = {}
        for i in range(self.n):
            target = []
            for j in range(self.n):
                if matrix[i, j]:
                    target.append(j)
            graph[i] = target
        for i in range(self.n):
            if graph[i]:
                return self._dfs_cycle(graph, i)

    def _dfs_cycle(self, graph, root):
        stack = []
        visited = []
        stack.append(root)

        while(stack):
            top = stack.pop()
            visited.append(top)
            if set(visited) & set(graph[top]):
                return True
            targets = list(set(graph[top]) - set(visited))
            targets.sort()
            stack.extend(targets)

        return False

    def _find_feedback_vertex_sets(self, fvs_size):
        FVS = []
        combinations = self._combinations(fvs_size)
        for comb in combinations:
            matrix = self.network.remove_nodes(comb, self.n)
            if not self._is_there_cycle(matrix):
                fvs = []
                for i, bool in enumerate(comb):
                    if bool:
                        fvs.append(self.nodes[i])
                FVS.append(fvs)
        return FVS

    def find_all_fvs(self):
        for i in range(self.n + 1):
            if i == 0:
                continue
            fvs = self._find_feedback_vertex_sets(i)
            if not self.feedback_vertex_set:
                self.feedback_vertex_set.extend(fvs)
            else:
                FVS = []
                for fvs_earlier in self.feedback_vertex_set:
                    for fvs_current in fvs:
                        if set(fvs_earlier) | set(fvs_current) != set(fvs_current):
                            FVS.append(fvs_current)
                self.feedback_vertex_set.extend(FVS)

a = FVSFinder("nodes.txt", "annotation.txt")
a.find_all_fvs()
print(a.feedback_vertex_set)