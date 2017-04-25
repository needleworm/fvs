import fvsFinder as fv

#a = fv.FVSFinder("mapk_annotation.txt")
#b = fv.FVSFinder("toy_annotation.txt")
#c = fv.FVSFinder("Fumia_cytoscape.txt")

#e = fv.FVSFinder("test1.csv")
#f = fv.FVSFinder("test1.csv")
#g = fv.FVSFinder("test1.csv", mode="maxcover")

#e = fv.FVSFinder("test1.csv", mode="checker", fvs_found = ['FoxD-a/b'])

f = fv.FVSFinder("drosophila.csv", matrix=True, xheader=True, yheader=True, precomb=True)
