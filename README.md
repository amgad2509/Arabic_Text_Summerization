# Automatic Text Summarization Web Application

This project is a web-based application for automatic text summarization using pre-trained models. It leverages the power of machine learning to generate concise summaries of given text inputs. The summarization model used in this project is based on the transformers library by Hugging Face.

## Requirements

- Python 3.x
- PyTorch
- Transformers
- NLTK

You can install the required Python packages using pip:

```bash
pip install torch transformers nltk
```

Additionally, NLTK requires some additional downloads. You can download these resources by running the following commands in a Python environment:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## Usage

To use this application, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies as mentioned above.

3. Run the web application script.

4. Access the web application through your browser.

## How it Works

The core functionality of this application lies in the `get_summary` function defined in `summarizer.py`. This function takes a text input and generates a summary using a pre-trained language model.

The steps involved in summarization are as follows:

1. Tokenize the input text into sentences using NLTK's sentence tokenizer.
2. Preprocess the text and append necessary tokens for summarization.
3. Encode the tokenized text using the pre-trained tokenizer.
4. Generate the summary using the pre-trained language model.
5. Decode the generated summary and return the result.

