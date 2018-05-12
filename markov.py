
from mido import MidiFile
import os

dic = {}
j = 1
for file in os.listdir("midi"):
    if file.endswith(".mid"):
    	file = os.path.join("midi", file)
    	mid = MidiFile(file)
    	for i, track in enumerate(mid.tracks):
    		lst = []
    		for message in track :
    			lst.append(str(message))
    		dic[str(j)] = lst
    		j += 1

songs_notes_map = {}

for i in range(1, j):
	lst = dic[str(i)]
	count = 1
	for msg in lst:
		
		split = msg.split(" ")
		#print(split)
		for s in split:
			if "note=" in s:
				
				note = s.split("=")[1]
				#print(note)
				if count % 3 == 0:
					key = str(first) + " " + str(second);
					#print(key)
					songs_notes_map.setdefault(key, []).append(note)
				else:
					if count % 2 == 0:
						second = note
					else:
						first = note
		count += 1
print(songs_notes_map)
for k, v in songs_notes_map.items():
	print("....." + k)
	print("[")
	if v is not None:
		for note in v:
			print(note)
	print("]")