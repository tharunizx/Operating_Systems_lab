no_job=int(input("Enter number of jobs: "))
ex_time=[]
for i in range(no_job):
    ext=int(input(f"Enter the time required for Job{i+1}:"))
    ex_time.append(ext)
ex_time.sort()
t=0
wt=[]
for i in range(no_job):
    wt.append(t)
    t+=ex_time[i]
print("Job number\tExecution time\tWaiting time\tTurnaround time")
for i in range(no_job):
    print(f"J{i+1}\t\t{ex_time[i]}\t\t{wt[i]}\t\t{wt[i]+ex_time[i]}")
awt=sum(wt)/len(wt)
att=(sum(wt)+wt[i]+ex_time[i])/len(wt)
print("Average waiting time= ",awt)
print("Average turnaround time= ",att)
    
