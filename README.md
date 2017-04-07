FVS FINDER Documentation
========================

# AUTHOR
>Byunghyun Ban
* CTO of New Page Inc. (2011~2013)
* CEO & CTO of Studio Mic Inc. (2015)
* CFO of Cheesecake Studio Inc. (2016)
* Graduate Student(Master's Program) @ Bio and Brain Engineering Department, KAIST (Korea Advanced Institute of Science and Technology)
* Systems Biology and Inspired Engineering(SBIE) Lab.
* http://sibe.kaist.ac.kr
* needleworm@kaist.ac.kr

## 1. Environments
* Python

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

>>  fv.FVSFinder("network_file.txt")

network file should be placed in 'network/'

The result will be saved in 'results/'
