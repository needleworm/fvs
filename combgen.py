import pickle
import itertools

comb = []
comb2 = []

def combisave(i):
    comb = (list(itertools.combinations(range(49), i)))
    f = open("combinations49_" + str(i) + ".pkl", 'wb')
    pickle.dump(comb, f)
    f.close()
    print(i)

def combisave2(i):
    comb = list(itertools.combinations(range(50), i))
    f = open("combinations50_" + str(i) + ".pkl", 'wb')
    pickle.dump(comb, f)
    f.close() 
    print(i)


for i in range(49):
    combisave(i)
    combisave2(i)

combisave2(50)

