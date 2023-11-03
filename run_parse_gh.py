import pandas
import os
import re
import glob
import requests
import json 
import time

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


another_dataset = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):
	f = open(json_file_name,"r")
	json_data = json.load(f)
	f.close()

	login = json_data['login']
	print(login)
	avatar_url = json_data['avatar_url']
	url = json_data['url']
	following = json_data['following']
	num_starred = json_data['starred_url']
	name = json_data['name']
	company = json_data['company']
	blog = json_data['blog']
	location = json_data['location']
	email = json_data['email']
	hireable = json_data['hireable']
	created_time = json_data['created_at']
	updated_time = json_data['updated_at']

	if created_time != None:
		created_time = created_time.split("T")[1]
		created_time = created_time.replace("Z","")
		print(created_time)
	else:
		print("null created time")
	if updated_time != None:
		updated_time = updated_time.split("T")[1].replace("Z","")
		print(updated_time)
	else:
		print("null updated time")

	# to retrieve the number starred
	access_point = num_starred.replace("{/owner}{/repo}","")

	f = open("token","r")
	token = f.read()
	f.close()

	github_session = requests.Session()
	github_session.auth = ("claracullum",token)

	num_starred = github_session.get(access_point)
	num_starred = num_starred.text.count("hooks_url")
	print(num_starred)

	time.sleep(5)

	#to make the csv
	row = pandas.DataFrame.from_records([{
			'avatar_url': avatar_url,
			'url': url,
			'following': following,
			'starred': num_starred,
			'name': name,
			'company': company,
			'blog': blog,
			'location': location,
			'email': email,
			'hireable': hireable,
			'created_time': created_time,
			'updated_time': updated_time
		}])

	another_dataset = pandas.concat([another_dataset,row])

another_dataset.to_csv("parsed_files/gh_user_data.csv", index=False)



