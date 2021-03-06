
from mido import MidiFile, MidiTrack, Message
import os
import numpy
import random

dic = {}
j = 1
avg = 0
n = 0
for file in os.listdir("midi"):
	
	if file.endswith(".mid"):
		count = 0
		file = os.path.join("midi", file)
		mid = MidiFile(file)
		for i, track in enumerate(mid.tracks):
			lst = []
			for message in track :
				lst.append(str(message))
				count += 1
			dic[str(j)] = lst
			j += 1
		avg += count
		n += 1

avg = avg / n
songs_notes_map = {}
songs_times_map = {}
songs_velocities_map = {}

for i in range(1, j):
	lst = dic[str(i)]
	note_count = 1
	for msg in lst:
		#print(msg)
		if msg.startswith("<") or msg.endswith(">"):
			continue
		split = msg.split(" ")
		#print(split)
		for s in split:
			if "note=" in s:
				
				note = s.split("=")[1]
				#print(note)
				if note_count % 3 == 0:
					key = str(first_note) + " " + str(second_note);
					#print(key)
					songs_notes_map.setdefault(key, []).append(note)
				else:
					if note_count % 2 == 0:
						second_note = note
					else:
						first_note = note
				note_count += 1
				continue
			if "time=" in s and ">" not in s:
				
				time = s.split("=")[1]

				#print(note)
				if note_count % 3 == 0:
					if first_note is None or second_note is None:
						continue
					key = str(first_note) + " " + str(second_note);
					#print(key)
					songs_times_map.setdefault(key, []).append(time)
				continue
			if "velocity=" in s:
				
				vel = s.split("=")[1]

				#print(note)
				if note_count % 3 == 0:
					if first_note is None or second_note is None:
						continue
					key = str(first_note) + " " + str(second_note);
					#print(key)
					songs_velocities_map.setdefault(key, []).append(vel)
'''
print(songs_notes_map)
print("...............")
print("\n")
print(songs_times_map)
print("...............")
print("\n")
print(songs_velocities_map)'''


count = 0
if random.random() < 0.5:
	sign = 1
else:
	sign = -1

notes_no = avg + random.random() * 0.3 * sign * avg / 500
print(avg)
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
track.append(Message('program_change', program=4, time=0))

for k, v in songs_notes_map.items():
	if count > notes_no:
		break;
	split = k.split(" ")
	n1 = split[0]
	n2 = split[1]
	i = random.randint(0, len(v)-1)
	n3 = v[i]

	keys1 = list(songs_times_map.keys())

	#while (k not in songs_times_map):
	#	k = random.randint(0, len(keys))

	#ra1 = random.randint(0, len(songs_times_map[k]))
	#while (ra1 not in songs_times_map[k]):
		#ra1 = random.randint(0, len(songs_times_map[k]))
	krand = random.choice(keys1)
	t1 = random.choice(songs_times_map[krand])

	#ra1 = random.randint(0, len(songs_times_map[k]))
	#while (ra1 not in songs_times_map[k]):
	#	ra1 = random.randint(0, len(songs_times_map[k]))
	krand = random.choice(keys1)
	t2 = random.choice(songs_times_map[krand])

	#ra1 = random.randint(0, len(songs_times_map[k]))
	#while (ra1 not in songs_times_map[k]):
	#	ra1 = random.randint(0, len(songs_times_map[k]))
	krand = random.choice(keys1)
	t3 = random.choice(songs_times_map[krand])

	keys1 = list(songs_velocities_map.keys())
	kvel = random.choice(keys1)
	#print(songs_velocities_map[kvel])
	ch = random.randint(0, 1)
	m1 = Message('note_on' ,channel=ch,  note=int(n1), velocity=int(songs_velocities_map[kvel][0]), time=int(t1) * 2)
	kvel = random.choice(keys1)
	ch = random.randint(0, 1)
	m2 = Message('note_on' ,channel=ch,  note=int(n2), velocity=int(songs_velocities_map[kvel][0]), time=int(t2) * 2)
	if int(n3) % 2 == 0:
		ch = 1
	else:
		ch = 0
	kvel = random.choice(keys1)
	m3 = Message('note_on' ,channel=ch,  note=int(n3), velocity=int(songs_velocities_map[kvel][0]), time=int(t3) * 2)
	count += 3
	track.append(m1)
	track.append(m2)
	track.append(m3)

mid.save('output/new_song5.mid')