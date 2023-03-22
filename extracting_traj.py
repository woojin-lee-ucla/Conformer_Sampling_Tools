import os

# Set the directory containing the folders of interest
directory = "Your current folder" # need to add your directory path

# Create the "analysis" directory if it doesn't already exist
analysis_dir = os.path.join(directory, "analysis")
if not os.path.exists(analysis_dir):
    os.mkdir(analysis_dir)

# Loop through folders n1, n2, ..., n10
for i in range(1, 11):
    folder_name = f"n{i}"
    folder_path = os.path.join(directory, folder_name)

    # Check if the folder exists before trying to access files inside
    if os.path.exists(folder_path):
        # Rename the traj file inside the folder
        traj_filename = "traj"
        traj_filepath = os.path.join(folder_path, traj_filename)

        if os.path.exists(traj_filepath):
            # Create the analysis subdirectory for this folder if it doesn't already exist
            analysis_subdir = os.path.join(analysis_dir, folder_name)
            if not os.path.exists(analysis_subdir):
                os.mkdir(analysis_subdir)

            # Move the traj file to the analysis subdirectory and rename it to traj.xyz
            new_filename = "traj.xyz"
            new_filepath = os.path.join(analysis_subdir, new_filename)
            os.rename(traj_filepath, new_filepath)
            print(f"Moved {traj_filename} to {analysis_subdir} as {new_filename}")
        else:
            print(f"No traj file found in {folder_name}")
    else:
        print(f"{folder_name} folder not found in {directory}")
