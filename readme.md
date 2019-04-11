# Show Commands to JSON

These scripts were designed to take the Cisco command `show interface status` ouput and convert it into a JSON format.

`status_to_JSON_textfile` reads the output from a .txt file within the folder and converts it to JSON.

`status_to_JSON_textfile` utilizes Netmiko to SSH to a device, run the show command, and then convert the results to JSON.