import os
import sys
import shutil

# Get directory name
mydir= r"C:\Users\NareshKumarD\Documents\GitHub\rl_wb\_build"

try:
    shutil.rmtree(mydir)
    print("Removed")
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
