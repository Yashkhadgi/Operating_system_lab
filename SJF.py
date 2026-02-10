def sjf_non_preemptive(processes):
    """
    processes: list of tuples (pid, burst_time)
    """

    # Sort by burst time
    processes.sort(key=lambda x: x[1])

    waiting_time = {}
    turnaround_time = {}

    current_time = 0

    for pid, burst in processes:
        waiting_time[pid] = current_time
        turnaround_time[pid] = current_time + burst
        current_time += burst

    print("PID | Burst | Waiting | Turnaround")
    print("-----------------------------------")

    total_wt = total_tat = 0

    for pid, burst in processes:
        wt = waiting_time[pid]
        tat = turnaround_time[pid]
        total_wt += wt
        total_tat += tat
        print(f"{pid:3} | {burst:5} | {wt:7} | {tat:10}")

    n = len(processes)
    print("\nAverage Waiting Time =", total_wt / n)
    print("Average Turnaround Time =", total_tat / n)


# Example usage
process_list = [
    (1, 6),
    (2, 8),
    (3, 7),
    (4, 3)
]

sjf_non_preemptive(process_list)

