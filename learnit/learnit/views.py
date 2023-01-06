# iihave created this file -- jayvanjare
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html',)

    
def about(request):
    return HttpResponse('About')

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremove=request.GET.get('newlineremove','off')
    extraspaceremove=request.GET.get('extraspaceremove','off')



    #analyze the text
    
    if removepunc=="on":
    # analyzed=djtext
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for  char in djtext:
            if char not in punctuation:
                analyzed=analyzed + char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()

        params={'purpose':'UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 

    elif newlineremove=='on':
        analyzed="" 
        for char in djtext:
            if char != "\n" :
                analyzed=analyzed+ char
                


        params={'purpose':'New Line Remove','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 

    elif extraspaceremove=='on':
        analyzed="" 
        for index,char in enumerate(djtext):
            if not(djtext[index] ==" " and  djtext[index+1] == " ") :
                analyzed=analyzed+ char
                
            
                


        params={'purpose':'Extra Space Remove','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    
    
    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("Cap First")

# def newlineremove(request):
#     return HttpResponse("<b>New Line Remove")

# def charcount(request):
#     return HttpResponse("Char count")

# def spaceremove(request):
#     return HttpResponse('<h1>Space remove</h1>')