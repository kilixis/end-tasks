import psutil

# List of process names to terminate
processes_to_terminate = ['Notepad.exe', 'chrome.exe', 'Skype.exe','msteams.exe']

# Path to the folder containing the processes to terminate
folder_path = r'C:\Program Files (x86)\Microsoft\Edge\Application'

def terminate_processes(process_names, folder_path):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            # Terminate by name
            if proc.info['name'] in process_names:
                proc.terminate()  # or proc.kill()
                print(f"Terminated {proc.info['name']} with PID {proc.info['pid']}")

            # Terminate by folder path
            elif proc.info['exe'] and proc.info['exe'].startswith(folder_path):
                proc.terminate()  # or proc.kill()
                print(f"Terminated {proc.info['name']} with PID {proc.info['pid']} from {proc.info['exe']}")

        except psutil.NoSuchProcess:
            print(f"No Such Process for PID {proc.info['pid']}")
        except psutil.AccessDenied:
            print(f"Access Denied for {proc.info['name']} with PID {proc.info['pid']}")
        except Exception as e:
            print(f"Undetermined error: {str(e)}")

terminate_processes(processes_to_terminate,folder_path)
