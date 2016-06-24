# COCI-grader
Python 3 code that grades submissions to COCI problmes.
Example files included to display useage.

## Setup
First set up a base directory that will contain your code submissions for this contest (each contest needs its own base directory). This base directory should contain:
* Your .cpp code submissions (in the form taskname.cpp, all lowercase)
* A grader directory that contains:
  * The python grader file (coci_grader.py)
  * directory which is a direct download of the contest's test data, but it should be called testdata.

## Usage
Call this function when in the grader directory:
```
python3 coci_grader.py [task name] [time limit]
```
or when in the base directory call:
```
python3 grader/coci_grader.py [task name] [time limit]
```
For example:
```
python3 coci_grader.py vudu 1
```
submits task vudu with a time limit of 1 second.

