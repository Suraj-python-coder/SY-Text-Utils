# I have created this file :- Suraj
from django.http import HttpResponse
from django.shortcuts import render

# templates:
def index(request):
    return render(request,'index.html') 

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox values
    removepunc=request.POST.get('removepunc',"off")
    fullcaps=request.POST.get('fullcaps',"off")
    newlineremover=request.POST.get('newlineremover',"off")
    extraspaceremover=request.POST.get('extraspaceremover',"off")
    charcounter=request.POST.get('charcounter',"off")

    # check which chechbox is on
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
       
    if( charcounter=="on"):
        analyzed = 0
        for char in djtext:
            analyzed= analyzed+1          
        params = {'purpose': 'Charecter Counter', 'analyzed_text': analyzed}
  
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcounter!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
