### Basic test cases can be fun !!

#### most-basic.py 

The `most-basic.py` includes a most basic implementation for what testing essentially is.

Two functions are defined `addition` & `subtraction` that take 2 parameters as input and returns the respective answer.

Two more function are defined which are not implemented the wrong way, defined by the names `wrong_addition` and `wrong_subtraction`

and then, there are 4 test cases defined one for each function which will test those functions by providing the appropriate
inputs and expecting the right outcome, if not received it's gonna burst. !!

To execute : `python most-basic.py`

#### basic.py

The `basic.py` takes the `basic.py` to an whole another level by implementing the `unittest` library which is built in by Pyhton

It implements the `unittest` library by defining a class as `testing` and implements the same test cases into, what is improves
is, in `most-basic.py` if one test fails it's gonna stop the execution of the tests at the moment, contrast to it here in `basic.py`
thanks to `unittest` all the test functions will be executed and return the errors all together along with specifying which tests were failed.

For people who are interested in exploring this topic more : [Real Python](https://realpython.com/python-testing/)

##### Best of Luck for writing unit test's for your life, It's an whole another world.

Thank you [Umair Kamran](https://github.com/UmairKamran) for recommending the implementation idea for `addition` & `subtraction`
to get a grasp on unit testing.