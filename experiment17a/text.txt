def bankers_algoritha|):
n = int(input ("Enter the nuaber of processes
m = intlinout("Eater the rumber of resources: ")
allet
a
[l_
max_clain= []
total
E =
avail
a
wort
a,
need
finish = ['n']
#
count
0
print("Enter the allocation matrix:")
in range (n):
alloc.apperd(list/map(int, imput().split())))
print("Enter the claim matrix:")
in sange (n):
zak_claia.apperd(lise(map(inb, impue()."plie())))
print("Enter the zesource vector:")
total = list (map(int, input().split()))
avaii= [0]
fer i in Sange (n):
for j in range(m):
avail(]] += alloc(4](3]
work = (total[i] - avail[i] tor i in range (m)]
need = [[max_elais[4][31 - alloc[i](j] for j in range(m)] for i in range(n)]
while count < n:
safe = False
for i in range(n):
if finiah[i] = 'n':
if all(need[i][]] <= wort[]] for j in sange(a)):
print(f"All resources can be allocatnd to Precess [i + 11")
prins("Available resources after allocation:")
for k in range (m)
wort[s] += alloc[i] [t]
prins(f"[vork[k]:4]", end="")
print("in")
£inisk[i],
count + 1
safe
True
break
if not safe:
print("The system is not in
safe state
"
return
print("InThe syatem is in a safe state
if__ name __="main_":
bankers_ _algorith(]