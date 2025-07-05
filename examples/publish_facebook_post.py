"""
    This is an example for facebook page publish a post.

    Refer: https://developers.facebook.com/docs/graph-api/reference/page/feed#publish
"""

import os

from pyfacebook import GraphAPI

APP_ID = '1442432229496744' # os.environ.get("APP_ID")  # Your App ID
APP_SECRET = '4c4ba4b8e5c31214bfe0abd46d711b4c' # os.environ.get("APP_SECRET")  # Your App secret
ACCESS_TOKEN = 'EAAUf4mym16gBOZBPLu6V7tvU9H8lpscgg4rvZBOo3ZCnZBNRLXf3aysrZCVt4a1Ca1w1TZBGvBJOri7TRdNuXLhvudEG0m2LwQKb45alu2C6izDQ7VLFvS2wq2hENP8XeGyUdZBlCKHIPiO5E0aD6wtxGKSZCtZA4GVqXhWrlSSZCaAoQIehYqlLtESQBFc3CuY8mZBHEyAydWIycQVF3iunCoxR4Rg3aUjnTAeeYZAr61LWvwZDZD'

def publish_simple_posts(page_id):
    api = GraphAPI(app_id=APP_ID, app_secret=APP_SECRET, access_token=ACCESS_TOKEN)

    data = api.post_object(
        object_id=page_id,
        connection="feed",
        params={
            "fields": "id,message,created_time,from",
        },
        data={"message": "This is a test message by api"},
    )
    print(data)
    # {'id': 'xxx', 'message': 'This is a test message by api', 'created_time': '2022-06-01T03:49:36+0000', 'from': {'name': 'xx', 'id': 'xxxx'}}
    return True


if __name__ == "__main__":
    publish_simple_posts(page_id="653224174543911") # "1389220978975648" 109845401782936
