MAX = 25

def main():
frag = [0] * MAX

b = [0] * MAX

f = [0] * MAX

bf = [0] * MAX # Block flag to mark if the block is allocated ff = [0] * MAX # File flag to store block number for each file

nbint (input("Enter the number of blocks: "))

nf int(input("Enter the number of files: "))

print("\nEnter the size of the blocks:")

for i in range (nb):

b[i] = int(input (f"Block (i + 1): "))

print("Enter the size of the files:")

for i in range (nf):

f[i] = int(input(f"File (i + 1): "))

for i in range (nf):

lowest = float('inf')

for j in range (nb):

if bf[j] == 0: temp = b[j] #Check if block is not allocated - f[i] if temp >= 0 and temp < lowest: lowest = temp frag [i] = lowest # Store the fragmentation

ff[i] = j # Assign block number

if lowest != float('inf'):

bf[ff[i]] = 1 # Mark block as allocated

print("\nFile No\tFile Size\tBlock No\tBlock Size\tFragment")

for i in range (nf):

if ff[i] != 0 or frag[i] != 0:

print (f" (i + 1)\t\t(f[i]}\t\t[ff[i] + 1}\t\t[b[ff[i]]}\t\t{frag[i])") else:

if name == "main":

print (f"[i + 1}\t\t{f[i]}\t\tNot Allocated\t\t-\t\t-")|

main()