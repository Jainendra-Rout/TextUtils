# code created by administrator

from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
  return render(request, 'index.html')


def analyze(request):
  dtext = request.POST.get('text', 'default')
  removepunc = request.POST.get('removepunc', 'off')
  uppercase = request.POST.get('uppercase', 'off')
  newremover = request.POST.get('newremover', 'off')
  charcount = request.POST.get('charcount', 'off')
  spaceremover = request.POST.get('spaceremover', 'off')


  if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
    given_text = ""
    for char in dtext:
      if char not in punctuations:
        given_text = given_text + char

      params = {'purpose':'Remove Punctuations', 'analyzed_text':given_text}
      dtext = given_text

  if(uppercase == "on"):
    analyzed = ""
    for char in dtext:
      analyzed = analyzed + char.upper()

    params = {'purpose':'CAPITALIZE text', 'analyzed_text': analyzed}
    dtext = analyzed


  if(newremover == "on"):
    analyzed = ""
    for char in dtext:
      if char != "\n" and char != "\r":
        analyzed = analyzed + char

    params = {'purpose':'New Line Remover', 'analyzed_text': analyzed}
    dtext = analyzed


  if(charcount == "on"):
    analyzed = 0
    for char in dtext:
      if char == " ":
        analyzed -= 1
      analyzed += 1

    params = {'purpose':'Characters counting', 'analyzed_text': analyzed}
    dtext = analyzed


  if(spaceremover == "on"):
    analyzed = ""
    for char in dtext:
      if char != " ":
        analyzed = analyzed + char

    params = {'purpose':'Space Remover', 'analyzed_text': analyzed}
    dtext = analyzed

  if (removepunc != "on" and uppercase != "on" and newremover != "on" and charcount != "on" and spaceremover != "on"):
    return render (request, 'error.html')

  return render(request, 'analyze.html', params)