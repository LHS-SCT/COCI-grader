# COCI Grader

import sys
import os
import filecmp
import string
from subprocess import call, run, TimeoutExpired, SubprocessError, DEVNULL, PIPE
from shutil import copyfile

# Colors
green = '\033[92m'
red = '\033[91m'
reset = '\033[0m'

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
if not os.path.isfile(submission_path + task_name + ".cpp"):
    print("Submission file not found.")
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
suffixes = [''] + list('abcdefghijklmnopqrstuvwxyz')
si = 0 # suffix index
results = []
while (os.path.isfile(input_file_prefix + str(step)) or os.path.isfile(input_file_prefix + str(step) + 'a')):
    results.append(["*"])
    for suffix in suffixes:
        if os.path.isfile(input_file_prefix + str(step) + suffix) == False:
            continue
        copyfile(input_file_prefix + str(step) + suffix, task_name + ".in")
        found_result = False
        try:
            run(["./a.out"], timeout=time_limit, check=True, stdout=PIPE)
        except TimeoutExpired:
            results[-1] = ["t"]
            found_result = True
            break
        except SubprocessError:
            results[-1] = ["!"]
            found_result = True
            break
        if not found_result:
            if os.path.isfile(task_name + ".out") == False:
                results[-1] = ["!"]
                found_result = True
                break
            with open(task_name + ".out", 'r') as content_file1:
                content1 = content_file1.read().replace("\r\n", "\n")
            with open(output_file_prefix + str(step) + suffix, 'r') as content_file2:
                content2 = content_file2.read().replace("\r\n", "\n")
            if content1 == content2:
                found_result = True
            else:
                results[-1] = ["x"]
                found_result = True
                break
    print((green if results[-1][0] == "*" else red) + str(step) + ". " + results[-1][0] + reset)
    step += 1

