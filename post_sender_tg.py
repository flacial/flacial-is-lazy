from simple_chalk import chalk
import requests

## A script for my Telegram channel posts
def postMaker():
    url = "https://api.telegram.org/<bot-key>/sendMessage"
    
    tags = input("\nTags: ")
    if not tags.find('-'):
        return chalk.red("\nText has a hyphen!\n")
    else:
        description = input("Description: ")
        
        # TODO - add conditional check for if the URL is working
        link = input("Link: ")
    
    data = {
        "chat_id": "<Chat-id>",
        "text": f"<b>Tags:</b> {tags}\n\n<b>Description</b>: {description}\n\n<b>Link:</b> {link}",
        "parse_mode": "html"
    }
    
    # Send a post request to the bot's API
    response = requests.post(url, data)

    # Check if there's an error
    if response.status_code == 200:
        return chalk.green("\nThe post has been sent successfully!\n")
    else:
        return chalk.red("\nSomething wrong has happened\n")
    
    
if __name__ == '__main__':
    print(postMaker())