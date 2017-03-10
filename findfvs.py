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

    def __init__(self, node_file, anno_file, find_minimal_only=True):
        self.network = nt.Network(node_file, anno_file)
        self.n = self.network.n
        self.nodes = self.network.nodes
        if find_minimal_only:
            self.find_minimal_fvs()
        else:
            self._combinations()
            self.find_all_fvs()

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

    def _find_minimal_fvs(self):
        idx = []
        self_feedback = []
        fvs = []
        before = time.time()
        for i in range(self.n):
            if self.network.matrix[i][i]:
                self_feedback.append(i)
            else:
                idx.append(i)

        for i in range(self.n - len(self_feedback)):
            combination = self._single_combination(self.n - len(self_feedback), i)
            if self_feedback:
                for j, comb in enumerate(combination):
                    if comb:
                        combination[j] = self._comb_mody(list(comb), self_feedback)
            fvs = self._find_feedback_vertex_sets(combination)
            if fvs:
                print(str(time.time() - before) + " seconds spent for Finding Minimal FVS.\n")
                return fvs, i + len(self_feedback)
        return fvs, 0

    def _combinations(self):
        combinations = {}
        before = time.time()
        for i in range(self.n + 1):
            combinations[i] = []
        comb_max = 2 ** self.n
        print("Total " + str(comb_max) + " kinds of combinations exits")
        for i in range(comb_max):
            if i % 400000 == 0:
                print(str(float(i) / comb_max * 100) + "% of combinations generated")
            combination = self._dec_2_binary_combination(i)
            idx = sum(combination)
            combinations[idx].append(combination)
        print(str(time.time() - before) + " seconds spent for combination\n")
        self.combinations = combinations

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

        truth = False
        for i in range(self.n):
            if graph[i]:
                truth += self._dfs_cycle(graph, i)
        return truth

    def _dfs_cycle(self, graph, root):
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
        out = open("All_FVS.txt", 'w')
        before = time.time()
        print("Combination Done")
        rng = self.n + 1
        for i in range(rng):
            temp = time.time()
            if i == 0:
                continue
            self.feedback_vertex_set[i] = self._find_feedback_vertex_sets(self.combinations[i])
            print("size " + str(i) + " FVS searching Done!")
            print(str(time.time() - temp) + " seconds spent for this step.\n")

        earlier = []
        for i in range(rng):
            if i == 0:
                continue
            if not earlier:
                earlier.extend(self.feedback_vertex_set[i])
                continue
            current = self.feedback_vertex_set[i]
            self.feedback_vertex_set[i] = []
            FVS = []
            onOff = np.ones(len(current), dtype='bool')

            for fvs_early in earlier:
                for p, fvs_current in enumerate(current):
                    if set(fvs_early) & set(fvs_current) == set(fvs_early):
                        onOff[p] *= 0
            for q in range(len(current)):
                if onOff[q]:
                    FVS.append(current[q])

            earlier.extend(FVS)
            self.feedback_vertex_set[i] = FVS

        for i in range(rng):
            if i == 0:
                continue
            for fvs in self.feedback_vertex_set[i]:
                if fvs:
                    out.write(str(fvs))
                    out.write('\n')

        print(str(time.time() - before) + " seconds spent for whole step..\n")
        out.close()
        count = 0
        for i in range(rng):
            if i == 0:
                continue
            cnt = len(self.feedback_vertex_set[i])
            print("There are  " + str(cnt) + "minimal FVSs with size " + str(i) + ".")
            count += cnt
        print("Total " + str(count) + " minimal FVSs are found.")
