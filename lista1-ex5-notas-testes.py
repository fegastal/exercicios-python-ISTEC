print("Introduza o lado 1")
l1 = float(input())
print("Introduza o lado 2")
l2 = float(input())
print("Introduza o lado 3")
l3 = float(input())

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if(l1 == l2 == l3):
        print("Equilátero")
    else:
if((l1==l2) or (l2==l3) or (l1==l3)):
print("Isósceles")
else:
print("Escaleno")
input()