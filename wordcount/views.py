# to send response to the webpage(HttpResponse)
from django.http import HttpResponse

#We need to tell Django, where to look for templates (entry in settings.py)
# to render the html file
from django.shortcuts import render

import operator

# #Request is that we got from the urls.py
# def home(request):
#     return HttpResponse('Hello to Django')

#Request is that we got from the urls.py
def home(request):
    # Using render for home.html (request,html file,what other information you want to send in dictionary form)
    return render(request, 'home.html', {'hey': 'Let\'s count the WORDS'})
    # Passing dictionary as another parameter and in html just call the key name


def count(request):
    # Getting the value from the name of the parameter
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    #Which word appeared the most?
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            # if word there in dictionary, increment by 1
            worddictionary[word] += 1
        else:
            # add to the dictionary
            # if word is not there in dictionary, set value to 1
            worddictionary[word] = 1

    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(
        1), reverse=True)  # sorting the dictionary based on the count of words

    #Returning html file with 'youtext','length','sortedlist' keys to pass the value to the html file
    return render(request, 'count.html', {'yourtext': fulltext, 'length': len(wordlist), 'sortedlist': sortedlist})


def aboutus(request):
    return render(request, 'aboutus.html')
