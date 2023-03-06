import requests
from bs4 import BeautifulSoup

# Set the URL of the Baidu Tieba website you want to scrape
url = 'https://tieba.baidu.com/f?kw=python'

# Send a GET request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the posts on the page by searching for a specific HTML tag and class
posts = soup.find_all('div', {'class': 'threadlist_title'})

# Loop through each post, extract its link, and send a GET request to retrieve its content
for post in posts:
    link = 'https://tieba.baidu.com' + post.a['href']
    post_response = requests.get(link)
    post_soup = BeautifulSoup(post_response.content, 'html.parser')
    
    # Find all the comments in the post and print their text
    comments = post_soup.find_all('div', {'class': 'd_post_content'})
    for comment in comments:
        print(comment.get_text(strip=True))
