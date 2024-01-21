# SMS-Spam-Classification-
Say goodbye to annoying spam texts with our smart system that tells you if a message is spam or not – it's like having a personal text superhero!


## Overview

This project implements a machine learning-based SMS spam classifier using a Naive Bayes model and TF-IDF vectorization. The system is designed to efficiently classify incoming SMS messages as spam or not spam. The integration of a Streamlit web application enhances user interaction and accessibility.

## Project Files

- **SMS Spam Classification.ipynb**: Jupyter notebook containing the source code for the project.
- **app.py**: Python script for the Streamlit web application.
- **model.pkl**: Pickled file containing the trained Naive Bayes classifier.
- **spam.csv**: Dataset file in Excel format containing labeled SMS messages.
- **vectorizer.pkl**: Pickled file containing the TF-IDF vectorizer.

## Usage

1. Open and run `SMS Spam Classification.ipynb` to explore the code and model training.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## How to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [NLTK](https://www.nltk.org/) for NLP tools.
- [Streamlit](https://streamlit.io/) for interactive web applications.

Feel free to explore, contribute, and provide feedback!
