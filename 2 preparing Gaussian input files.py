pip install ase

for i in {0..100}; do ase-gui file_"$i".xyz -o file_"$i".gjf; done

# now you install ase, .xyz can be automatically reformed into .gjf. This is Shell script.
