string = '1h 45m,360s,25m,30m 120s,2h 60s'
string_new = string.split(',')
minutes = 0

for total in string_new:
    time = total.split()
    for t in time:
        if 'h' in t:
            hour = int (t.replace('h', ''))
            minutes += hour * 60
        elif 'm' in t:
            minute = int(t.replace('m', ''))
            minutes += minute
        elif 's' in t:
            sec = int (t.replace('s', ''))
            minutes += sec / 60

print (int(minutes))


