# COCI Grader

import sys
import os
import filecmp
from subprocess import call, run, TimeoutExpired, SubprocessError, DEVNULL, PIPE
from shutil import copyfile

# Colors
green = '\033[92m'
red = '\033[91m'
reset = '\033[30m'

# Paths
submission_path = "./../"
test_data_path = "./testdata/"

# Set current directory
pos = sys.argv[0].rfind("/")
if pos >= 0:
    os.chdir(sys.argv[0][:pos])

# Program inputs
if len(sys.argv) != 3:
    print("Invalid arguments. The arguments should be: [task name] [time limit]")
    sys.exit()
    
task_name = sys.argv[1]
if not os.path.isdir(test_data_path + task_name):
    print("Invalid arguments. The arguments should be: [task name] [time limit]")
    sys.exit()
try:
    time_limit = float(sys.argv[2])
except ValueError:
    print("Invalid arguments. The arguments should be: [task name] [time limit]")
    sys.exit()

copyfile(submission_path + task_name + ".cpp", task_name + ".cpp");

# Compile
sys.stdout.write("Compiling... ")
try:
    run(["g++", "-O2", "-std=c++0x", task_name + ".cpp"], check=True)
except SubprocessError:
    print("Failed to compile.")
    sys.exit()
print("done")

# Run actual test
step = 1
input_file_prefix = test_data_path + task_name + "/" + task_name + ".in."
output_file_prefix = test_data_path + task_name + "/" + task_name + ".out."
results = []
while (os.path.isfile(input_file_prefix + str(step))):
    copyfile(input_file_prefix + str(step), task_name + ".in")
    found_result = False
    try:
        run(["./a.out"], timeout=time_limit, check=True, stdout=PIPE)
    except TimeoutExpired:
        results.append(["t"])
        found_result = True
    except SubprocessError:
        results.append(["!"])
        found_result = True
    if not found_result:
        with open(task_name + ".out", 'r') as content_file1:
            content1 = content_file1.read().replace("\r\n", "\n")
        with open(output_file_prefix + str(step), 'r') as content_file2:
            content2 = content_file2.read().replace("\r\n", "\n")
        if content1 == content2:
            results.append(["*"])
            found_result = True
        else:
            results.append(["x"])
            found_result = True
    print((green if results[-1][0] == "*" else red) + str(step) + ". " + results[-1][0] + reset)
    step += 1

