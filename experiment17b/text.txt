def job_scheduling()
job
time
C1
=
safe = [None] * 10
n = int(input ("Enter the number of jobs: "))
for i in range (n):
job_name = input (f"Enter job (it1) name: ")
job_time = int (input (f"Enter job (i+1) time: "))
job.append (job_name)
time.append(job_time)
avail = int (input ("Enter the available resources: "))
temp = time[:] t Copy of time array for sorting
tem = list(range(n)) $ Index tracking list for original jobs
for i in range (n)
for j in range (i t 1, n):
if temp[i] > temp[j]
temp[i], temp[j] = temp[j], temp[i]
tem[i], tem[j] = tem[j], tem[i]
ind =1 ₩ Index to track safe sequence
for i in range (n)
q= tem[i] t Get the index of the job in sorted order
if time[q] <= avail:
safe[ind] = tem[i] t Add the job to the safe sequence
avail -= time[q] t Reduce available resources
print (£"(job[safe[ind]]|", end=' ') $ Print the job name
ind += 1
else:
print ("No safe sequence")
break
if ind > 1:
print ("InSafe sequence is:")
for i in range(1, ind):
print (f"(job[safe[i]]) (time[safe[i]]]", end=', ')
print ("Ib\b ") t Remove last comma and space
name_==
main
job_scheduling ()