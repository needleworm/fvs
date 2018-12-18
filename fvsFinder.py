"""
Author : Byunghyun Ban
sbie.kaist.ac.kr
needleworm@Kaist.ac.kr

Korea Advanced Institute of Science and Technology
"""
import numpy as np
import network as nt
import time
import tarjan as tj
import itertools
import pickle
import math


class FVSFinder:
    n = 0
    current_size = 0
    network = None
    nodes = []
    single_comb = []
    self_feedback = []
    temp = []
    precomb = False
    outputfile = ""

    def __init__(self, network_file, output_file="Minimal_FVSs.txt", find_minimal_only=True, mode="minimal", fvs_found=[],
            matrix=False, xheader = False, yheader = False, threshold=3, trim=True, reverse=False, precomb=False):

        # mode: minimal, checker, maxcover
        self.network = nt.Network(network_file, matrix=matrix, xheader=xheader, yheader=yheader, threshold=threshold, trim=trim, reverse=reverse)
        self.n = self.network.n
        self.self_feedback = []
        self.nodes = self.network.nodes
        self.temp = list(np.zeros(self.n, dtype="int"))
        self.precomb = precomb
        self.outputfile = output_file
        if mode == "checker":
            self.checker(fvs_found)
        elif mode == "minimal" and find_minimal_only:
            print("\nFinding Minimal Feedback Vertex Sets\n")
            self.find_minimal_fvs()
        elif mode == "maxcover":
            print("\nFinding Coverage\n")
            self.maxcover()
        """
        else:
            print("\nFinding All Feedback Vertex Sets\n")
            self.find_all_fvs()
        """
        print("**********************************************")
        print("**************** PROCESS DONE ****************")
        print("**********************************************\n\n\n")

    @staticmethod
    def _tarjan_check(graph):
        scc = tj.tarjan(graph)
        for sc in scc:
            if len(sc) > 1:
                return True
        return False

    def maxcover(self):
        numfeedbacks = []
        graph = self._graph_generator(self.network.matrix)
        scc = tj.tarjan(graph)
        original_numfeedbacks = self._numfeedbacks(scc)
        for i in range(self.n):
            mod_matrix = np.delete(self.network.matrix, i, 0)
            mod_matrix = np.delete(mod_matrix, i, 1)
            graph = self._graph_generator(mod_matrix, n= self.n-1)
            scc = tj.tarjan(graph)
            numfeedbacks.append((i, self._numfeedbacks(scc)))

        if not self.outputfile:
            self.outputfile = "maxcoverage.txt"

        out = open("result/"+self.outputfile, "w")
        out.write("Original Network has " + str(original_numfeedbacks) + " feedbacks.")
        for node, num in numfeedbacks:
            line = "Removal of Node " + self.nodes[node] + " reduces number of SCCs into " + str(num) + ".\n"
            print(line)
            out.write(line)
        out.close()


    @staticmethod
    def _numfeedbacks(sccs):
        scc = 0
        for element in sccs:
            if len(element) > 1:
                scc += 1
        return scc

    def checker(self, fvs_found):
        before = time.time()
        for node in fvs_found:
            self.network.remove_node_from_network(self.network.nodes.index(node))
        self.network.trim_none_feedback_nodes()
        self.nodes = self.network.nodes
        self.n = self.network.n
        if self._tarjan_check(self._graph_generator(self.network.matrix, self.n)):
            print("The Set is Not FVS")
        else:
            print("This Set is an FVS")
        print(str(time.time() - before) + " seconds spent for determination proces.")

    def find_minimal_fvs(self):
        out = open("result/" + self.outputfile, 'w')
        before = time.time()
        fvs, size = self._find_minimal_fvs()
        size += len(self.self_feedback)
        print("All process Done!")
        print("Total " + str(time.time() - before) + " seconds spent for overall process.\n")
        if not size:
            print("No FVS exists")
            return
        print("Size of minimal FVS is " + str(size) + '.')
        print("Total " + str(len(fvs)) + " minimal FVS exists.\n")
        if not fvs:
            out.write(str(self.self_feedback))
        else:
            for i, fv in enumerate(fvs):
                out.write(str(self.self_feedback + fv))
                if i != len(fvs) - 1:
                    out.write('\n')
        out.close()

    def _find_self_feedback(self):
        idx = []
        for i in range(self.n):
            if self.network.matrix[i][i]:
                self.self_feedback.append(self.nodes[i])
            else:
                idx.append(i)
        for sf in self.self_feedback:
            self.network.remove_node_from_network(self.network.nodes.index(sf))
        self.network.trim_none_feedback_nodes()
        self.n = self.network.n
        self.nodes = self.network.nodes
        return idx

    def _find_minimal_fvs(self):
        self._find_self_feedback()
        fvs = []
        before = time.time()

        if self.self_feedback:
            print("There are " + str(len(self.self_feedback)) + " self-feedback nodes on the network.\n\n")
        print("**********************************************")
        print("*********** Starting  Main Process ***********")
        print("**********************************************\n")
        for i in range(1, self.n):
            before_time = time.time()
            print("Checking if size " + str(i + len(self.self_feedback)) + " FVS exists.")
            fvs = self._find_feedback_vertex_sets(i)
            if fvs:
                print(str(time.time() - before) + " seconds spent for Finding Minimal FVS.\n")
                return fvs, i + len(self.self_feedback)
            print("Size " + str(i + len(self.self_feedback)) + " FVS Doesn't Exist.")
            print(str(time.time() - before_time) + " seconds spent for this step.\n")
        return fvs, 0

    def _graph_generator(self, matrix, n=0):
        graph = {}
        if not n:
            n = self.n
        for i in range(n):
            target = []
            for j in range(n):
                if matrix[i, j]:
                    target.append(j)
            graph[i] = target
        return graph

    def _is_there_cycle(self, matrix):
        for i in range(self.n):
            if matrix[i][i]:
                return True
        graph = self._graph_generator(matrix, self.n)
        for i in range(self.n):
            if graph[i]:
                if self._dfs_cycle(graph, i):
                    return True
        return False

    def _dfs_cycle(self, graph, root):
        stack = []
        visited = []
        stack.append(root)

        while stack:
            top = stack.pop()
            visited.append(top)
            if set(visited) & set(graph[top]):
                return self._tarjan_check(graph)
            targets = list(set(graph[top]) - set(visited))
            targets.sort()
            stack.extend(targets)

        return False

    def _find_feedback_vertex_sets(self, i):
        FVS = []
        if self.precomb:
            comb = pickle.load("combinations49_" + str(i) + ".pkl")
            for el in comb:
                matrix = self.network.remove_nodes(el)
                if not self._is_there_cycle(matrix):
                    fvs = []
                    for idx in el:
                        fvs.append(self.nodes[idx])
                    FVS.append(fvs)
            return(FVS)

        for comb in itertools.combinations(range(self.n), i):
            print(comb)
            matrix = self.network.remove_nodes(comb)
            if not self._is_there_cycle(matrix):
                fvs = []
                for idx in comb:
                    fvs.append(self.nodes[idx])
                FVS.append(fvs)
        return FVS

    def find_all_fvs(self):
        print("********************\n")
        print("Currently Updating This Method. Please use Old Version If you want to find All FVS.")
        print("********************\n")

    def how_to_cite():
        print("**********************************************")
        print("Please Mention Github Repository\n   https://github.com/needleworm/fvs\n")
        print("and its author, Byunghyun Ban (KAIST, South Korea.)")
        print("**********************************************")
