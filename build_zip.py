import shutil
import os
import glob
import re
import subprocess

try:
	shutil.rmtree("./thisismattmiller/")
	os.remove("./thisismattmiller.zip")
except:
	pass

os.makedirs('./thisismattmiller/', exist_ok=True)


shutil.copytree('./about/', './thisismattmiller/about', dirs_exist_ok=True)  # Fine
shutil.copytree('./categories/', './thisismattmiller/categories', dirs_exist_ok=True)  # Fine
shutil.copytree('./css/', './thisismattmiller/css', dirs_exist_ok=True)  # Fine
shutil.copytree('./img/', './thisismattmiller/img', dirs_exist_ok=True)  # Fine
shutil.copytree('./js/', './thisismattmiller/js', dirs_exist_ok=True)  # Fine
shutil.copytree('./post/', './thisismattmiller/post', dirs_exist_ok=True)  # Fine
shutil.copytree('./series/', './thisismattmiller/series', dirs_exist_ok=True)  # Fine
shutil.copytree('./tags/', './thisismattmiller/tags', dirs_exist_ok=True)  # Fine

os.remove("./thisismattmiller/img/post_lin.webm")


shutil.copy('./index.html', './thisismattmiller/index.html')

todo = list(glob.glob('./thisismattmiller/post/*.html')) + list(glob.glob('./thisismattmiller/post/*/*.html'))
todo.append('./thisismattmiller/about/index.html')
todo.append('./thisismattmiller/categories/index.html')
todo.append('./thisismattmiller/series/index.html')
todo.append('./thisismattmiller/tags/index.html')
todo.append('./thisismattmiller/index.html')

for file in todo:
	newfiletext = ''
	with open(file) as filepointer:
		print(file.count('/'),file)
		for line in filepointer:

			if (file.count('/')) == 4:
				line = re.sub(r'https://thisismattmiller.com/post/(.*?)/',r'\.\./post/\1/index.html',line)
				line = line.replace('https://thisismattmiller.com/css/','../../css/')
				line = line.replace('<a href="/about"','<a href="../../about/index.html"')
				line = line.replace('<a href="/"','<a href="../../index.html"')
				line = line.replace('src="/img/','src="../../img/')




			if (file.count('/')) == 3:
				line = re.sub(r'https://thisismattmiller.com/post/(.*?)/',r'\.\./post/\1/index.html',line)
				line = line.replace('https://thisismattmiller.com/css/','../css/')
				line = line.replace('<a href="/about"','<a href="../about/index.html"')
				line = line.replace('<a href="/"','<a href="../index.html"')
				line = line.replace('src="/img/','src="../img/')

			if (file.count('/')) == 2:
				line = re.sub(r'https://thisismattmiller.com/post/(.*?)/',r'./post/\1/index.html',line)
				line = line.replace('https://thisismattmiller.com/css/','./css/')
				line = line.replace('href="about/"','href="./about/index.html"')



			newfiletext = newfiletext + line
	with open(file,'w') as outfile:
		outfile.write(newfiletext)



cmd_str = "zip -9 -r thisismattmiller.zip ./thisismattmiller/"
subprocess.run(cmd_str, shell=True)


shutil.rmtree("./thisismattmiller/")

# for line in index:

# 	
