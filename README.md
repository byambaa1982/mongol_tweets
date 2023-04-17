# Python Twitter API and Google Cloud Integration
This project is designed to demonstrate the integration of the Twitter API with Google Cloud Platform - Using Machine Learning APIs.

## Dependencies
The following libraries are required for this project:

- tweepy
- pandas
- numpy
- regex
- json
- time
- io
- datetime
- pandas_gbq

## Authentication

To use this project, you need to authenticate against the Google Cloud APIs. Follow these steps to get started:

1. Visit the API console and choose "Credentials" on the left-hand menu.
2. Choose "Create Credentials" and generate an API key for your application. You should probably restrict it by IP address to prevent abuse, but for now, just leave that field blank and delete the API key after trying out this demo.
3. Copy the API key and enter it in the first executable cell of the notebook.

## Accessing Google Drive
You can access your Google Drive files by mounting your Google Drive in Colab.

```python

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

```
## Functions

### `desc_users`

This function takes a list of Twitter usernames and returns a dataframe containing information about each user's account, including their name, screen name, description, number of tweets, number of friends, number of followers, account age, and average tweets per day.

 ``` python

def desc_users(account_list):
    users = {}
    users["name"] = []
    users["screen_name"] = []
    users["description"] = []
    users["statuses_count"] = []
    users["friends_count"] = []
    users["followers_count"] = []
    users["account_age"] = []
    users["average_tweets_per_day"] = []

    if len(account_list) > 0:
        for target in account_list:
            try:
                item = api.get_user(target)
                users["name"].append(item.name)
                users["screen_name"].append(item.screen_name)
                users["description"].append(item.description)
                users["statuses_count"].append(item.statuses_count)
                users["friends_count"].append(item.friends_count)
                users["followers_count"].append(item.followers_count)

                tweets = item.statuses_count
                account_created_date = item.created_at
                delta = datetime.utcnow() - account_created_date
                account_age_days = delta.days
                users["account_age"].append(account_age_days)

                if account_age_days > 0:
                    users["average_tweets_per_day"].append(float(tweets)/float(account_age_days))
            except:
                print("not found:{}".format(target))

    df = pd.DataFrame(users, columns=users.keys())
    return df
 ```
