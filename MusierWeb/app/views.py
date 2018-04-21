from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR+"/app/")
sys.path.append(BASE_DIR+"/app/Capriccia/")
from Capriccia.GAMain import *


def index(request):
	return render(request, 'app/index.html', {})

def notionLoad(request):
	#GET request
	if request.method == "GET":
		print(sys.path)
		return render(request, 'app/notionLoad.html', {})
	#POST request
	elif request.method == "POST":
		Dict = ["C,","^C,", "D,","^D,", "E,", "F,","^F,", "G,","^G,", "A,","^A,", "B,",\
				"C" ,"^C" , "D" ,"^D" , "E" , "F" ,"^F" , "G" ,"^G" , "A" ,"^A" , "B" ,\
				"c" ,"^c" , "d" ,"^d" , "e" , "f" ,"^f" , "g" ,"^g" , "a" ,"^a" , "b" ,\
				"c'","^c'", "d'","^d'", "e'", "f'","^F'", "g'","^g'", "a'","^a'", "b'"
		]
		Meter = request.POST.get("Meter")
		Tonality = request.POST.get("Tonality")
		notions = request.POST.get("notions")
		Seq = main_version_2(Tonality, Meter, notions).get_notes()
		#Seq=[9, None, 2, 6, 2, None, -3, None, 0, None, 5, None, 12, None, 5, None, 9, 13, 9, None, 2, 0, None, 5, 9, None, 4, 2, 0, None, -3, None, 0, None, 5, 2, 5, None, 12, 9, 4, 6, None, 11, 9, None, 4, None, 9, None, 4, None, -3, 1, None, 6, -7, -3, None, None, None, None, None, None]
		count = 1
		note_count = 0
		priod_count = -1
		long_note = False
		generated_notions = '''X: 1
M: 4/4
L: 1/8
K: C
Q: 1/4=150
%%MIDI program 11
'''
		for i in range(len(Seq)):

			if (Seq[i] == None):
				count += 1
				long_note = True
			else:			
				if long_note is True:
					generated_notions += str(count)
					count = 1
					long_note = False
				if ((note_count) % 8) == 0:
					priod_count += 1
					generated_notions += "|"
					if ((priod_count % 4) == 0) and (priod_count != 0):
						generated_notions += "\n"
				generated_notions += Dict[12 + Seq[i]]
			note_count += 1
		if Seq[-1] == None:
			generated_notions += str(count)
		return HttpResponse(json.dumps({"generated_notions":generated_notions}), content_type="application/json")

	else:
		return redirect("/app/notionLoad")
