import wmi

def get_drive_letter(device_name):
    # Connect to the WMI service
    c = wmi.WMI()

    # Query for all USB devices
    usb_devices = c.Win32_USBHub()
    #print(usb_devices)

    # Iterate over the devices and find the one with the specified name
    for device in usb_devices:
        print('Device: ',device)
        if device_name in device.Name:
            print('Device_name: ',device_name)
            # Get the associated disk drive
            associated_drive = device.Associators()[0]

            # Extract the drive letter
            drive_letter = associated_drive.Caption

            return drive_letter

    # If the device is not found, return None
    return None

# Usage example
device_name = "Samsung"
drive_letter = get_drive_letter(device_name)
print('The conencted drive letter is: ', drive_letter)