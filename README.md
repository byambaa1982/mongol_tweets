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

python ```

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

```
