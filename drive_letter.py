import os
import win32api
import time

# Test code for win32api
test = win32api.GetLogicalDrives
print(test)

def find_drive_with_name(target_name):
    available_drives = [f"{drive}:\\" for drive in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{drive}:\\" or drive == ':')]
    print(available_drives)
    for drive in available_drives:
        drive_name = drive.split("\\")[-2]
        print(drive_name)
        if target_name.lower() in drive_name.lower():
            return drive

    return None

# Example usage
target_name = "CIRCUITPY"
found_drive = find_drive_with_name(target_name)

if found_drive:
    print(f"The drive with name '{target_name}' is found on drive letter: {found_drive}")
else:
    print(f"No drive with name '{target_name}' found.")