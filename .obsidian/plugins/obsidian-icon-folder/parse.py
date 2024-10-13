# Open the file for reading, process it, and then write the filtered lines back to the file
with open('data.json', 'r') as f:
    lines = f.readlines()

# Filter out lines that contain "TiFile"
filtered_lines = [line for line in lines if "TiFile" not in line]

# Write the filtered lines back to the file (overwriting the original content)
with open('data.json', 'w') as f:
    f.writelines(filtered_lines)
