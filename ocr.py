from PIL import Image
from pytesseract import image_to_string
import os
import json
#import pytesseract
im = Image.open(r'C:\Python27\Screenshots\Screenshot(1).png')
print(im)

print(image_to_string(im))
'''



f_out = open("movies.json","w")

# print (image_to_string(Image.open('Screenshot (2).png')))
for file in (os.listdir("Screenshots/")):
	title = ""
	release = ""
	score = ""
	voters = ""
	img = Image.open("Screenshots/"+file)
	# text = image_to_string(img).split("\n")
	# print (text)
	name_img = img.crop((271,545,1492,770))
	title = image_to_string(name_img).split("\n")
	
	if ')' in title[0]:
		title = title[0][:-6].strip()
	else:
		title = title[0].strip() + " " + title[1][:-6].strip()
	print (title)
	# release_img = img.crop((266,706,1428,862))
	release_date = image_to_string(img).split("\n")
	month = {"January":'01', "February" :'02', "March":'03', "April":'04', "May":'05', "June":'06', "July":'07', "August":'08', "September":'09',  "October":'10',  "November":'11',  "December":'12'}
	day = {"1":"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
	for line in release_date:
		if title=="A Trip to Mars":
			release = "19180222"
			break
		if '(USA)' in line:
			try:
				items = line.split()
				release = items[-2]+month[items[-3]]+day.get(items[-4],items[-4])
				print(release)
			except:
				pass
			# print(items[-4],items[-3],items[-2])


	# print (release_date)
	rating = img.crop((1600,548,1800,609))
	score = float(image_to_string(rating))
	no_of_votes = img.crop((1600,615,1800,645))
	voters = int(image_to_string(no_of_votes).replace(",",''))
	print (score, voters)
	if title!= "" and release!="":
		js = {"movie_title":title,"release_date":release,"movie_rating":score,"no_of_votes":voters}
		f_out.write(json.dumps(js)+"\n")
	# for i in range (len(text)):
	# 	if text[i].strip() != '' and text[i].strip()[0] == "+":
	# 		title = text[i].replace('+','').strip()
	# 		while ")" not in title:
	# 			i+=1
	# 			title += text[i]
	# 		title.strip()[:-6].strip()
	# 		print (title)
'''
