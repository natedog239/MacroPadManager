import psutil
import win32api
import time

test = win32api.GetLogicalDrives()
print(test)

def get_drive_letter(device_name):
    # Get a list of all connected drives 
    drives = psutil.disk_partitions()

    # Iterate over the drives and find the one with the specified name
    for drive in drives:
        print(drive)
        letter = drive[1]
        print(letter)
        time.sleep(1)
        #info = win32api.GetVolumeInformation(letter)
        #print(info)
        time.sleep(1)

    # If the device is not found, return None
    return None

# Usage example
device_name = "CIRCUITPY"
drive_letter = get_drive_letter(device_name)

if drive_letter:
    print(f"The drive letter associated with {device_name} is {drive_letter}")
else:
    print(f"No drive named {device_name} found.")