import fvsFinder as fv

#a = fv.FVSFinder("mapk_annotation.txt")
#b = fv.FVSFinder("toy_annotation.txt")
#c = fv.FVSFinder("Fumia_cytoscape.txt")

e = fv.FVSFinder("test1.csv")
f = fv.FVSFinder("test2.csv")

e = fv.FVSFinder("test1.csv", checker=True, fvs_found = ['FoxD-a/b'])

