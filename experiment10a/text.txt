def main():

buffer = [None] 10 # Buffer of size 10

bufsize = 10 # Buffer size

in_pos = 0 #'in' index for producer out_pos = 0 # 'out' index for consumer

choice = 0 # User choice # Produced value

produce = 0 consume = 0 # Consumed value

while choice != 3:

print("\n1. Produce \t 2. Consume \t3. Exit")

choice int (input("Enter your choice: "))

if choice == 1: # Produce

if (in_pos + 1) & bufsize == out pos: #Check if buffer is full

print("\nBuffer is Full")

else:

produce = int(input("Enter the value: "))

buffer [in_pos] = produce

in_pos (in_pos + 1) & bufsize # Circular increment of 'in' index =

elif choice == 2: # Consume

if in_pos == out_pos: # Check if buffer is empty

print("\nBuffer is Empty")

else:

consume = buffer [out_pos]

print (f"\nThe consumed value is (consume)")

out_pos (out pos + 1) % bufsize # Circular increment of 'out' index =

elif choice == 3: # Exit

print("Exiting...")

else: print("Invalid choice, please select again.")

if name == main":

main()