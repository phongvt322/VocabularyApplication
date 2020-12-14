# debug script

# Importing subprocess
import subprocess

# Your command
cmd = "python3 Preeeeee.py"

# Starting process
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Getting the output and errors of the program
stdout, stderr = process.communicate()

# Printing the errors
print(stderr)
