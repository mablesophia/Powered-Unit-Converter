#########################################################################################################
# Program Name: Powered Unit Converter
# Date:         17 Sep 2018
# Description:  The program does unit conversion — provide the translation of a quantity
#               specified by a certain amount in one source unit and a destination unit
#########################################################################################################
import sys

distance_list = ['ft', 'cm', 'mm', 'mi', 'm', 'yd', 'km', 'in' ]
weights_list  = ['lb', 'mg', 'kg', 'oz', 'g']
volumes_list  = ['floz', 'qt', 'cup', 'mL', 'L', 'gal', 'pint']

def menu():
    ''' The user interface of the powered unit coverter '''
    print('##############################################################################################')
    print('Welcome to our Python-powered Unit Converter\n')
    print('You can convert Distances , Weights , Volumes & Times to one another, but only')
    print('within units of the same category, which are shown below. E.g.: 1 mi in ft\n\
           \t\tDistances: ft cm mm mi m yd km in   \n\
           \t\tWeights:   lb mg kg oz g            \n\
           \t\tVolumes:   floz qt cup mL L gal pint') 
    print('##############################################################################################')

    while True:
        user_input = input('Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ')
        if len(user_input.split()) == 1:
            if user_input == 'q':
                print('Thanks for converting with us.')
                sys.exit(0)
            else:
                print('ERROR')
        else:
            if len(user_input.split()) == 4:
                source_nbr, source_unit, word_in, dest_unit = user_input.split(' ')
                if source_nbr.isdigit() == False:
                    print('ERROR2')
                elif source_unit not in distance_list or dest_unit not in distance_list:
                    print('ERROR1')
                elif word_in != 'in':
                    print('ERROR3')
                else:
                    nbr = float(source_nbr)
                    src_dist(nbr, source_unit, dest_unit)
##                if source_unit in distance_list and dest_unit in distance_list:
##                    src_dist(source_nbr, source_unit, dest_unit)
##                else:
##                    print('ERROR')


def src_dist(nbr, source_unit, dest_unit):
    ''' Convert distance units '''
    if source_unit == 'ft':
        _src_ft(nbr, dest_unit)
    if source_unit == 'cm':
        _src_cm(nbr, dest_unit)
    if source_unit == 'mm':
        _src_mm(nbr, dest_unit)
    if source_unit == 'mi':
        _src_mi(nbr, dest_unit)
    if source_unit == 'm':
        _src_m(nbr, dest_unit)
    if source_unit == 'yd':
        _src_yd(nbr, dest_unit)
    if source_unit == 'km':
        _src_km(nbr, dest_unit)
    if source_unit == 'in':
        _src_in(nbr, dest_unit)

def _src_in(nbr, dest_unit):
    ''' Convert in to other units '''
    in_dict = {'ft': 0.0833333, 'cm': 2.54, 'mm': 25.4, 'mi': 0.0000157828,
                'm': 0.0254, 'yd': 0.0277778, 'km': 0.0000254, 'in': 1 }
    for key, values in in_dict.items():
        if dest_unit == key:
            print(float(source_nbr)*values) 

def _src_km(nbr, dest_unit):
    ''' Convert km to other units '''
    km_dict = {'ft': 3280.84, 'cm': 100000, 'mm': 1000000, 'mi': 0.621371,
                'm': 1000, 'yd': 1093.61, 'km': 1, 'in': 39370.1 }
    for key, values in km_dict.items():
        if dest_unit == key:
            print(float(nbr)*values) 

def _src_yd(nbr, dest_unit):
    ''' Convert yd to other units '''
    yd_dict = {'ft': 3, 'cm': 91.44, 'mm': 914.4, 'mi': 0.000568182,
                'm': 0.9144, 'yd': 1, 'km': 0.0009144, 'in': 36 }
    for key, values in yd_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)   

def _src_m(nbr, dest_unit):
    ''' Convert m to other units '''
    m_dict = {'ft': 3.28084, 'cm': 100, 'mm': 1000, 'mi': 0.000621371,
                'm': 1, 'yd': 1.09361, 'km': 0.001, 'in': 39.3701 }
    for key, values in m_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)

def _src_mi(nbr, dest_unit):
    ''' Convert mi to other units '''
    mi_dict = {'ft': 5280, 'cm': 160934, 'mm': 1609340, 'mi': 1,
                'm': 1609.34, 'yd': 1760, 'km': 1.60934, 'in': 63360 }
    for key, values in mi_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)

def _src_mm(nbr, dest_unit):
    ''' Convert mm to other units '''
    mm_dict = { 'ft': 0.00328084, 'cm': 0.1, 'mm': 1, 'mi': 0.000000621371,
                'm': 0.001, 'yd': 0.00109361, 'km': 0.000001, 'in': 0.0393701 }
    for key, values in mm_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)    

def _src_cm(nbr, dest_unit):
    ''' Convert cm to other units '''
    cm_dict = { 'ft': 0.0328084, 'cm': 1, 'mm': 10, 'mi': 0.00000621371,
                'm': 0.01, 'yd': 0.0109361, 'km': 0.00001, 'in': 0.393701 }
    for key, values in cm_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)

def _src_ft(nbr, dest_unit):
    ''' Convert ft to other units '''
    ft_dict = { 'ft': 1, 'cm': 30.48, 'mm': 304.8, 'mi': 0.000189394,
                'm': 0.3048, 'yd': 0.333333, 'km': 0.0003048, 'in': 12 }
    for key, values in ft_dict.items():
        if dest_unit == key:
            print(float(nbr)*values)
        

if __name__ == '__main__':
    menu()
