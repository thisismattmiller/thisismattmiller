import toml
import requests
import json

## req the google sheet as json
resp = requests.get('https://spreadsheets.google.com/feeds/cells/1YVJq-BC2ZLx2Q74PNs2Ct3BAh7tjNY7ZgNBed2_RVDA/1/public/full?alt=json')
sheet = resp.json()

lookup = {}
row = 0

# build a lookup buy cell Id
for e in sheet['feed']['entry']:
	lookup[e['title']['$t']] = e['content']['$t']
	if int(e['gs$cell']["row"])>row:
		row=int(e['gs$cell']["row"])


cat_lookup = {}

for x in range(1,row+1):

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
