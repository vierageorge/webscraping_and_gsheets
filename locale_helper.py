from locale import *

def perc_to_float(input):
    without_percent = input.replace("%","")
    try:
        output = float(without_percent)/100
    except ValueError:
        output = atof(without_percent)/100
    return output

def money_to_float(input):
    without_curr = input.replace("$","")
    without_comma = without_curr.replace(",","")
    output = float(without_comma)
    return output

def longnum_to_float(input):
    setlocale(LC_ALL,'')
    out_local_co = atof(input)
    setlocale(LC_ALL,'en-US')
    out_local_us = atof(input)
    setlocale(LC_ALL,'')
    return out_local_co if out_local_co >= out_local_us else out_local_us
