import datetime
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    # Get the current system time with microseconds
    system_time = datetime.datetime.now()

    # Extract the hours, minutes, seconds, and microsecond parts
    #hours_part = system_time.hour
   # minutes_part = system_time.minute
    #seconds_part = system_time.second
    microseconds_part = system_time.microsecond

    # Combine hours, minutes, seconds, and microseconds to form a floating-point number
    #current_time_in_seconds = hours_part * 3600 + minutes_part * 60 + seconds_part + microseconds_part / 1_000_000

    # Check if the current time (in seconds) is prime
    if is_prime(int(microseconds_part)):
        print(microseconds_part)
        break

    # Wait for a short duration before checking again
    time.sleep(0.1)