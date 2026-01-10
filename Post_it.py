import requests
import os 
import requests

def post_it(message: str):
    url = "https://linkedin.com/api/post"
    payload = {"message": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Post successful!")
    else:
        print("Failed to post message.")
    return response
if __name__ == "__main__":
    message = input("Enter the message to post: ")
    post_it(message)