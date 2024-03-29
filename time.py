# %%

import os
import sys
import numpy as np
import pandas as pd

# %%

def pace_to_decimal(pace_str):
    """
    Convert pace time from "minutes:seconds" format to decimal minutes.
    
    Parameters:
    pace_str (str): Pace time in "minutes:seconds" format.
    
    Returns:
    float: Pace time in decimal minutes.
    """
    minutes, seconds = map(int, pace_str.split(':'))
    return minutes + seconds / 60

def decimal_to_pace(decimal_minutes):
    """
    Convert pace time from decimal minutes to "minutes:seconds" format.
    
    Parameters:
    decimal_minutes (float): Pace time in decimal minutes.
    
    Returns:
    str: Pace time in "minutes:seconds" format.
    """
    minutes = int(decimal_minutes)
    seconds = int((decimal_minutes - minutes) * 60)
    return f"{minutes}:{str(seconds).zfill(2)}"  # zfill(2) ensures the seconds are always two digits

# %% 

pace_list = ["8:41", "9:29", "9:33", "9:43", "9:45", "9:29", "9:31", "9:58", "10:34"]
pace_list_1 = ["8:43", "9:27", "9:19", "9:17", "9:15", "9:04", "8:51"]

# Convert to decimal minutes
decimal_arr = np.array([pace_to_decimal(pace) for pace in pace_list])
decimal_arr_1 = np.array([pace_to_decimal(pace) for pace in pace_list_1])

# Convert back to "minutes:seconds" format
pace_list_convert = [decimal_to_pace(decimal) for decimal in decimal_arr]
pace_list_convert_1 = [decimal_to_pace(decimal) for decimal in decimal_arr_1]

print(pace_list)
print(decimal_arr)
print(pace_list_convert)  # Slight rounding errors here, within the second.

# %% 

print(decimal_to_pace(np.mean(decimal_arr)))
print(decimal_to_pace(np.mean(decimal_arr_1)))


# %%
