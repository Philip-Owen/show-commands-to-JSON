from netmiko import Netmiko
import getpass
import re
import json


def get_status():

    # Create device dictionary
    device = {
        "host": input("IP address of device: "),
        "username": input("Username: "),
        "password": getpass.getpass("Password: "),
        "device_type": "cisco_ios",
    }

    # Establish SSH connection to device, run command, and disconnect from session
    conn = Netmiko(**device)
    show_status = 'show interface status'
    output = conn.send_command(show_status)
    output = output.split('\n')
    conn.disconnect()

    # Write results to .json file
    with open(f'{device["host"]}.json', 'w') as f:
        json.dump(int_status_to_JSON(output), f, indent=4, sort_keys=False)
        print('Write of text file to JSON complete...')


def int_status_to_JSON(output):
    lines = []
    int_status = []

    # Searches output for lines matching regex
    # Regex is looking for a pattern of two letters followed by a single digit and a forward slash
    # Will match Gi1/0/3, Fa0/1, etc.
    for l in output:
        p = re.compile(r'[a-zA-z]{2}\d\/')
        if p.match(l):
            lines.append(l)

    # Loops array of matched interfaces, splits each line, and builds a dictonary object for each interface
    for l in lines:
        l = [l[:10], l[10:29], l[29:41], l[42:53], l[53:60], l[60:67], l[67:]]
        status = {
            'int': l[0].rstrip().lstrip(),
            'desc': l[1].rstrip().lstrip(),
            'status': l[2].rstrip().lstrip(),
            'vlan': l[3].rstrip().lstrip(),
            'duplex': l[4].rstrip().lstrip(),
            'speed': l[5].rstrip().lstrip(),
            'type': l[6].rstrip().lstrip()
        }
        int_status.append(status)

    return int_status


if __name__ == "__main__":
    get_status()
