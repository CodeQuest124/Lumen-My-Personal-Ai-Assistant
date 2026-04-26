'''
import datetime

def get_time_information() -> str:
    now = datetime.datetime.now()
    return(
        f"Current Real-time Information:\n"
        f"Day: {now.strftime('%A')}\n"     #Monday
        f"Date: {now.strftime('%d')}\n"    #05
        f"Month: {now.strftime('%B')}\n"   #February
        f"Year: {now.strftime('%Y')}\n"    #2026
        f"Time: {now.strftime('%H')} hours, {now.strftime('%M')} minutes, {now.strftime('%S')} seconds\n"
    )
'''    
from datetime import datetime

def get_time_information() -> str:
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y, %I:%M %p")
