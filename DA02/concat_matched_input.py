import os
import sys

run = str(sys.argv[1]) #'south'
nber_files = int(sys.argv[2]) # 30

# to concatenate matched inputs 00 to 29 for south
from astropy.table import Table, vstack
merged_dir = os.path.join(os.getenv('CSCRATCH'),'legacysim','dr9','DA02',run,'file0_rs0_skip0','merged')
print(f"reading from {merged_dir}")
file_idx = ["%.2d"%i for i in range(nber_files)]
print(f"File indexes: {file_idx}")
#Read in the fits table you want to append 
# Use Astropy's 'vstack' function
print(f"Start concatenating files")
concat_legacysim = vstack([Table.read(os.path.join(merged_dir,f'matched_inputs_{i}.fits'), format='fits') for i in file_idx])
print(f"Finished concatenating files")
# Create fits file with new concatenated randoms
print(f"saving {os.path.join(merged_dir,'matched_input_concatenated.fits')}")
concat_legacysim.write(os.path.join(merged_dir,'matched_input_concatenated.fits'), format='fits', overwrite=False)
print(f"saved {os.path.join(merged_dir,'matched_input_concatenated.fits')}")