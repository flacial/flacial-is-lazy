from simple_chalk import chalk

## A script for my Telegram channel posts
def postMaker():
    tags = input("Tags: ")
    description = input("Description: ")
    link = input("Link: ")
    return chalk.yellow.bold(f"**Tags:** {tags}\n\n**Description**: {description}\n\n**Link:** {link}")
    
    
if __name__ == '__main__':
    print(postMaker())