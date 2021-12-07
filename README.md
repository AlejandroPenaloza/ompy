# <img width="500" alt="ompy logo heading 2" src="https://user-images.githubusercontent.com/56207845/139159286-893a6e08-c04e-47d5-b405-d9d2d684dc9b.png">

#### Python library development, mainly mathematical tools. Intended to grow to a Python module.

#### Follow the blog [Ompy](https://ompy.tumblr.com).
--------



# Documentation


## ompy
\
Operations and relations for angles and their different measures. (for now, to be developed).

__are_bools(*tuple_arg*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It checks if items in tuple are booleans data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *tuple_arg*: *tuple*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *bool*. True if all items are bools. False otherwise.

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ theta: *int*, *float* or *str*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as respective input is to be "DdMM'SS''" or
"DdMM'SS''" pattern; where D could be any digits number  (under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
*bool*; default *True*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is radians.\

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *float*; original angle now in decimal degrees.

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *theta*: *int*, *float* or *str*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as *str*, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
bool; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
bool; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
*bool*; default *True*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is decimal degrees.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *float*; original angle now in radians.

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *theta*: *int*, *float* or *str*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as str, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
*bool*; default *True*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is radians.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *float*; original angle now in gradians.

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *theta*: *int*, *float* or *str*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert. If provided as *str*, current unit has to be sexagesimal system as 
respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
(under supported range), MM (whole num) and SS (could be decimal) are a 1 or 2 digit number lower than 60.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_sexagesimal:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is degrees, minutes and seconds (sexagesimal measurement system).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
*bool*; default *True*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is radians.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *float*; original angle now in number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_turns(1.23456)
0.196486326544
>>> op.to_turns(12.3456, from_dec_degrees=True)
0.034293333333
>>> op.to_turns("12d34'56''", from_sexagesimal=True)
0.034950617284
>>> op.to_turns(12.3456, from_gradians=True)
0.030864
```
\
__to_sexagesimal(*theta, from_dec_degrees=False, from_gradians=False, from_turns=False, from_radians=True*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It converts the provided angle into the sexagesimal system, where the angle is
    composed by the degrees, minutes and seconds magnitudes; following the pattern 
    D°MM'SS'' (D, MM, SS are the magnitudes; MM and SS are 1 or 2 digit numbers lower than 60).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *theta*: *int* or *float*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angle to convert.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_dec_degrees:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is decimal degrees.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_gradians:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is gradians.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_turns:*
*bool*; default *False*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is number of turns/revolutions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*from_radians:*
*bool*; default *True*.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass *True* if current unit to convert from is radians.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ Sexagesimal angle features (angle as *str* and its parts according
    to the sexagesimal system format) from the original angle.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'sexagesimal angle features', *tuple*-like; consisting on the following fieldnames and values:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"str_"      : *str*; converted angle following the pattern "D°MM'SS''".\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"degrees"   : *int*; degrees section from converted angle.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"minutes"   : *int*; minutes section from converted angle.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"seconds"   : *float*; seconds section from converted angle.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.ompy as op
>>> op.to_sexagesimal(1.23456)
SexagesimalAngle(str_="70°44'6.279200415296''", degrees=70, minutes=44, seconds=6.279200415296)
>>> op.to_sexagesimal(1.23456).str_
"70°44'6.279200415296''"
>>> op.to_sexagesimal(1.23456).degrees
70
>>> op.to_sexagesimal(1.23456).minutes
44
>>> op.to_sexagesimal(1.23456).seconds
6.279200415296

>>> op.to_sexagesimal(12.3456, from_dec_degrees=True)
SexagesimalAngle(str_="12°20'44.16''", degrees=12, minutes=20, seconds=44.16)
>>> op.to_sexagesimal(12.3456, from_gradians=True)
SexagesimalAngle(str_="11°6'39.744''", degrees=11, minutes=6, seconds=39.744)
>>> op.to_sexagesimal(0.123456, from_turns=True)
SexagesimalAngle(str_="44°26'38.976''", degrees=44, minutes=26, seconds=38.976)
```



## cubic
\
Analysis for cubic equations (for now, to be developed).

\
__cbrt(*radicand*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates the real cubic root -principal value- of rational representations of real numbers.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *radicand:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number to take the root of.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *float*; cubic root.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.cubic as cb
>>> cb.cbrt(216)
6.0
>>> cb.cbrt(-27.0)
-3.0
>>> cb.cbrt(10)
2.154434690032
```
\
__to_depressed(*coef_a, coef_b, coef_c, coef_d*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transforms a general cubic equation to a depressed cubic equation. 
It takes general equation coefficients 'a', 'b', 'c', 'd' and returns depressed equation coefficients 'p', 'q'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *coef_a:* *int*, *float*; required (it cannot be 0).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_b:* *int*, *float*; required.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_c:* *int*, *float*; required.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_d:* *int*, *float*; required.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *tuple*. *[0]:* coefficient 'p', *[1]:* coefficient 'q'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.cubic as cb
>>> cb.to_depressed(1, -3, -3, 1)
(-6.0, -4.0)
>>> cb.to_depressed(1, 1, 1, 1)
(0.6666666666666667, 0.7407407407407407)
>>> cb.to_depressed(1, 0, 2, 3)
(2.0, 3.0)
>>> cb.to_depressed(2, 0, 0, 0)
(0.0, 0.0)
```
\
__cbdelta(*coef_p, coef_q, as_frac=False*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates the cubic discriminant (delta) for a depressed cubic equation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *coef_p:* *int*, *float*, *fractions.Fraction*; required. Coefficient 'p' from depressed equation. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_q:* *int*, *float*, *fractions.Fraction*; required. Coefficient 'q' from depressed equation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*as_frac:* *bool* (*True* or *False*); optional. *False* by default. Object type to be returned.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ Cubic delta number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fractions.Fraction object if as_frac passed as *True*, *float* otherwise.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.cubic as cb
>>> cb.cbdelta(3, 4)
20.0
>>> cb.cbdelta(-3, -2)
0.0
>>> cb.delta(5.55555, -4.44444)
-5.6495085912265
```
\
__depressed_roots(*coef_p, coef_q, symbolic*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For depressed cubic equations returns a tuple with its roots.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *coef_p:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coefficient 'p' from depressed equation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_q:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coefficient 'q' from depressed equation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*symbolic:* *bool* (*True* or *False*)
; optional. *False* by default. For requesting symbolic math output.\

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ *tuple*; equation roots.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[0]*      : *str*; first root, represents a real number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[1]*   : *str*; second root, represents a real or complex number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[2]*   : *str*; third root, represents a real or complex number.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.cubic as cb
>>> cb.depressed_roots(-3, -2)
('2.0', '-1.0', '-1.0')
>>> cb.depressed_roots(1, 0)
('0.0', '-0.0 + 1.0i', '-0.0 - 1.0i')
>>> cb.depressed_roots(0, 1)
('-1.0', '0.5 + 0.86602540378i', '0.5 - 0.86602540378i')
>>> cb.depressed_roots(1.11111, 2.22222)
('-1.02650941551',
 '0.513254707755 + 1.37891304479i',
 '0.513254707755 - 1.37891304479i')
```

\
__roots(*coef_a, coef_b, coef_c, coef_d*)__\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates cubic general equations roots.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Parameters:__ *coef_a:* *int*, *float*, *fractions.Fraction*; required (it cannot be 0).\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Equation coefficient 'a'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_b:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Equation coefficient 'b'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_c:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Equation coefficient 'c'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*coef_d:* *int*, *float*, *fractions.Fraction*; required.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Equation coefficient 'd'.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*symbolic:* *bool* (*True* or *False*)
; optional. *False* by default. For requesting symbolic math output.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Returns:__ Equation roots.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sympy* objects display; if *symbolic* passed as *True*.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Tuple* otherwise:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[0]*      : *str*; first root, represents a real number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[1]*   : *str*; second root, represents a real or complex number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[2]*   : *str*; third root, represents a real or complex number.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Examples:__
```
>>> import ompy.cubic as cb
>>> cb.roots(1, -15, 75, -125)
('5.0', '5.0', '5.0')
>>> cb.roots(2, -3, -11, 6)
('3.0', '-2.0', '0.5')
>>> cb.roots(1, 2, 3, 4)
('-1.6506291914',
 '-0.1746854043 + 1.5468688872i',
 '-0.1746854043 - 1.5468688872i')
 >>> cb.roots(3, 0, 0, 0)
 (0.0, 0.0, 0.0)
``` 




### Citations and credits

### SymPy
To cite SymPy in publications use

> Meurer A, Smith CP, Paprocki M, Čertík O, Kirpichev SB, Rocklin M,
> Kumar A, Ivanov S, Moore JK, Singh S, Rathnayake T, Vig S, Granger BE,
> Muller RP, Bonazzi F, Gupta H, Vats S, Johansson F, Pedregosa F, Curry
> MJ, Terrel AR, Roučka Š, Saboo A, Fernando I, Kulal S, Cimrman R,
> Scopatz A. (2017) SymPy: symbolic computing in Python. *PeerJ Computer
> Science* 3:e103 <https://doi.org/10.7717/peerj-cs.103>

SymPy is BSD licensed, so you are free to use it whatever you like, be
it academic, commercial, creating forks or derivatives, as long as you
copy the BSD statement if you redistribute it (see the LICENSE file for
details). That said, although not required by the SymPy license, if it
is convenient for you, please cite SymPy when using it in your work and
also consider contributing all your changes back, so that we can
incorporate it and all of us will benefit in the end.

```
Copyright (c) 2006-2021 SymPy Development Team

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of SymPy nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

--------------------------------------------------------------------------------

Patches that were taken from the Diofant project (https://github.com/diofant/diofant)
are licensed as:

Copyright (c) 2006-2018 SymPy Development Team,
              2013-2021 Sergey B Kirpichev

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of Diofant or SymPy nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

--------------------------------------------------------------------------------

Submodules taken from the multipledispatch project (https://github.com/mrocklin/multipledispatch)
are licensed as:

Copyright (c) 2014 Matthew Rocklin

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of multipledispatch nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

--------------------------------------------------------------------------------

The files under the directory sympy/parsing/autolev/tests/pydy-example-repo
are directly copied from PyDy project and are licensed as:

Copyright (c) 2009-2021, PyDy Authors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name of this project nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL PYDY AUTHORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
