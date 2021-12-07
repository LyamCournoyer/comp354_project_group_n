# comp354_project_group_n
comp 354 project for group n

# Interpreter
The intepreter executes files.

It was designed using python 3.10.
## How to run
There is a test file _interpreter/test_file.txt_ that can be used (any file can be passed)

`python ./interpreter/interpreter.py --file interpreter/test_file.txt`

# Editor
Currently pretty basic and based off of https://pythonguides.com/python-tkinter-editor#Python_Tkinter_code_editor
Only minor changes have been done to be integrated with the interpreter.

## How to run
`python ./editor/editor.py`

# Tests
The tests are writting using [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)

## How to run
### A single test file
`python -m  tests.test_math_actions`
### All test files
`python -m unittest discover -v -s interpreter/ `