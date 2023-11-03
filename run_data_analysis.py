import pandas
import matplotlib.pyplot as plt

data_initial = pandas.read_csv("html_files/data_initial.csv")
data_initial_frame = pandas.DataFrame(data_initial)
data_clean = pandas.read_csv("html_files/data_clean.csv")
gh_user_data = pandas.read_csv("parsed_files/gh_user_data.csv")
gh_user_data = pandas.DataFrame(gh_user_data)

# SUMMARY STATISTICS
print("1. Initial Data")
print("This data includes all users (minus duplicates) listed on the charcoalpaper webpage along with their repo count, followers, and date created.")
print("Summary Statistics:")
di = data_initial.describe(include='all')
print(di)

print("2. Cleaned Data")
print("This data includes only the valid user IDs from the charcoalpaper site.")
print("Summary Statistics:")
dc = data_clean.describe(include='all')
print(dc)

print("3. Github Info Data")
print("This contains all information scraped from Github on the valid users.")
print("Summary Statistics:")
#No Summary Stats (qualitative): avatar_url,url,name,blog,location,company,email,hireable,
#Summary Stats: following,starred,created_time,updated_time
following = gh_user_data['following']
print("Following:")
print(following.describe())
starred = gh_user_data['starred']
print("Starred:")
print(starred.describe())
created_time = gh_user_data['created_time']
print("Created Time:")
print(created_time.describe())
updated_time = gh_user_data['updated_time']
print("Updated Time:")
print(updated_time.describe())

# Other Relavant Info 
unique_ids_count = len(data_initial['Login ID'])
print("Unique IDs:")
print(unique_ids_count)
invalid_ids_count = unique_ids_count - len(data_clean['Login ID'])
print("Invalid IDs:")
print(invalid_ids_count)

# Scatterplots
repo_count = data_initial['Repo Count']
follower_count = data_initial['Follower Count']
data_initial_frame.plot(kind='scatter',x='Repo Count',y='Follower Count')

plt.xlabel('# of Repositories')
plt.ylabel('# of Followers')
plt.title('Followers and Repositories')

plt.savefig('parsed_files/Repo_Followers.png')

#another
updated_time = gh_user_data['updated_time']
created_time = gh_user_data['created_time']
gh_user_data.plot(kind='scatter',x='updated_time',y='created_time')

plt.xlabel('Last time updated')
plt.ylabel('Created')
plt.title('Created VS Updated')

plt.savefig('parsed_files/Created.png')


