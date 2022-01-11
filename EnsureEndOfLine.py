import os.path
from os import walk

# Change this directory to wherever the files you want to adjust are
target_directory = ""

filesConsidered = 0
filesAdjusted = 0

# Set the extensions to consider
fileExts = ["kt", "java"]

for (dirpath, dirnames, filenames) in walk(target_directory):
    for filename in filenames:
        try:
            absolute_filename = os.path.join(dirpath, filename)
            # Only consider certain file extensions
            if absolute_filename.split(".")[-1] not in fileExts:
                continue
            with open(absolute_filename, 'r+') as f:
                filesConsidered += 1
                # Access second to last byte
                f.seek(-1, 2)
                # Read the last byte
                last_byte = f.read(1)
                # Check if the last byte is an End of Line
                if last_byte != '\n':
                    # If it's not, add the line
                    filesAdjusted += 1
                    f.write('\n')
                    f.close()
        except IOError:
            # Couldn't read file (ex. empty files)
            continue

# Print results
print("Number of files scanned: " + str(filesConsidered))
print("Number of files adjusted: " + str(filesAdjusted))
