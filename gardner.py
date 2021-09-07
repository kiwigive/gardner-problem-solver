from itertools import product
from math import floor, ceil
from tabulate import tabulate

m = input("m: ")
n = input("n: ")
k = input("k: ")
mn = float(m * n)
case = [ele for ele in product(range(0, m), repeat = k)]
rs = []
rf = []
for i in case:
    pstart = 1.0
    pend = mn
    for j in range(1, k + 1):
        l = i[j - 1]
        pstart = ceil(pstart / m) + (l * n)
        pend = ceil(pend / m) + (l * n)
        ##print(i, l, j, int(pstart), int(pend))
    if (pstart == pend):
        rs.append((int(pstart), int(pend), i))
    else:
        rf.append((int(pstart), int(pend), i))
rs.sort()
rf.sort()
print("======= success =======")
print(rs)
print("======== fail ========")
print(rf)
print("======================")

datatable = [{'Position','Code'}]
isfindall = True
j = 1
for i in range(1, int(mn) + 1):
    isfind = False
    listcode = [i]
    for j in range(j, len(rs) + 1):
        result_success = rs[j-1]
        position = result_success[0]
        if (i != position):
            break
        isfind = True
        code = result_success[2]
        code = code[::-1]
        code = str(code).replace(', ','').replace('(','').replace(')','')
        listcode.append(code)
    if (isfind == False):
        isfindall = False
    datatable.append(listcode)
if (isfindall == False):
    print("Unsolvable")
    print(tabulate(datatable))
else:
    print("Solvable")
    print(tabulate(datatable))
