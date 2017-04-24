# Code for parsing a TLE file
from datetime import datetime



def read_tle_file(tlefile, **kwargs):
    """
    
    Read in a TLE file and return the TLE that is closest to the date you want to
    propagate the orbit to.
    """
    times = []
    line1 = []
    line2 = []
    
    from os import path
    from datetime import datetime
    # Catch if the file can't be opened:
    
    try:
        f = open(tlefile, 'r')
    except FileNotFoundError:
        print("Unable to open: "+tlefile)
    
    ln=0
    for line in f:
#        print(line)
        if (ln == 0):
            year= int(line[18:20])
            day = int(line[20:23])
            
            times.extend([datetime.strptime("{}:{}".format(year, day), "%y:%j")])
            line1.extend([line.strip()])
            ln=1
        else:
            ln=0
            line2.extend([line.strip()])
    f.close()
    return times, line1, line2

def get_epoch_tle(epoch, tlefile):
    """
    
    Find the TLE that is closest to the epoch you want to search.
    
    epoch is a datetime object, tlefile is the file you want to search through.
    
    """

    times, line1, line2 = read_tle_file(tlefile)
    from datetime import datetime

    mindt = 100.
    min_ind = 0
    for ind, t in enumerate(times):
        dt = abs((epoch -t).days)
        if dt < mindt:
            min_ind = ind
            mindt = dt

    good_line1 = line1[min_ind]
    good_line2 = line2[min_ind]

    return mindt, good_line1, good_line2


