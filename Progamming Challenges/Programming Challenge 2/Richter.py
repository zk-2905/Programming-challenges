richt = float(input("Enter richter scale measurements: "))
energy = 10**((1.5*richt)+4.8)
tnt = energy/ 4.184*(10**9)
print("Equivalence in joules: ", energy)
print("Equivalence in tons of TNT: ", tnt)
              
