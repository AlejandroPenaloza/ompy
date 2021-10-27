# <img width="500" alt="ompy logo heading 2" src="https://user-images.githubusercontent.com/56207845/139159286-893a6e08-c04e-47d5-b405-d9d2d684dc9b.png">

#### Python library development, mainly mathematical tools. Intended to grow to a Python module.
--------


## Documentation


### ompy

This file provides functions to be used with angles and their different measures. (FOR NOW, TO KEEP BEING DEVELOPED).

__are_bools__(*tuple_arg*)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It checks if items in tuple are booleans data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *tuple_arg*: tuple.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ bool. True if all items are bools.

```
>>> import ompy.ompy as op
>>> op.are_bools(True, 2, "Hello")
False
>>> op.are_bools(True, False, True)
True
```
