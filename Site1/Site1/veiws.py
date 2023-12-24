#i created
from django.http import HttpResponse
from django.shortcuts import render


#earlier code
#def index(request):
    #return HttpResponse("Home")

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #gettext
    djtext = request.GET.get('text', 'default')
    # check checkbox values
    removepuc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    charcount = request.GET.get('charcount', 'off')

    #check which check box is on
    if (removepuc == "on") :
    #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext :
            if char!="/n":
                analyzed = analyzed + char
        params = {'purpose':'new line removed','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if (charcount == "on"):
        count = 0
        for char in djtext:
            if char != " ":
                count = count + 1
        params = {'purpose':'charchounter is','analyzed_text': count}
        #return render(request,'analyze.html',params)

    if(charcount != "on" and newlineremove != "on" and fullcaps != "on" and removepuc != "on"):
        return HttpResponse("error")



    return render(request, 'analyze.html', params)



#def capfirst(request):
    #return HttpResponse("Capfirst")

#def about (request):
    #return HttpResponse("hello about")

#def newlineremove (request):
    #return HttpResponse ("newlineremove")

#def spaceremove (request) :
    #return HttpResponse ("space remover <a href='/'> back</a>")
#def charcount (request):
    #return HttpResponse("charcount ")

#EX1
#def nav(request):
    #return HttpResponse('''<a href="https://www.youtube.com"> Youtube </a> <br> <a href="https://www.instagram.com/direct/inbox/">instagram</a>''')