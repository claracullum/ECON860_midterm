# Instructions
### In order of correct performance

1. run_requests.py
>This scrapes the charcoalpaper website and enters its html into a file in the directory
>"html_files" that is dated/timestamped.

2.  run_parse.py
>This outputs a csv called data_initial (in "html_files" directory) that has all of the
>4 columns of data from charcoal paper for each unique user ID (duplicates removed)

3. run_requests_gh.py
>This program has 2 main purposes. First, it scrapes the users' github information and places
>them into json files in the json_file directory. Second, it checks whether or not the user
>is still valid and created a new dataset with only valid IDs called "data_clean" in the
"html_files" directory. 

4. run_parse_gh.py
>This puts all of the desired github information fron the json files into a csv called
>"gh_user_id" in the "parsed_files" directory.

5. run_data_analysis
>This program allows you to view A.) Summary Statistics B.) valid/invalid ID counts
>and C.) scatterplots of two data relationships. 
