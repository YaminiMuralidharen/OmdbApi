import json
import pdb
import sys, urllib
import urllib.request, urllib.parse, urllib.error
from argparse import ArgumentParser  
parser = ArgumentParser()
parser.add_argument("--movie", help="Type movie name after parameter -m", required=True)
#parser.print_help()
args = parser.parse_args()
title= args.movie

baseurl = 'http://www.omdbapi.com/?'
apikey='YOURAPIKEY'
omdbapikey='&apikey='+ apikey
#title ='Guardians of the Galaxy Vol. 2'
foundRatingvalue = False
try:
	url = baseurl + urllib.parse.urlencode({'t': title })+omdbapikey
	res = urllib.request.urlopen(url)
	data = res.read()
	json_data=json.loads(data)
	if json_data['Response']=='True':
		ratingsobj = json_data['Ratings']
		if ratingsobj is not None:
			for source in ratingsobj:
				if(source['Source']=='Rotten Tomatoes'):
					foundRatingvalue=True
					print('Rotten tomato value for the movie ', source['Value'])	
					break
		if(foundRatingvalue==False):
			print("Rotten tomato value for the movie is not found")
	else:
		print("Movie name is invalid")

except urllib.error.URLError as e:
	print("ERROR: {e.reason}")
