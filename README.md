# Multilingual Translator and Text Analysis Tool

A user-friendly web application built with **Gradio** and **Hugging Face Transformers** to provide a suite of text processing functionalities, including translation, summarization, sentiment analysis, grammar correction, and character counting.

[**Live Demo**](https://huggingface.co/spaces/oB3TAo/text-app) - Explore the deployed version of the app.

## Features

- **Translation**: Translate text from English to French, German, or Romanian.
- **Text Summarization**: Summarize lengthy texts and provide word counts.
- **Sentiment Analysis**: Determine the sentiment (positive, negative, neutral) of a given text.
- **Grammar Correction**: Automatically correct grammar errors in English sentences.
- **Character Counting**: Instantly count the number of characters in any text input.

## Getting Started

### Prerequisites

- **Python** (3.x recommended)
- **pip** (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/oB3TAo/translation-app.git
   cd translation-app
   ```

2. **Install dependencies**:
   Install all required packages listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the web app locally by running:
   ```bash
   python main.py
   ```

4. **Access the app**:
   Once the server starts, the app will automatically open in your browser. You can also manually navigate to `http://127.0.0.1:7860/`.

## How to Use

The app offers the following functionalities:

1. **Translation**: Select a language (French, German, Romanian) and input text in English to translate.
2. **Text Summarization**: Paste or type a large block of text and get a concise summary along with a word count.
3. **Sentiment Analysis**: Input any text to determine its emotional tone (positive, negative, or neutral).
4. **Grammar Correction**: Submit an English sentence, and the tool will return a grammatically corrected version.
5. **Character Counting**: Instantly count the number of characters in your inputted text.

You can also use predefined examples within the app to test each functionality.

## Technologies Used

- **Gradio**: For building the user interface of the web app.
- **Hugging Face Transformers**: For implementing NLP models such as translation, summarization, and sentiment analysis.