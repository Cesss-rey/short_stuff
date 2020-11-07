
entries = int(input())
phone_directory = {}

for x in range(0,entries):
    inp = input()
    entry = inp.split()
    phone_directory[entry[0]] = entry[1]
    
while True:
    try:
    	query = input()
    except:
    	break
    number = phone_directory.get(query)
    if number != None:
    	print(query + "=" + number)
    else:
    	print("Not Found")