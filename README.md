# Powered-Unit-Converter #
The program does unit conversion — provide the translation of a quantity specified by a certain amount in one source unit and a destination unit
## Program Requirement ##
- [x] Welcome text for your program, listing your name, the program's use, and its input format
- [x] A list of all the categories and units within that category you support so the user knows what they can do
- [x] A repeating loop that asks for conversions over an over in the format we described above.
- [x] If the format is not exactly right, a friendly, helpful error message should be printed along with the prompt again.
## Result ##
```
##############################################################################################
Welcome to our Python-powered Unit Converter

You can convert Distances , Weights , Volumes & Times to one another, but only
within units of the same category, which are shown below. E.g.: 1 mi in ft
           		Distances: ft cm mm mi m yd km in   
           		Weights:   lb mg kg oz g            
           		Volumes:   floz qt cup mL L gal pint
##############################################################################################
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 10 mi in m
16093.4
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ln mi in m
ERROR2
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 10 ln in m
ERROR1
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 10 mi ln m
ERROR3
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 100 m in yd
109.36099999999999
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 1000 mm in km
0.001
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: 10
ERROR
Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: q
Thanks for converting with us.
```
