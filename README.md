# COCI-grader
Python 3 code that grades submissions to COCI problems.
Example files from task "VUDU" ('15 - '16 Contest #2) included to display usage.

## Setup
First set up a base directory that will contain your code submissions for the contest (each contest needs its own base directory). This base directory should contain:

* Your .cpp code submissions (in the form `taskname.cpp`, all lowercase)
* A *grader* directory that contains:
    * Directory which is a direct download of the contest's test data, but renamed *testdata*
    * Depending on your OS:
        * Include the python grader file `coci_grader.py` if on MacOS
        * Include the python grader file `coci_win.py` if on Windows

Note that the base directory for each contest can contain whatever additional files you want, as long as it has the sumbission file. The grader script only makes edits to files in the grader directory. You should never have to edit the grader directory once you set it up with either `coci_grader.py` or `coci_win.py` and the *testdata* directory.

## Usage

> ### MacOS

> Call this from the grader directory:
```
$ python3 coci_grader.py [task name] [time limit]
```
or call from the base directory:
```
$ python3 grader/coci_grader.py [task name] [time limit]
```
For example:
```
$ python3 coci_grader.py vudu 1
```
submits task "VUDU" with a time limit of 1 second.

===

> ### Windows

> Call this from the grader directory:
```
$ py -3 coci_win.py [task name] [time limit]
```
or call from the base directory:
```
$ py -3 grader/coci_win.py [task name] [time limit]
```
For example:
```
$ py -3 coci_win.py vudu 1
```
submits task "VUDU" with a time limit of 1 second.

## Other

Please contact Louie Golowich or Vivek Bhupatiraju with any questions!



