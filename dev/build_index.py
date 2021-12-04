import toml
import requests
import json
import sys
import re
## req the google sheet as json
# resp = requests.get('https://spreadsheets.google.com/feeds/cells/1YVJq-BC2ZLx2Q74PNs2Ct3BAh7tjNY7ZgNBed2_RVDA/1/public/full?alt=json')
resp = requests.get('https://docs.google.com/spreadsheets/d/1YVJq-BC2ZLx2Q74PNs2Ct3BAh7tjNY7ZgNBed2_RVDA/gviz/tq?tqx=out:json&tq&gid=0')

jsonString = re.search(r'(?<="table":).*(?=}\);)',resp.text).group(0)

sheet = json.loads(jsonString)



lookup = {}
row = 0

# build a lookup buy cell Id
for rows in sheet['rows']:

	# dunno what this c key is but its there
	rows = rows['c']

	# lookup[e['title']['$t']] = e['content']['$t']
	for idx, col in enumerate(sheet['cols']):
		

		
		if rows[idx] == None:
			# lookup[col['id']+str(row)] = None
			# if its empty dont add to the lookup
			pass
		elif 'f' in rows[idx]:
			if rows[idx]['f'] != None:
				lookup[col['id']+str(row)] = rows[idx]['f']
		elif 'v' in rows[idx]:
			if rows[idx]['v'] != None:
				lookup[col['id']+str(row)] = rows[idx]['v']

		else:
			print("unkown data type here", rows[idx], 'in row', row)

	row=row+1


cat_lookup = {}


try:

	for x in range(0,row):


		cat = lookup['A'+str(x)]
		cat_clean = cat.lower().replace(' ','').replace('/','').replace('*','')

		if cat_clean not in cat_lookup:
			cat_lookup[cat_clean] = {}
			cat_lookup[cat_clean][cat_clean] = {
				"label": cat,
				"desc" : cat,
				"things":[]
			}

		

		title = lookup['B'+str(x)]
		date = lookup['C'+str(x)]
		desc = 	lookup['D'+str(x)]
		links = []
		links.append({
				"label" :lookup['E'+str(x)].split('|')[0],
				"url" :lookup['E'+str(x)].split('|')[1]
			})

		
		if 'F'+str(x) in lookup:

			links.append({
				"label" :lookup['F'+str(x)].split('|')[0],
				"url" :lookup['F'+str(x)].split('|')[1]
			})	


		if 'G'+str(x) in lookup:
			links.append({
				"label" :lookup['G'+str(x)].split('|')[0],
				"url" :lookup['G'+str(x)].split('|')[1]
			})	


		if 'H'+str(x) in lookup:
			links.append({
				"label" :lookup['H'+str(x)].split('|')[0],
				"url" :lookup['H'+str(x)].split('|')[1]
			})	
		print('row',str(x))
		if 'I'+str(x) in lookup:
			links.append({
				"label" :lookup['I'+str(x)].split('|')[0],
				"url" :lookup['I'+str(x)].split('|')[1]
			})	
		if 'J'+str(x) in lookup:
			links.append({
				"label" :lookup['J'+str(x)].split('|')[0],
				"url" :lookup['J'+str(x)].split('|')[1]
			})	


		cat_lookup[cat_clean][cat_clean]['things'].append(
				{	
					"label":title,
					"desc":desc,
					"date":date,
					"links":links
				})
except:


	print("-----------------")
	print("Spreadsheet formating error!")
	print("-----------------")
	sys.exit()





output  = ""
for key in cat_lookup:
	output = output + toml.dumps({"params": {"mystuff": cat_lookup[key]}}) + "\n\n\n"


# read in existing file
new_file = ""
with open('config.toml') as infile:
	for line in infile:

		if '# HOMEPAGE ITEMS' in line:
			new_file = new_file + '# HOMEPAGE ITEMS \n\n'
			new_file = new_file + output
			break
		else:
			new_file = new_file + line

with open('config.toml','w') as out:
	out.write(new_file)
