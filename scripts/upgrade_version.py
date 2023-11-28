import io
# Filename containing the version information
filename = 'PolyDeDupe/version.py'

# Read the current version information
with io.open(filename, 'w', encoding='utf-8') as file:
    lines = file.readlines()


for i, line in enumerate(lines):
    if '_MINOR' in line:
        parts = line.split('=')
        minor_version = int(parts[1].strip().strip('"')) + 1
        lines[i] = '_MINOR = "{}"\n'.format(minor_version)
        break

# Write the updated version information back to the file
with io.open(filename, 'w', encoding='utf-8') as file:
    file.writelines(lines)
