# to send response by just typing here in python file(HttpResponse)
from django.http import HttpResponse

from django.shortcuts import render  # to render the html file

import operator

# #Request is that we got from the urls.py
# def home(request):
#     return HttpResponse('Hello to Django')


def home(request):
    # Using render
    return render(request, 'home.html', {'hey': 'Let\'s count the WORDS'})
    # Passing dictionary as another parameter and in html just call the key name


def count(request):
    # Getting the value from the name of the parameter
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

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
        1), reverse=True)  # sorting the dictionary

    return render(request, 'count.html', {'yourtext': fulltext, 'length': len(wordlist), 'sortedlist': sortedlist})


def aboutus(request):
    return render(request, 'aboutus.html')
