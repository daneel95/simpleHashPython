import time

def calculate_hash_python(string):
    hs = string.__hash__()
    if (hs < 0):
        hs = -hs
    while hs > 10:
        hs = int(hs / 10) + hs % 10
    
    return hs

def calculate_hash_with_sleep(string):
    time.sleep(threadSleepValue)
    
    return calculate_hash_python(string)
	