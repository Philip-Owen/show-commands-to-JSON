import re
import json


def int_status_to_JSON(file_path):
    lines = []
    int_status = []

    # Open file and create a list
    file = open(file_path)
    output = file.readlines()

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


# Write json file from int_status_to_JSON results
with open('output.json', 'w') as f:
    json.dump(int_status_to_JSON('interface_status.txt'),
              f, indent=4, sort_keys=False)
    print('Write of text file to JSON complete...')
