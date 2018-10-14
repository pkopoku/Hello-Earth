#A basic greedy alg

#todo: establish generalized problem
A={1,2,3,4,5}
T=8
time_used=0
num_of_things_done=[]

for i in A:
    if time_used >= T:
        break
    else:
        num_of_things_done.append(i)
        time_used+=i

print(num_of_things_done)
print(time_used)
print("Completed")
