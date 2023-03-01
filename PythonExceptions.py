"""
Syntax errors occur when the parser detects an incorrect statement.
This time, you ran into an exception error. This type of error occurs whenever
syntactically correct Python code results in an error.
"""
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()
