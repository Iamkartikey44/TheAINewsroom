# TheAINewsroom

## Overview

TheAINewsroom is a GenerativeAI project that creates a newsroom experience by fetching the latest news using the [NewsAPI](https://newsapi.org/). Additionally, it generates a video based on the fetched news using the [D-ID](https://www.d-id.com/). This project consists of three main files: `app.py`, `get_news.py`, and `news_video.py`. To use this project, you'll need API keys for both D-ID and NewsAPI.

<video src='https://github.com/Iamkartikey44/TheAINewsroom/blob/main/video.mp4' width=180/>


## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Required Python libraries (install using `pip install -r requirements.txt`)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Iamkartikey44/TheAINewsroom.git
    cd TheAINewsroom
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain API keys:

    - Get your D-ID API key from [D-ID](https://www.d-id.com/).
    - Get your NewsAPI key from [NewsAPI](https://newsapi.org/).

4. Configure API keys:

    Open `.env` and replace `YOUR_DID_API_KEY` and `YOUR_NEWSAPI_KEY` with your D-ID and NewsAPI keys, respectively.

## Usage

### 1. Fetch Latest News

Run `get_news.py` to fetch the latest news:

```bash
python new_api.py
```

This script fetches the latest news using the NewsAPI.

### 2. Generate Video

Run `news_video.py` to generate a video based on the fetched news with the help DID API:

```bash
python news_video.py
```

This script uses the fetched news to generate a video.

### 3. Run the Main App

Run `app.py` to start the main application:

```bash
python app.py
```

This script serves as the main file to execute the entire newsroom application.

## Video Link

Check out a sample video generated by TheAINewsroom [here](https://github.com/Iamkartikey44/TheAINewsroom/blob/main/video.mp4).

## License

This project is licensed under the [MIT License](https://github.com/Iamkartikey44/TheAINewsroom/blob/main/LICENSE).

## Acknowledgments

- [D-ID](https://www.d-id.com/) for providing the Video Genration API.
- [NewsAPI](https://newsapi.org/) for providing the news data API.

Feel free to contribute and make improvements to TheAINewsroom!

