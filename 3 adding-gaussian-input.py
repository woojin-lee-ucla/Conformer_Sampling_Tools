import os

# Loop over all files with names file_0.gjf, file_1.gjf, ..., file_27.gjf
for i in range(100):
    file_name = f'file_{i}.gjf'
    
    # Read in the contents of the file
    with open(file_name, 'r') as f:
        file_contents = f.readlines()
    
    # Replace the first 5 lines with the desired text
    file_contents[0:5] = ['%nprocshared=4\n', '%mem=8GB\n', '#p wb97xd/6-311++g(d,p) scrf=(smd,solvent=water) temperature=273.15\n', '\n', 'Title Card Required\n\n0 1\n']
    # Below will be written in each .gjf file
    # %nprocshared=4
    # %mem=8GB
    # #p wb97xd/6-311++g(d,p) scrf=(smd,solvent=water) temperature=273.15
    
    # Title Card Required
    
    # 0 1
   
    # Write the modified contents back to the file
    with open(file_name, 'w') as f:
        f.writelines(file_contents)
    
    # Print a message indicating the file has been modified
    print(f'Modified {file_name}')
