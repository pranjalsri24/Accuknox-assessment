#problem 1 of task 2 which is system health montinor
import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 200

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
memory_usage = memory_info.percent
disk_info = psutil.disk_usage('/')
disk_usage = disk_info.percent
running_processes = len(psutil.pids())

def check_thresholds(cpu, memory, disk, processes):
    alerts = []
    if cpu > CPU_THRESHOLD:
        alerts.append(f"CPU usage is too high: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"Memory usage is too high: {memory}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Disk usage is too high: {disk}%")
    if processes > PROCESS_THRESHOLD:
        alerts.append(f"Number of running processes is too high: {processes}")
    return alerts


def send_alerts(alerts):
    for alert in alerts:
        print(alert)
        with open('system_health.log', 'a') as log_file:
            log_file.write(alert + '\n')


alerts = check_thresholds(cpu_usage, memory_usage, disk_usage, running_processes)
if alerts:
    send_alerts(alerts)
else:
    print("All system metrics are within the defined thresholds.")
