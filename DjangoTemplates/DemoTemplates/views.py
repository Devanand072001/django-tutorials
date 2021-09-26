from django.shortcuts import render
import datetime as time

def display(request):
    date = time.datetime.now()
    message = "Hi, Good "
    hour = int(date.strftime('%H'))
    if hour < 12 :
        message = message + "morning"
    elif hour > 12 and hour < 18:
        message = message + "afternoon"
    else :
        message = message + "evening"
    date_dict = {'display_date' : date, "name" : "Devanad V", "greetings": message }
    print(date_dict)
    print(date_dict['display_date'])
    return render(request,'index.html', context = date_dict)
# Create your views here.
