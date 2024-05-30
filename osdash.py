import os
import time
import psutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_dashboard():
    clear_screen()
    print("Memory Management Dashboard\n")
    print("1. Display Memory Information")
    print("2. Monitor Memory Usage of a Specific Application")
    print("3. Exit")
    choice = input("\nEnter your choice: ")
    return choice

def display_memory_info():
    memory_info = psutil.virtual_memory()
    print("\nMemory Information:")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Memory Usage Percentage: {memory_info.percent}%")
    input("\nPress Enter to continue...")

def monitor_memory_usage(application_name):
    try:
        while True:
            clear_screen()
            print(f"Monitoring Memory Usage of '{application_name}' (Press Ctrl+C to stop)...\n")
            processes = [proc for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']) if application_name in proc.info['name']]
            if processes:
                total_memory = sum(proc.info['memory_info'].rss for proc in processes)
                print(f"'{application_name}' Memory Usage: {total_memory} bytes")
            else:
                print(f"No process found with name '{application_name}'")
            time.sleep(2)  # Update every 2 seconds
    except KeyboardInterrupt:
        pass

def main():
    while True:
        choice = display_dashboard()

        if choice == "1":
            display_memory_info()
        elif choice == "2":
            all_process_names = [proc.info['name'] for proc in psutil.process_iter(attrs=['name'])]
            print("All running process names:", all_process_names)

            application_name = input("\nEnter the name of the application to monitor: ")
            monitor_memory_usage(application_name)
        elif choice == "3":
            print("Exiting the Memory Management Dashboard...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
