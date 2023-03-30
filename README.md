# Conformer_Sampling_Tools
The manual analysis takes a long time by checking each result from numerous conformers. The codes automate the process of quantitative analysis of conformers. 

# The steps of this code is shown below:
# 1 xyz files extracting.py - conformers.xyz -> conformer1.xyz, conformer2.xyz, conformer3.xyz, ... , conformer100.xyz 
# 2 preparing Gaussian input files.py - conformer1.xyz, conformer2.xyz, conformer3.xyz, ... , conformer100.xyz -> conformer1.gjf, conformer2.gjf, conformer3.gjf, ... , conformer100.gjf
# 3 adding-gaussian-input.py - Adding Gaussian input (proccessor #, memory #, functional and basis set, title, charge and spin state
# 4 transfer .gjf.py  - transfer .gjf files to a single folder
#  (you submit the jobs in cluster, and get .out files after the calculations)
# 5 extracting energy from output files then multiply by 627.509.py - automatically extract energies of single point calculations, and multiply by 627.509
