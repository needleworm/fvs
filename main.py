import findfvs as fv

a = fv.FVSFinder("mapk_nodes.txt", "mapk_annotation.txt")
a.find_all_fvs()
