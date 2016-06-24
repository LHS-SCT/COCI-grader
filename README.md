# COCI-grader
Python 3 code that grades submissions to COCI problmes.
Example files included to display useage.

## Setup
First set up a base directory that will contain your code submissions for this contest (each contest needs its own base directory). This base directory should contain:
* Your .cpp code submissions (in the form taskname.cpp, all lowercase)
* A grader directory that contains:
  * The python grader file (coci_grader.py)
  * directory which is a direct download of the contest's test data, but it should be called testdata.
Note that the base directory for each contest can contain whatever additional files you want, as long as it has the sumbission file (you can even work on your code here). The grader script only makes edits to files in the grader directory.

## Usage
Call this function from the grader directory:
```
python3 coci_grader.py [task name] [time limit]
```
or call from the base directory:
```
python3 grader/coci_grader.py [task name] [time limit]
```
For example:
```
python3 coci_grader.py vudu 1
```
submits task vudu with a time limit of 1 second.

