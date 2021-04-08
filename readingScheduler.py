import datetime

pages = input("Book pages count: ")
start_page = input("Starting page number: ")
end_page = input("Ending page number: ")
pace = input("Pages to read each day: ")
day = datetime.datetime.now().day
month = datetime.datetime.now().month

def dayscheck (days, months, startpagecount, endpagecount):
        if days <= 9 and months <= 9:
            print(f"{startpagecount} - {endpagecount}, 0{days} / 0{months}")
        elif days <= 9 and months > 9:
            print(f"{startpagecount} - {endpagecount}, 0{days} / {months}")
        elif months <= 9 and days > 9:
            print(f"{startpagecount} - {endpagecount}, {days} / 0{months}")
        else:
           print(f"{startpagecount} - {endpagecount}, {days} / {months}")

def bookr(pages, start_page, end_page, pace, day, month):
    read_days = int(pages / pace)
    startpagecount = start_page
    endpagecount = start_page
    days = 0 + day
    months = 0 + month
    print("****************************\n Here's your monthly reading checklist :D\n****************************")
    for i in range(read_days + pace):
        days += 1
        if endpagecount < end_page:
            endpagecount += pace
        else:
            break
        if (startpagecount == start_page and endpagecount == pace + start_page) or startpagecount == endpagecount:
            startpagecount = start_page
        else:
            startpagecount += pace
        if endpagecount > end_page:
            difference = endpagecount - end_page
            endpagecount -= difference
        if days > 28 or (days > 30 and months in (4, 6, 9, 11)) or (days > 31):
            months += 1
            days = 1
        dayscheck (days, months, startpagecount, endpagecount)

    return "****************************"


print(bookr(int(pages), int(start_page), int(end_page), int(pace), int(day), int(month)))