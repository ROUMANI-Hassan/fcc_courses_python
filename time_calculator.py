def add_time(start, duration, day=0):
    print(start,duration,day)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    if isinstance(day,list):
        pass
    else:
        if str(day).isdigit():
            day = ['', day]
        else:
            day = day.lower()
            day = [x for x in day]
            day[0] = day[0].upper()
            day = ''.join(day)
            day = [day, 0]

    if duration == '0:00':
        if day[0] == '':
            if day[1]==0:
                return start
            elif day[1]==1:
                return f'{start} (next day)'
            else:
                return f'{start} ({day[1]} days later)'
        else:
            if day[1]==0:
                return f'{start}, {day[0]}'
            elif day[1]==1:
                return f'{start}, {day[0]} (next day)'
            else:
                return f'{start}, {day[0]} ({day[1]} days later)'
            

    time = start.split(':')
    start_hour = int(time[0])
    start_min = int(time[1].split(' ')[0])

    time = duration.split(':')
    duration_hour = int(time[0])
    duration_min = int(time[1])

    time_of_day = start[-2:]

    if start_hour == 12:
        start_hour = 0

    if start_min + duration_min >= 60:
        start_min = start_min + duration_min
        duration_min = '00'
        start_hour = start_hour + (start_min//60)
        start_min = '00' if abs(start_min - 60*(start_min//60))==0 else str(abs(start_min - 60*(start_min//60)))
    else:
        start_min = start_min + duration_min
        duration_min = '00'

    if len(str(start_min))==1:
            start_min = '0'+ str(start_min)

    start_hour = start_hour + duration_hour
    if start_hour >= 12:
        duration_hour = start_hour-12
        start_hour = 12
        if time_of_day == 'PM':
            time_of_day = 'AM'
            day[1] = day[1] + 1
            day[0] = days[(days.index(day[0])+1)%7] if day[0] in days else ''
        else:
            time_of_day = 'PM'
    else:
        duration_hour = 0
    duration = f'{duration_hour}:{duration_min}'
    start = f'{start_hour}:{start_min} {time_of_day}'
    print(start)
    return add_time(start,duration,day)

#print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

#print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

#print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

#print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

#print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('8:16 PM', '466:02', 'tuesday'))
# Returns: 7:42 AM (9 days later)
