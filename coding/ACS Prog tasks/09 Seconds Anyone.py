#program to turn a time from hh:mm:ss to seconds
#function
def get_seconds(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#output
sTime = str(input("Please input the time"))
print(get_seconds(sTime))