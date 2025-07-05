"""
    This is an example for get post detail by FacebookApi class.

    Refer: https://developers.facebook.com/docs/graph-api/reference/pagepost
"""

import os
from pyfacebook import FacebookApi

APP_ID = '1442432229496744' # os.environ.get("APP_ID")  # Your App ID
APP_SECRET = '4c4ba4b8e5c31214bfe0abd46d711b4c' # os.environ.get("APP_SECRET")  # Your App secret
ACCESS_TOKEN = 'EAAUf4mym16gBOzNv4tmS1BzZBGHK44mibP7RyQr3vhOKnJf1d2Ay5BcFJ4elzfmittldlwVn5iZAiN4H6WH7MZA6NmOSNtP0fZC38BgWm9Xdb4vfMNZCgZAgTfFuJc0vmnhYL0nMzEpQLsmXkQMNhVIxjKop17bBjnOTAgZBRwXSdJ46LLZAN6fE1ArnZCkjupZAddQHk4rgSJS5CzBZBbS' # os.environ.get("ACCESS_TOKEN")  # Your Access Token


def handler(post_id):
    api = FacebookApi(app_id=APP_ID, app_secret=APP_SECRET, access_token=ACCESS_TOKEN)
    post = api.post.get_info(
        post_id=post_id,
        fields="id,message,created_time,full_picture,status_type,updated_time",
    )
    print(f"ID: {post.id}")
    print(f"Time: {post.created_time}")
    print(f"Data: {post.to_json()}")
    return True


if __name__ == "__main__":
    handler(post_id="19292868552_371106181716390")
