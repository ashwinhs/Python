# **Python Learning**
## Example 1: **Convert Decimals to Roman**
(Files begin with Int2Roman) <br />

**Solution 1**: This is the round about solution which uses the position of the digit in the number and uses some crazy logic to convert from Integer to Roman! <br />
**Solution 2**: This is a super condensed method to get the same result. Essentially, the logic is to do loop over the tupules/list, divide the number by each of the integers. If the quotient is > 1, then we have match. Multiply that with the roman number to get the actual value. <br />
**Solution 3**: Same as 2. But uses Enums, Class methods and "yield". Good to understand Python!
<br />
## Example 2: **Logic Gates**
(File : LogicGates.py) <br />
This is an example from Interactive python which is particularly interesting since it helps us comprehend "OOP" Object oriented Python.
<br />
## Example 3: **Test Performance, Creating lists**
(File: ListPerformance.py) <br />
This script tests creating lists using 4 different ways - <br />
* Concatenate (Concatenate one list with another)
* Appending (using append function)
* List comprehension
* Using Range and List functions
<br />We finally time each of the function using timeit module's Timer function. This runs each of the function 1000times before returning the average time taken.
