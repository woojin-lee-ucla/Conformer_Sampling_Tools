#This is an automation script, which transfers 'pymol-distance-excecute' to each 'n#' folder.

import os
import shutil

source_file = "Your current directory" # need to add your current directory
target_dir = "Your target directory" # need to add your target directory

# Loop through each directory in the target directory
for i in range(1, 11):
    # Construct the path to the destination directory
    dest_dir = os.path.join(target_dir, f"n{i}")
    # Copy the source file to the destination directory
    shutil.copy2(source_file, dest_dir)
