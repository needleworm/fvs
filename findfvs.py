"""
Author : Byunghyun Ban
SBIE
needleworm@Kaist.ac.kr
"""
import numpy as np
import network as nt
import time

class FVSFinder:
    feedback_vertex_set = {}
    n = 0
    current_size = 0
    network = None
    nodes = []
    combinations = []
    single_comb = []
    self_feedback = []

    def __init__(self, node_file, anno_file, find_minimal_only=True, checker=False, fvs_found = []):
        self.network = nt.Network(node_file, anno_file)
        self.n = self.network.n
        self.nodes = self.network.nodes
        if checker:
            self.checker(fvs_found)
        elif find_minimal_only:
            print("\nFinding Minimal Feedback Vertex Sets\n")
            self.find_minimal_fvs()
        else:
            print("\nFinding All Feedback Vertex Sets\n")
            self._combinations()
            self.find_all_fvs()

#    def checker(self, fvs_found):
#        for node in fvs_found:

    def find_minimal_fvs(self):
        before = time.time()
        fvs, size = self._find_minimal_fvs()
        print("All process Done!")
        print("Total " + str(time.time() - before) + " seconds spent for overall process.\n")
        if not fvs:
            print("Something is Wrong. Cannot find any FVS")
            exit(1)
        print("Size of minimal FVS is " + str(size) + '.')
        print("Total " + str(len(fvs)) + " minimal FVS exists.\n")
        out = open("result/Minimal_FVS.txt", 'w')
        for i, fv in enumerate(fvs):
            out.write(str(fv))
            if i != len(fvs) -1:
                out.write('\n')
        out.close()

    def _single_combination(self, n, r):
        combinations = []
        temp = list(np.zeros(self.n, dtype="int"))
        self._combination_generator(temp, 0, n, r, 0, r)
        for comb in self.single_comb:
            combi = np.zeros(n, dtype='bool')
            for el in comb:
                combi[el] = True
            temp = []
            for el in combi:
                temp.append(el)
            combinations.append(temp)
        self.single_comb = []
        return combinations

    def _comb_mody(self, comb, self_feedback):
        for i, combi in enumerate(comb):
            temp = []
            for val in combi:
                temp.append(val)
            for idx in self_feedback:
                temp.insert(idx, True)
            comb[i] = temp
        return comb

    def _combination_generator(self, lst, index, n, r, target, R):
        if r == 0:
            self.single_comb.append(list(lst[:R]))
        elif target == n:
            return
        else:
            lst[index] = target
            self._combination_generator(lst, index + 1, n, r - 1, target + 1, R)
            self._combination_generator(lst, index, n, r, target + 1, R)

    def _find_self_feedback(self):
        idx = []
        for i in range(self.n):
            if self.network.matrix[i][i]:
                self.self_feedback.append(i)
            else:
                idx.append(i)
        return idx

    def _find_minimal_fvs(self):
        idx = self._find_self_feedback()
        fvs = []
        before = time.time()

        if self.self_feedback:
            print("There are " + str(len(self.self_feedback)) + " self-feedback nodes on the network.\n\n")

        print("********** Starting Main Process **********\n")
        for i in range(self.n - len(self.self_feedback)):
            before_time = time.time()
            print("Checking if size " + str(i + len(self.self_feedback) + 1) + " FVS exists.")
            combination = self._single_combination(self.n - len(self.self_feedback), i + 1)
            if self.self_feedback:
                combination = self._comb_mody(combination, self.self_feedback)
            fvs = self._find_feedback_vertex_sets(combination)
            if fvs:
                print(str(time.time() - before) + " seconds spent for Finding Minimal FVS.\n")
                return fvs, i + len(self.self_feedback) + 1
            print("Size " + str(i + len(self.self_feedback) + 1) + " FVS Doesn't Exist.")
            print(str(time.time() - before_time) + " seconds spent for this step.\n")
        return fvs, 0

    def _is_there_cycle(self, matrix):
        for i in range(self.n):
            matrix[i, i] = False
        graph = {}
        for i in range(self.n):
            target = []
            for j in range(self.n):
                if matrix[i, j]:
                    target.append(j)
            graph[i] = target

        truth = False
        for i in range(self.n):
            if graph[i]:
                truth += self._dfs_cycle(graph, i)
        return truth

    @staticmethod
    def _dfs_cycle(graph, root):
        stack = []
        visited = []
        stack.append(root)

        while stack:
            top = stack.pop()
            visited.append(top)
            if set(visited) & set(graph[top]):
                return True
            targets = list(set(graph[top]) - set(visited))
            targets.sort()
            stack.extend(targets)

        return False

    def _find_feedback_vertex_sets(self, combinations):
        FVS = []
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
        print("********************\n")
        print("Currently Updating This Method. Please use Old Version If you want to find All FVS.")
        print("********************\n")
