# <img width="500" alt="ompy logo heading 2" src="https://user-images.githubusercontent.com/56207845/139159286-893a6e08-c04e-47d5-b405-d9d2d684dc9b.png">

#### Python library development, mainly mathematical tools. Intended to grow to a Python module.
--------



## Documentation


### ompy
\
This file provides functions to be used with angles and their different measures. (FOR NOW, TO BE DEVELOPED).

__are_bools(*tuple_arg*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It checks if items in tuple are booleans data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *tuple_arg*: tuple; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ bool. True if all items are bools. False otherwise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.are_bools(True, 2, "Hello")
False
>>> op.are_bools(True, False, True)
True
```
\
__to_dec_degrees(*theta, from_sexagesimal=False, from_gradians=False, from_turns=False, from_radians=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle to decimal degrees.\
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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_dec_degrees(1.23456)
70.735077555671
>>> op.to_dec_degrees("12d34'56''", from_sexagesimal=True)
12.582222222222
>>> op.to_dec_degrees(12.3456, from_gradians=True)
11.11104
>>> op.to_dec_degrees(0.123456, from_turns=True)
44.44416
```
\
__to_radians(*theta, from_sexagesimal=False, from_gradians=False, from_turns=False, from_dec_degrees=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle to radians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ theta: int, float or str; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
bool; default True.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is decimal degrees.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ float; original angle now in radians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_radians(12.3456)
0.215471368134
>>> op.to_radians("12d34'56''", from_sexagesimal=True)
0.219601204995
>>> op.to_radians(12.3456, from_gradians=True)
0.193924231321
>>> op.to_radians(0.123456, from_turns=True)
0.775696925283
```
\
__to_gradians(*theta, from_dec_degrees=False, from_sexagesimal=False, from_turns=False, from_radians=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle to gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ theta: int, float or str; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
bool; default True.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is radians.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ float; original angle now in gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_gradians(1.23456)
78.594530617412
>>> op.to_gradians(12.3456, from_dec_degrees=True)
13.7173333333
>>> op.to_gradians("12d34'56''", from_sexagesimal=True)
13.98024691358
>>> op.to_gradians(0.123456, from_turns=True)
49.3824
```
\
__to_turns(*theta, from_dec_degrees=False, from_sexagesimal=False, from_gradians=False, from_radians=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle to number of equivalent turns or revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ theta: int, float or str; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
bool; default False.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
bool; default True.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass True if current unit to convert from is radians.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ float; original angle now in number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_turns(1.23456)
0.196486326544
>>> op.to_turns(12.3456, from_dec_degrees=True)
0.034293333333
>>> op.to_turns("12d34'56''", from_sexagesimal=True)
0.034950617284
>>> op.to_turns(0.123456, from_gradians=True)
0.030864
```
