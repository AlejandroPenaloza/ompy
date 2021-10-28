# <img width="500" alt="ompy logo heading 2" src="https://user-images.githubusercontent.com/56207845/139159286-893a6e08-c04e-47d5-b405-d9d2d684dc9b.png">

#### Python library development, mainly mathematical tools. Intended to grow to a Python module.
--------



## Documentation


### ompy
\
This file provides functions to be used with angles and their different measures. (FOR NOW, TO BE DEVELOPED).

__are_bools__(*tuple_arg*)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It checks if items in tuple are booleans data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *tuple_arg*: tuple; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ bool. True if all items are bools. False otherwise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Example:__
```
>>> import ompy.ompy as op
>>> op.are_bools(True, 2, "Hello")
False
>>> op.are_bools(True, False, True)
True
```
\
__to_dec_degrees(*theta, from_sexagesimal=False, from_gradians=False, from_turns=False, from_radians=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle into decimal degrees.\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ theta: int, float or str; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as respective input is to be "DdMM'SS''" or
"DdMM'SS''" pattern; where D could be any digits number  (under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
bool; default True.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is radians.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ float; original angle now in decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Example:__
```
>>> import ompy.ompy as op
>>> op.to_dec_degrees(1.23456)
70.735077555671
>>> op.to_dec_degrees("12d34'56''", from_sexagesimal=True)
12.582222222222
```
