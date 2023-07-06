import psutil

def get_drive_letter(device_name):
    # Get a list of all connected drives
    drives = psutil.disk_partitions()

    # Iterate over the drives and find the one with the specified name
    for drive in drives:
        if device_name in drive.device:
            return drive.mountpoint

    # If the device is not found, return None
    return None

# Usage example
device_name = "CIRCUITPY"
drive_letter = get_drive_letter(device_name)

if drive_letter:
    print(f"The drive letter associated with {device_name} is {drive_letter}")
else:
    print(f"No drive named {device_name} found.")