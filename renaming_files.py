import os
import glob

for i, filename in enumerate(glob.glob('*.txt')):
    os.rename(filename, ('file-' + str(i) + '.txt'))