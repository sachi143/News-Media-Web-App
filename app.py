from flask import Flask, render_template, request
import requests
from datetime import datetime
import os
from newspaper import Article
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variable
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Check if the API key is available
if not NEWS_API_KEY:
    raise Exception("NEWS_API_KEY is missing. Please ensure it's set in the .env file.")

BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Fetch articles from NewsAPI with pagination and optional topic filtering
def fetch_news(page=1, page_size=4, topic=None):
    params = {
        'apiKey': NEWS_API_KEY,  # Use the API key
        'country': 'us',
        'page': page,
        'pageSize': page_size
    }

    if topic:  # Add topic filtering
        params['category'] = topic

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error fetching news: {data.get('message', 'Unknown error')}")

    articles = data.get('articles', [])
    total_results = data.get('totalResults', 0)

    return articles, total_results


# Get the article content (fallback for NewsAPI truncation)
def get_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:300]  # Truncate content to 300 characters
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors like 403 Forbidden
        if e.response.status_code == 403:
            print(f"Error scraping article: {e} on URL {url}")
        return None
    except Exception as e:
        print(f"General error extracting content: {e} on URL {url}")
        return None


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    topic = request.args.get('topic', None)  # Get the selected topic from query params
    page_size = 4

    # Fetch articles based on page and optional topic
    articles, total_results = fetch_news(page=page, page_size=page_size, topic=topic)
    news_data = []

    for article in articles:
        try:
            content = get_article_content(article['url'])
            if content:
                news_data.append({
                    'title': article['title'],
                    'content': content,
                    'link': article['url'],
                    'image': article['urlToImage'],
                    'timestamp': datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y at %I:%M %p'),
                    'source': article['source']['name']
                })
        except Exception as e:
            print(f"Error processing article: {e}")
            continue

    # Pagination details
    total_pages = (total_results + page_size - 1) // page_size

    return render_template('index.html', articles=news_data, current_page=page, total_pages=total_pages, selected_topic=topic)


if __name__ == '__main__':
    # Add a debug print to check if the API key is loaded correctly
    print(f"Loaded API Key: {NEWS_API_KEY}")  # This will print the API key for debugging purposes
    app.run(debug=True)
