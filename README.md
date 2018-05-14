FVS FINDER Documentation
========================

# AUTHOR
>Byunghyun Ban
* CTO of Imagination Garden Inc. (2018~)
* CFO of Cheesecake Studio Inc. (2016)
* CEO & CTO of Studio Mic Inc. (2015)
* CTO of New Page Inc. (2011~2013)
* Master's Degree @ Bio and Brain Engineering Department, KAIST (Korea Advanced Institute of Science and Technology)
* Systems Biology and Inspired Engineering(SBIE) Lab.
* bhban@kaist.ac.kr
* bahn1307@gmail.com

## 1. Environments
* Python3
* Don't support any problems from python2 environment

## 2. Dependencies
### 1. numpy
* numpy library required.
* Type "sudo pip3 install numpy" on bash.

### 2. tarjan
* tarjan library required.
* Type "sudo pip3 install tarjan" on bash.

*If you are using windows, please visit numpy and tarjan webpage to install Dependencies.*

## 3 . How to use
Please import FVSFinder on python3 environment.
> Example
>>  import FVSFinder as fv

### 1. To Find Minimal FVSs
Create an FVSFinder class with input conditions. the initiator automatically starts the job.
Input file must be cleared but output file is not. Default output file name is "Minimal_FVS.txt"
>  a = fv.FVSFinder("network_file.txt", "output_file.txt")

network file should be placed in 'network/'. It could be any file if python I/O module supports line-by-line reading. (.txt, .csv, ...)

The result will be saved in 'results/'

### 2. To test if a set is FVS.
Test if the given list fvs_found can remove all cycles in the network

> b = fv.FVSFinder("test1.csv", mode="checker", fvs_found = list_of_nodes)

### 3. Max Coverage Investigation
Test maximum cycle coverage of all nodes. For each node, program examines how much SCCs are remaining by removing it. If the resulting number is great, the node influences many cycles.

> c = fv.FVSFinder("test1.csv", mode="maxcover")

### 4. File format
Default file format is <source, target> form. To use adjacency matrix input, activate additional parameters when calling the class.

> d = fv.FVSFinder(network_file, matrix=True, xheader=True, yheader=True)

If the matrix has x-direction or y-direction header(names of nodes for ex.), please set xheader and yheader value to True. (default value is set False)

### 5. Threshold
For example, neural network has weight rather than boolean value for linkage notation. you may set threshold. If the value in adjacency matrix is lower than threshold, the program consider it as disconnection.

> e = fv.FVSFinder("c_elegans.csv", matrix=True, xheader=True, yheader=True, threshold=0)
