# COCI Grader

import sys
import os.path
import filecmp
from subprocess import call, run, TimeoutExpired, SubprocessError
from shutil import copyfile

# Colors:
green = '\033[92m'
red = '\033[91m'
reset = '\033[30m'

test_data_path = "./testdata/"

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
        
submission_path = "./"

# Compile:
sys.stdout.write("Compiling... ")
try:
    run(["g++", "-O2", "-std=c++0x", submission_path + task_name + ".cpp"], check=True)
except SubprocessError:
    print("Failed to compile.")
    sys.exit()
print("done")

# Copy .in and .out files (will be overwritten)
tempin_name = "tempin.txt"
tempout_name = "tempout.txt"
was_in = False
was_out = False
if os.path.isfile(submission_path + task_name + ".in"):
    copyfile(submission_path + task_name + ".in", submission_path + tempin_name)
    was_in = True
if os.path.isfile(submission_path + task_name + ".out"):
    copyfile(submission_path + task_name + ".out", submission_path + tempout_name)
    was_out = True

# Run actual test
step = 1
input_file_prefix = test_data_path + task_name + "/" + task_name + ".in."
output_file_prefix = test_data_path + task_name + "/" + task_name + ".out."
results = []
while (os.path.isfile(input_file_prefix + str(step))):
    copyfile(input_file_prefix + str(step), submission_path + task_name + ".in")
    found_result = False
    try:
        run([submission_path + "a.out"], timeout=time_limit, check=True)
    except TimeoutExpired:
        results.append(["t"])
        found_result = True
    except SubprocessError:
        results.append(["!"])
        found_result = True
    if not found_result:
        with open(submission_path + task_name + ".out", 'r') as content_file1:
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

if was_in:
    copyfile(submission_path + tempin_name, submission_path + task_name + ".in")
if was_out:
    copyfile(submission_path + tempout_name, submission_path + task_name + ".out")

