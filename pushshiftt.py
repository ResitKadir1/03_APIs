from pmaw import PushshiftAPI
import os
import time
import pandas as pd

if not os.path.exists("PushshiftAPI_Data"):
    os.makedirs("PushshiftAPI_Data")
PushshiftAPI_Data = "PushshiftAPI_Data/"


# create an API wrapper object
# PMAW automatically manages parallelization of requests using multiple
# proesses running on multiple CPU cores
api = PushshiftAPI(num_workers=os.cpu_count()*5)

# setting query parameters
subreddit = 'wallstreetbets'
before = int(time.time())
after = 0
limit = 100

# get submissions
submissions = api.search_submissions(subreddit=subreddit, limit=limit, before=before, after=after)
sub_df = pd.DataFrame(submissions)

# get comments
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
comments_df = pd.DataFrame(comments)
#print(comments_df)

print(sub_df.head())
print(comments_df.head())
comments_df.to_csv(PushshiftAPI_Data+"output.csv", encoding='utf-8', index=False)
comments_df.head().to_csv(PushshiftAPI_Data+"comments_df_head.csv", encoding='utf-8', index=False)
sub_df.head().to_csv(PushshiftAPI_Data+"sub_df_head.csv", encoding='utf-8', index=False)