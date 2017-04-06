import fvsFinder as fv

#a = fv.FVSFinder("mapk_annotation.txt")
#b = fv.FVSFinder("toy_annotation.txt")
#c = fv.FVSFinder("Fumia_cytoscape.txt")

#e = fv.FVSFinder("test1.csv")
f = fv.FVSFinder("test2.csv")

#e = fv.FVSFinder("test1.csv", checker=True, fvs_found = ['FoxD-a/b'])
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
