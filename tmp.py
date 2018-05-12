'''str_message = str(message)
			if str_message is None or str_message == '':
				continue;
    		if j % 3 == 0:
    			tuplu = tuple([first, second])
    			#print(tuplu)
    			#if dic[tuplu] is None: 
    				#dic[tuplu] = [track]
    			#else:
    			if tuplu is None and tuplu in dic:
    				dic[tuplu] = dic[tuplu].append(str_message)
    			else:
    				dic[tuplu] = [str_message]
    		else:
    			if j % 2 == 0:
    				first = str_message
    			else:
    				second = str_message
    		j += 1'''