"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!
Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
A signal is provided to each wire by a gate, another wire, or some specific value.
Each wire can only get a signal from one source, but can provide its signal to multiple destinations.
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
    x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
If, for some reason, you'd like to emulate the circuit instead, almost all programming languages
(for example, C, JavaScript, or Python) provide operators for these gates.

_   _ _ _ _ _
32 16 8 4 2 1

1234 = 10011010010

1 = 0001
<< 2
000100 = 4

'AND' : '&'
'OR' : '|'

"""


"""

ASSUMPTIONS: 
1) Build a dictionary for bitwise operations
2) Building a dictionary from my input (each wire gets 1 signal)
3) I don't need to parse ALL instructions
4) No loops or recursions (DAGs)
5) all inputs must be INTs



OPERATIONS:
The Operators:
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.


HIGH LEVEL FLOW:

Build a dictionary object for my opeartors -- check if I can concat operations together
-- can you cast a string into a bitwise operation
e.g. y RSHIFT 2 --> ((456) >> 2)

Build a dictionary for input.  Key to value
{'dr': '~ dq', 'dq': 'dd & do', '

CRUX OF PROBLEM:
how do you process each of the key inputs?
Looks like a tree of possibilities?
a -> jj, jc -> bo, rd, m, lk


PSEUDOCODE:
Build it recursively



"""













"""


Assumptions:
Python has set of bit operators to do this to base10 integers

    Each input should map to a bit operator (make ints binary)
    AND -> 26 -> 0000000000011010 
       AND 53 -> 0000000000110101 
          EQUALS 0000000000010000 -> 16
    
    OR -> 0000000000011010 -> 26
       OR 0000000000110101 -> 53
   EQUALS 0000000000111111 -> 63
   
   26 LSHIFT 2 -> 0000000000011010[00] -> 0000000001101000 -> 104
   
   56 RSHIFT 2 -> 0000000000111000 -> 00000000001110 -> 14
   
   NOT 104 -> ~0000000001101000 -> 1111111110010111 -> 65431

High Level Flow:
    Create Dictionary of inputs. 
    Key is the output node
    Value is the transformation

Crux of problem:
    

Pseudocode:
mapping_func(input_operation):
    operation_dict = {
    "AND": "&"
    , "RSHIFT" : ">>"
    , "LSHIFT" : "<<"
    , "NOT" : "~"
    , "OR" : "|"
    , "XOR" : "^"
    }

with open(file) as f:
    new_dict = {}
    For line in f.readlines():
        out_temp = line.split('->')
        key, val = 
        
build a recursion system to handle the key parsing

"""