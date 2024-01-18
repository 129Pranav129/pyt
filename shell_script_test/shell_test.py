import os
import sys
import subprocess 

# subprocess.call(['/mnt/c/pyt/shell_script_test/run.sh'])

# subprocess.run(["/mnt/c/pyt/shell_script_test/run.sh"], shell=True)

script_path = '/mnt/c/pyt/shell_script_test/run.sh'

# Run the shell script using subprocess
subprocess.run(['bash', script_path])