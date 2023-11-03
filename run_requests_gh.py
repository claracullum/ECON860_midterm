import requests
import json
import os
import pandas
import time

if not os.path.exists("json_files"):
  os.mkdir("json_files")

# data_clean = pandas.DataFrame()
data_clean = pandas.read_csv("html_files/data_initial.csv")

access_point = "https://api.github.com"

f = open("token","r")
token = f.read()
f.close()

id_list = pandas.read_csv("html_files/data_initial.csv")
id_list = id_list['Login ID']

github_session = requests.Session()
github_session.auth = ("claracullum",token)

# checks the rate 
response_text = github_session.get(access_point+"/rate_limit").text
print(json.loads(response_text))

valid_usernames = []
invalid_usernames = []

for user_id in id_list: 
	file_name = "json_files/"+user_id+".json"

	if os.path.exists(file_name):
		print("File exists: ", user_id)
	else: 
		try:
			print(user_id)
			
			response_text = github_session.get(access_point+"/users/"+user_id).text
			json_text = json.loads(response_text)

			if "Not Found" in response_text:
				print(user_id + ": INVALID ID")
				invalid_usernames.append(user_id)
			else:
				f = open(file_name + ".tmp", "w")
				f.write(json.dumps(json_text))
				f.close

				os.rename(file_name+'.tmp',file_name)

				valid_usernames.append(user_id)

		except Exception as e: 
			print(file_name + ": ERROR")
			print(e)
			

		time.sleep(5)

for user_id in invalid_usernames:
		data_clean = data_clean.drop(data_clean[data_clean['Login ID'] == user_id].index)


data_clean.to_csv("html_files/data_clean.csv", index=False)

print(invalid_usernames.len())
print(valid_usernames.len())



