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
Seq = [[],[]]

def index(request):
	return render(request, 'app/index.html', {})

def notionLoad(request):
	#GET request
	if request.method == "GET":
		return render(request, 'app/notionLoad.html', {})
	#POST request
	elif request.method == "POST":
		Dict = ["C,,","^C,,", "D,,","^D,,", "E,,", "F,,","^F,,", "G,,","^G,,", "A,,","^A,,", "B,,",\
				"C,","^C,", "D,","^D,", "E,", "F,","^F,", "G,","^G,", "A,","^A,", "B,",\
				"C" ,"^C" , "D" ,"^D" , "E" , "F" ,"^F" , "G" ,"^G" , "A" ,"^A" , "B" ,\
				"c" ,"^c" , "d" ,"^d" , "e" , "f" ,"^f" , "g" ,"^g" , "a" ,"^a" , "b" ,\
				"c'","^c'", "d'","^d'", "e'", "f'","^F'", "g'","^g'", "a'","^a'", "b'"
		]
		Meter = request.POST.get("Meter")
		Meter = int(Meter) + 2 # 3 for 3/4; 4 for 4/4
		Major = int(request.POST.get("Major"))
		notions = request.POST.get("notions")
		Title = request.POST.get("Title")
		notion = []
		num = 0
		bgn = 1
		numDict=["1","^1","2","^2","3","4","^4","5","^5","6","^6","7"]
		for note in notions:
			if note.isdigit():
				if bgn:
					num = numDict.index(note)
					bgn = 0
				else:
					notion.append(num)
					num = numDict.index(note)
			elif note == "'":
				num+=12;
			elif note == ",":
				num-=12;
			elif note == "+":
				notion.append(None)
		Seq = main_version_2(Meter, Major)
		Seq_main = Seq[0].get_notes()
		Seq_chord = Seq[1].get_notes()
		# Seq_chord = []
		# Seq_main=[9, None, 2, 6, 2, None, -3, None, 0, None, 5, None, 12, None, 5, None, 9, 13, 9, None, 2, 0, None, 5, 9, None, 4, 2, 0, None, -3, None, 0, None, 5, 2, 5, None, 12, 9, 4, 6, None, 11, 9, None, 4, None, 9, None, 4, None, -3, 1, None, 6, -7, -3, None, None, None, None, None, None]
		# for note in Seq_main:
		#     if isinstance(note,type(1)):
		#         Seq_chord.append(note-16)
		#     else:
		#         Seq_chord.append(None)
		count = 1
		note_count = 0
		priod_count = -1
		long_note = False
		generated_notions = '''
M: %d/4
L: 1/8
Q: 1/4=150
'''%Meter
		generated_notions = "X:1\nT:"+Title + generated_notions
		##major track
		generated_notions += '''V:1
K:C
%%MIDI program 25
'''
		for i in range(len(Seq_main)):
			if (Seq_main[i] == None):
				count += 1
				long_note = True
			else:			
				if long_note is True:
					generated_notions += str(count)
					count = 1
					long_note = False
				if ((note_count) % (Meter * 2)) == 0:
					priod_count += 1
					generated_notions += "|"
					if ((priod_count % 4) == 0) and (priod_count != 0):
						generated_notions += "\n"
				generated_notions += Dict[24 + Seq_main[i]]
			note_count += 1
		if Seq_main[-1] == None:
			generated_notions += str(count)
		##minor track
		count = 1
		note_count = 0
		priod_count = -1
		long_note = False
		generated_notions += '''
V:2
K:bass
%%MIDI program 24
'''
		for i in range(len(Seq_chord)):
			if (Seq_chord[i] == None):
				count += 1
				long_note = True
			else:			
				if long_note is True:
					generated_notions += str(count)
					count = 1
					long_note = False
				if ((note_count) % (Meter * 2)) == 0:
					priod_count += 1
					generated_notions += "|"
					if ((priod_count % 4) == 0) and (priod_count != 0):
						generated_notions += "\n"
				generated_notions += Dict[24 + Seq_chord[i]]
			note_count += 1
		if Seq_chord[-1] == None:
			generated_notions += str(count)
		return HttpResponse(json.dumps({"generated_notions":generated_notions}), content_type="application/json")

	else:
		return redirect("/app/notionLoad")

def regenerate(request):
	if request.method == 'POST':
		return HttpResponse(json.dumps({"regenerated_notions":regenerated_notions}), content_type="application/json")
















