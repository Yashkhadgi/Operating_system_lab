def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_time = burst_time.copy()
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [-1] * n   # to calculate first response
    completion_time = [0] * n
    
    time = 0
    
    while True:
        done = True
        
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                
                # First time execution → set Response Time
                if response_time[i] == -1:
                    response_time[i] = time
                
                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    time += remaining_time[i]
                    completion_time[i] = time
                    remaining_time[i] = 0
        
        if done:
            break
    
    # Calculations
    for i in range(n):
        turnaround_time[i] = completion_time[i]   # since arrival = 0
        waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    # Output
    print("Process\tBT\tTAT\tWT\tRT")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}\t{response_time[i]}")
    
    print("\nAverage TAT:", sum(turnaround_time)/n)
    print("Average WT:", sum(waiting_time)/n)
    print("Average RT:", sum(response_time)/n)


# ---- Input ----
processes = ["P1","P2","P3","P4","P5","P6"]
burst_time = [0,1,2,3,4,6]
time_quantum = 2

round_robin(processes, burst_time, time_quantum)
