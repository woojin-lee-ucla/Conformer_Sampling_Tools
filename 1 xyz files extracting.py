import os

# open the merged file
with open('crest_conformers.xyz', 'r') as f:
    data = f.readlines()

# loop through the data and extract coordinates for each file
for i in range(100):
    file_name = f'file_{i}.xyz'
    file_data = data[i*50:(i+1)*50] # lines for each .xyz format for example between 1.xyz and 2.xyz
    
    # write the data to a new file
    with open(file_name, 'w') as f:
        f.writelines(file_data)
    
    # print a message indicating the file has been saved
    print(f'Saved {file_name}')




# 1 xyz files extracting.py # You can extract each .xyz coordinate from merged .xyz file (crest_conformers.xyz)
# 2 preparing Gaussian input files.py # you need to install ase through 'pip install ase' then, enter below in your terminal 
# for i in {0..27}; do ase-gui file_"$i".xyz -o file_"$i".gjf; done
# 3 add input files automatically in each .gjf
