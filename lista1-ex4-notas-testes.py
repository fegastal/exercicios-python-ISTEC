print("Introduza a nota do t1")
t1 = float(input())
print("Introduza a nota do t2")
t2 = float(input())
print("Introduza a nota do t3")
t3 = float(input())
print("Introduza a nota do t4")
t4 = float(input())
med = (t1+t2+t3+t4)/4
if (med >= 10):
    print(f"Passou com {med}")
else:
    print(f("Reprovou com {med}"))
input()