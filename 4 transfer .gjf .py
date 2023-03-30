# This code transfers all .gjf files to a newly created 'conformers' folder.
import os
import shutil

# create new directory for .gjf files
if not os.path.exists('conformers'):
    os.makedirs('conformers')

# move all .gjf files to the new directory
for file in os.listdir('.'):
    if file.endswith('.gjf'):
        shutil.move(file, 'conformers/' + file)
