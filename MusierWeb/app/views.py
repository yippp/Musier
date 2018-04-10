from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	return render(request, 'app/index.html', {})

def notionLoad(request):
	if request.method == "GET":
		return render(request, 'app/notionLoad.html', {})
	elif request.method == "POST":
		print(request.POST.get("Meter"))
		testmessege = request.POST.get("Meter")
		return render(request, 'app/notionLoad.html', {"testmessege":testmessege})
	else:
		return redirect("/app/notionLoad")