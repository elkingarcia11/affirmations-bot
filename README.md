# Auto-Tweeting Affirmation Bot

## Overview

This project automates the process of posting affirmations on Twitter by selecting random texts from a CSV file, creating images with text overlaid, and posting them at different times of the day. The app is built using Python and leverages the `Tweepy` library for Twitter integration, `Pillow` for image manipulation, and various utility modules for time-based logic and CSV handling.

## Features

- **Random Tweet Generation**: Selects random affirmations from a CSV file.
- **Dynamic Image Creation**: Overlays affirmation text on images for visual appeal.
- **Time-Based Tweeting**: Tweets change based on the time of day (morning, evening, night).
- **Twitter Integration**: Automatically posts tweets to a Twitter account using Tweepy.

## Prerequisites

- Python 3.x
- Twitter Developer Account with API keys and access tokens
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/twitter-auto-tweeting-app.git
   cd twitter-auto-tweeting-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Twitter API credentials by creating a `.env` file in the root directory:

   ```env
   TWITTER_CONSUMER_KEY=your_consumer_key
   TWITTER_CONSUMER_SECRET=your_consumer_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```


4. Add your Google Cloud Storage Service Account Credentials in a file called `service_account_credentials.json` and add `GOOGLE_APPLICATION_CREDENTIALS=service_account_credentials.json` to the `.env` file in the root directory

## Usage

1. Add your affirmation texts to `assets/affirmations.csv`. Each line in the CSV should contain one affirmation text.

2. Place your image files in a Google Cloud Storage bucket directory. The app will use these images as backgrounds for the affirmation text. Example images:
   - `morning.jpg`
   - `evening.jpg`
   - `night.jpg`

3. Place your font file in a Google Cloud Storage bucket directory. The app will use this font for the affirmation text in the image. Example font:
   - `PlayfairDisplay.ttf`

3. Run the script to start posting random affirmations:

   ```bash
   python main.py
   ```

4. The script will:
   - Generate an image with the affirmation text.
   - Determine the appropriate time of day (morning, evening, night) and choose the correct background image.
   - Post the generated image and text to Twitter.

## File Structure

```
.
├── assets/
│   ├── morning.jpg
│   ├── evening.jpg
│   ├── night.jpg
│   └── affirmations.csv
├── twitter_client.py  # Handles Twitter API interactions
├── main.py            # Main script that runs the app
├── requirements.txt   # List of dependencies
├── image_utils.py     # Image manipulation utilities
├── date_utils.py      # Date and time utilities
└── csv_utils.py       # CSV handling utilities
└── gcs_utils.py       # Google Cloud Storage handling utilities
```

## Modules

### `twitter_client.py`
Handles interaction with the Twitter API using `Tweepy`. It posts tweets with optional images.

### `main.py`
Runs the main logic of the app, including selecting a random affirmation, generating an image, and posting to Twitter.

### `image_utils.py`
Contains functions to overlay text on images, center text, and save the generated images with a unique filename.

### `date_utils.py`
Defines sub-ranges of the day (morning, evening, night) and checks which sub-range the current time falls into.

### `csv_utils.py`
Handles reading affirmations from the CSV file and selecting a random affirmation.


### `gcs_utils.py`
Handles fetching ad processing files from a Google Cloud Storage bucket.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
