import pandas
import os
import re
import glob 
from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()

#for file_name in glob.glob("html_files/*.html"):
f = open(file_name, "r")
soup = BeautifulSoup(file.read(),'html.parser')
f.close()

# body = soup.find("span", {"id":"wrapper"})

big_list = soup.find_all("div", {"class":"grid grid-cols-4 gap-4"})

userid_list = []
repo_list = []
followers_list = []
membersince_list = []

for div in big_list:
	userid = big_list.find("div", {"class": "userid"})
	userid_list.append(userid[0].text)
	repo = big_list.find("div", {"class": "repocount"})
	repo_list.append(repo[0].text)
	followercount = big_list.find("div", {"class": "followercount"})
	followers_list.append(repo[0].text)
	membersince = big_list.find("div", {"class": "membersince"})
	membersince_list.append(repo[0].text)

pandas.concat([dataset,
	pandas.DataFrame.from_records([{
		"userid_list":userid_list,
		"repo_list":repo_list,
		"followers_list":followers_list,
		"membersince_list":membersince_list
		}])
	])
	
dataset = pandas.concat([dataset,row])

dataset.to_csv("html_files/dataset1.csv", index=False)
