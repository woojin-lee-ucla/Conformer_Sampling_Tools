import re

# Define the regular expression pattern to search for the values after "HF=", excluding "0.,"
hf_pattern = re.compile(r'(?<=HF=)(?!0\.,)[\-0-9\.]+')

# Loop over all the output files
for i in range(0, 58):
    filename = f'file_{i}.out'
    
    # Open the output file and read its contents
    with open(filename, 'r') as f:
        content = f.read()
        
    # Search for the values after "HF=", excluding "0.,", using the regular expression pattern
    matches = hf_pattern.findall(content)
    if matches:
        # Extract the values as floats and multiply by 627.509
        values = [float(match) * 627.509 for match in matches]
        print(f'HF values in {filename}: {", ".join(str(val) for val in values)}')
    else:
        print(f'Could not find any HF values in {filename}')