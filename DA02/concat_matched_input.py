import os
# to concatenate matched inputs 00 to 14 for south
from astropy.table import Table, vstack
run = 'south'
merged_dir = os.path.join(os.getenv('CSCRATCH'),'legacysim','dr9','DA02',run,'file0_rs0_skip0','merged')
nber_files = 12
file_idx = file_idx = ["%.2d"%i for i in range(nber_files)]
#Read in the fits table you want to append 
# Use Astropy's 'vstack' function
concat_legacysim = vstack([Table.read(os.path.join(merged_dir,f'matched_inputs_{i}.fits'), format='fits') for i in file_idx])
# Create fits file with new concatenated randoms
concat_legacysim.write(os.path.join(merged_dir,'matched_input_concatenated.fits'), format='fits', overwrite=False)