import findfvs as fv

#a = fv.FVSFinder("mapk_nodes.txt", "mapk_annotation.txt")
#b = fv.FVSFinder("nodes.txt", "annotation.txt")
#c = fv.FVSFinder("fumia_simplified_nodes.txt", "Fumia_cytoscape.txt")

fvs = (
    ["E2F", "CycA", "UbcH10", "CycD", "NFkB", "p53", "Bcl2"],
    ['E2F', 'CycA', 'UbcH10', 'CycD', 'NFkB', 'p53', 'Bcl2', 'GSK3']
)

d = fv.FVSFinder("fumia_simplified_nodes.txt", "Fumia_cytoscape.txt", checker=True, fvs_found=fvs[0])