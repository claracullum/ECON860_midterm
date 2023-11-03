import pandas
import os
import re
import glob
import numpy
from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

dataset = pandas.DataFrame()

for file_name in glob.glob("html_files/*.html"):
    f = open(file_name, "r")
    soup = BeautifulSoup(f.read(), 'html.parser')
    f.close()

    big_list = soup.find_all("div", {"class": "grid grid-cols-4 gap-4"})

    userid_list = []
    repo_list = []
    repo_num_list = []
    followers_list = []
    membersince_list = []

    for div in big_list:
        userid = div.find("div", {"class": "userid"}).find("span")
        userid_list.append(userid.text.strip())
        repo = div.find("div", {"class": "repocount"}).text.strip()
        repo_list.append(repo)
        followercount = div.find("div", {"class": "followercount"})
        followers_list.append(followercount.text.strip().replace("*  ",""))
        membersince = div.find("div", {"class": "membersince"})
        membersince_list.append(membersince.text.strip())

    data = {
        'Login ID': userid_list,
        'Repo Count': repo_list, 
        'Follower Count': followers_list,
        'Member Since': membersince_list
    }

    dataset = pandas.DataFrame(data)

# dataset.to_csv("html_files/dataset.csv", index=False)

# data_clean = pandas.read_csv("html_files/dataset.csv")
data_initial = dataset.drop_duplicates()
data_initial.to_csv("html_files/data_initial.csv", index=False)




