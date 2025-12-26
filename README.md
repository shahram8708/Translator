# Translator

A simple web-based English ↔ Hindi translation application built using Flask and the `googletrans` library. The application provides a clean browser interface where users can enter text, choose translation direction, and instantly receive translated output using Google Translate services.

## Overview

The application consists of a lightweight Flask backend that exposes a translation endpoint and a frontend interface rendered through an HTML template. Users can type text in either English or Hindi and select whether to translate from English to Hindi or Hindi to English. The translated text is returned as JSON and displayed dynamically on the page.

## Features

* Translate English text to Hindi
* Translate Hindi text to English
* Simple and responsive web UI
* Real-time translation without page reload
* Error handling for invalid translation direction

## Tech Stack

* **Backend:** Flask
* **Translation Engine:** googletrans (Google Translate API wrapper)
* **Frontend:** HTML, CSS, JavaScript (Fetch API)
* **Production Support:** gunicorn

## Project Structure

```
Translator-main/
│
├── app.py                 # Flask application and translation logic
├── requirements.txt       # Dependencies
│
└── templates/
    └── index.html         # Web interface
```

## Installation

1. Ensure Python is installed.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open the browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Open the application in a web browser.
2. Enter text in the input box.
3. Select one of the following options:

   * English to Hindi
   * Hindi to English
4. Click the **Translate** button.
5. The translated result appears below the button.

## API

### `POST /translate`

Request body (JSON):

```json
{
  "text": "Hello",
  "direction": "en_to_hi"
}
```

Supported values for `direction`:

* `en_to_hi`
* `hi_to_en`

Response:

```json
{
  "translated_text": "नमस्ते"
}
```

If an invalid direction is sent, the response will contain:

```json
{
  "translated_text": "Invalid translation direction"
}
```

## Notes

* Internet connection is required because translations rely on Google services.
* This application is intended for learning and demonstration purposes.
