import fvsFinder as fv

a = fv.FVSFinder("mapk_annotation.txt")
b = fv.FVSFinder("toy_annotation.txt")
c = fv.FVSFinder("Fumia_cytoscape.txt")
d = fv.FVSFinder("fumia_original.txt")

fvs = (
    ["E2F", "CycA", "UbcH10", "p27", "Snail", "p53", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "p27", "Snail", "p53", "BAX"],
    ["E2F", "CycA", "UbcH10", "p27", "Snail", "Mdm2", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "CycD", "Snail", "p53", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "CycD", "Snail", "p53", "BAX"],
    ["E2F", "CycA", "UbcH10", "CycD", "Snail", "Mdm2", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "p27", "NFkB", "Mdm2", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "p27", "NFkB", "p53", "BAX"],
    ["E2F", "CycA", "UbcH10", "p27", "NFkB", "p53", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "CycD", "NFkB", "p53", "Bcl2"],
    ["E2F", "CycA", "UbcH10", "CycD", "NFkB", "p53", "BAX"],
    ["E2F", "CycA", "UbcH10", "CycD", "NFkB", "Mdm2", "Bcl2"]
)

for f in fvs:
    print(f)
    fv.FVSFinder("Fumia_cytoscape.txt", checker=True, fvs_found=f)
    print("\n\n\n")

