from django.shortcuts import render
from models import TagCloud
from django.http import HttpResponse
import scraper
# Create your views here.

def getIndex(request):
    index = request.GET["index"]
    wordCount = scraper.run(index)

    result = ""
    for (word, count) in wordCount:
        result = result + word+","
        result = result + str(count)+";"
        newRecord = TagCloud(Index=index, Tag=word, Count=count)
        newRecord.save()

    return HttpResponse(result)


