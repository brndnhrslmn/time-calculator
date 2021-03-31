def add_time(start, duration, day=None):

    # split the start time into time and AM or PM
    startTime, period = start.split()
    # split the start time into hours and minutes
    startHours, startMinutes = startTime.split(':')

    # split the duration into hours and minutes
    durationHours, durationMinutes = duration.split(':')

    # totalise hours and minutes
    totalHours = int(startHours) + int(durationHours)
    totalMinutes = int(startMinutes) + int(durationMinutes)

    # initialise required variables
    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    totalDays = int(totalHours / 24)
    increment = False

    # check the current number of days based on total hours
    if totalDays < 1:
        totalDays = 0
    if totalDays > 1:
        totalDays = totalDays

    # check for an hour changeover, hour-multiples and then for a 12-hour changeover
    if totalMinutes > 59:
        increment = True
        totalHours += 1
        totalMinutes %= 60
    if totalHours > 11:
        totalHours %= 12
        if int(durationHours) != 24 or increment == True:
            if period == 'AM':
                period = 'PM'
                totalDays = totalDays
            else:
                period = 'AM'
                totalDays += 1
        if totalHours == 0:
            totalHours = 12

    # create the initial string output
    new_time = f"{totalHours}:{str(totalMinutes).zfill(2)} {period}"

    # when a day is entered as an optional parameter, add to string and index based on elapsed time
    if day:
        currentIndex = week.index(day.title())
        futureIndex = int((currentIndex + totalDays) % 7)
        new_time += f", {week[futureIndex]}"
    if totalDays == 1:
        new_time += " (next day)"
    if totalDays > 1:
        new_time += f" ({int(totalDays)} days later)"

    return new_time
