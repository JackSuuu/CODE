import subprocess

subprocess.run(["ls", "-l"])
# run the command in terminal ls -l
completed = subprocess.run(["ls", "-l"],
                           capture_output=True,
                           text=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)

# how to run other python file in this python file
completed = subprocess.run(["python3", "/Users/jack/Desktop/Python/Python_standard_library/Time_mosh/Timestamps_mosh.py"],
                           capture_output=True,
                           text=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
