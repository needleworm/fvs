import fvsFinder as fv

#To Find mFVS
test = fv.FVSFinder("test2.csv")

#To check if a set is mFVS
#Example

"""aa = [['SOS', 'ErbB11', 'CaM', 'PL4/5-p2'],
['SOS', 'ErbB11', 'CaMKII', 'PL4/5-p2'],
['SOS', 'ErbB11', 'cytCa2+', 'DAG'],
['SOS', 'ErbB11', 'cytCa2+', 'PKC'],
['SOS', 'ErbB11', 'cytCa2+', 'phosphatidylacid'],
['SOS', 'ErbB11', 'cytCa2+', 'PI5K'],
['SOS', 'ErbB11', 'cytCa2+', 'PL4/5-p2'],
['SOS', 'ErbB11', 'cytCa2+', 'PI4-P'],
['SOS', 'ErbB11', 'cytCa2+', 'PLD'],
['ErbB11', 'CaM', 'ERK1/2', 'PL4/5-p2'],
['ErbB11', 'CaMKII', 'ERK1/2', 'PL4/5-p2'],
['ErbB11', 'cytCa2+', 'ERK1/2', 'PL4/5-p2']]

for i in aa:
	g = fv.FVSFinder("test2.csv", checker=True, fvs_found=i)
"""
