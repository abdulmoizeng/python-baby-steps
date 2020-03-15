# Interactive debugging in python:
from IPython import embed

var1 = 'something'
embed()  # <- quit for moving to next breakpoint (if any)
# when debugger is stopped user can check variables call methods with in the current scope
print('Its interactive debugging')
var2 = 'something different'
embed()
