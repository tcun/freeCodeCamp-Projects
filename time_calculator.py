def add_time(start, duration, day_req = "N/A"):

    start_h = int(start.split(":")[0])
    if "PM" in start: 
        start_h += 12

    start_min = int(start.split(":")[1].split()[0])

    dur_h = int(duration.split(":")[0])
    dur_min = int(duration.split(":")[1])
    days_later = int((start_h + dur_h + int((start_min + dur_min) / 60)) / 24) 

    hour_format = (start_h + dur_h + int((start_min + dur_min) / 60)) % 24 
    PM = False  
    if hour_format >= 12:      
        hour_format -= 12
        if hour_format == 0:
            hour_format = 12
        PM = True

    if hour_format == 0:
            hour_format = 12

    minute_format = str((start_min + dur_min) % 60).zfill(2) 

    if day_req == "N/A": 
        if days_later > 1:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM ({days_later} days later)"
            else:
                new_time = f"{hour_format}:{minute_format} AM ({days_later} days later)"
        elif days_later == 1:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM (next day)"
            else:
                new_time = f"{hour_format}:{minute_format} AM (next day)"
        else:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM"
            else:
                new_time = f"{hour_format}:{minute_format} AM"
    else: 
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
        day = days[(days.index(day_req.capitalize()) + 1 + days_later) % 7 - 1] 
        if days_later > 1:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM, {day} ({days_later} days later)"
            else:
                new_time = f"{hour_format}:{minute_format} AM, {day} ({days_later} days later)"
        elif days_later == 1:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM, {day} (next day)"
            else:
                new_time = f"{hour_format}:{minute_format} AM, {day} (next day)"
        else:
            if PM:
                new_time = f"{hour_format}:{minute_format} PM, {day}"
            else:
                new_time = f"{hour_format}:{minute_format} AM, {day}"

    return new_time