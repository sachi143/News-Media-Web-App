# News Media Web App 📡📰

This is a **News Media Web App** built using **Flask** and the **NewsAPI**. It displays the latest news articles with pagination and optional topic filtering. The app fetches article content, displays headlines, and allows users to navigate through news stories.

## Features ✨
- Fetches top headlines from the NewsAPI.
- Displays articles in a paginated format with 4 articles per page.
- Provides optional topic-based filtering (e.g., technology, sports, etc.).
- Displays article content, images, and publication details.
- Extracts full article content using the `newspaper` library in case of truncation.
- Responsive design using Bootstrap cards for a clean UI.

## Project Structure 📂

```
News Media Web App/
├── static/
│   └── style.css               # Custom CSS for styling
├── templates/
│   └── index.html              # HTML template for rendering the news articles
├── .env                        # Environment file containing the API key
├── app.py                      # Main Flask application
├── testing.py                  # File for testing the application
├── ngrok.exe                   # Optional tool for public URL exposure
└── README.md                   # Documentation file
```

## Prerequisites 🛠️

Before running the project, make sure you have the following installed:

- Python 3.7+
- Flask
- Requests
- Newspaper3k
- Python-dotenv

You can install the required libraries using:

```bash
pip install flask requests newspaper3k python-dotenv
```

## Setup Instructions 🚀

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sachi143/news-media-web-app.git
   cd news-media-web-app
   ```

2. **Set Up Environment Variables:**
   Create a `.env` file in the project directory and add your NewsAPI key:

   ```
   NEWS_API_KEY=your_news_api_key_here
   ```

3. **Run the Application:**
   Execute the following command in the project directory to start the Flask server:

   ```bash
   python app.py
   ```

4. **Access the App:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage 🏄‍♂️

- The homepage displays the latest top headlines.
- Use the pagination controls at the bottom to navigate between pages.
- You can filter articles by category by appending `?topic=<category>` to the URL, e.g., `http://127.0.0.1:5000?topic=technology`.

## Troubleshooting 🐛

- Ensure that the `.env` file contains a valid NewsAPI key.
- Check if all required libraries are installed using `pip freeze`.
- If API requests fail, verify the API key and network connectivity.

## Contributing 🤝

Feel free to contribute to this project by submitting issues or pull requests. Let's make it better together!

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more details.