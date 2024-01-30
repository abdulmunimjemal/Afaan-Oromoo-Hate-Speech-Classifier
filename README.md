# AfanOromo Hate Speech Classifier

## Overview

AfanOromoHateSpeechClassifier is a side project I am currently working on. The project focuses on addressing the issue of hate speech in Afaan Oromo language on Facebook. The dataset used for this classifier is collected from various Facebook pages, including those of political activists, broadcasting media, religious organizations, politicians, and famous personal blogs. The goal is to obtain a diverse and representative dataset, as these pages often generate numerous reactions and comments.

## Dataset Collection

The dataset collection process follows specific rules for selecting Facebook pages:
1. Pages that predominantly use the Afaan Oromo language for posts are chosen.
2. Pages with likes and followers exceeding 20,000 are selected.
3. Pages belonging to religious media, famous vloggers, politicians, and broadcasting media are prioritized to ensure a comprehensive dataset.

In total, 18 different Facebook pages are selected, and 20,000 unique datasets are collected from posts and comments.

Dataset Collection is done by Baharudin Sherif (2022) of Mettu University Faculty of Engineering and Technology.

## Dataset Labels

The dataset is annotated with binary classification labels: 'Hate' and 'Free.' After cleaning and removing unnecessary characters, among the 20,000 collected datasets, 9,985 are annotated as 'Free,' while the remaining 1,015 are annotated as 'Hate.'

## Implemented Models

The project includes the implementation of the following machine learning models for hate speech classification:

1. **Logistic Regression:**
   - Simple and efficient for binary classification tasks.
   - Suitable for high-dimensional datasets.

2. **Naive Bayes:**
   - Particularly good for text classification tasks.
   - Fast and works well with relatively small datasets.

3. **Support Vector Machines (SVM):**
   - Effective for high-dimensional spaces, like text data.
   - Can handle non-linear decision boundaries.

4. **Random Forest:**
   - Ensemble method that combines multiple decision trees.
   - Robust and less prone to overfitting.

5. **Gradient Boosting (XGBoost):**
   - Builds multiple weak learners sequentially, focusing on misclassified instances.
   - Can handle complex relationships in the data.

6. **Neural Networks (LSTM using Keras):**
   - Deep learning model for capturing complex patterns in text data.
   - Includes embedding layers and LSTM layers.

Feel free to add more or improve the current implementations. (Contribute)


## Project Structure

The project structure includes the implementation of a hate speech classifier using machine learning algorithms.

📂 **data/** \
   ├── Labels.xlsx \
   └── Posts.xlsx \
 \
📂 **models/** \
   └── (Trained and saved models will be saved here) \
 \
📂 **src/** \
   ├── 📂 **preprocessing/** \
   │    ├── special_char_handler.py \
   │    ├── stemmer.py \
   │    ├── stopword_remover.py \
   │    ├── tokenizer.py \
   │    └── preprocessor.py (integrates the above all and provides a pipeline function) \
   ├── train.ipynb \
   └── (Other source code files) \
 \
📄 **requirements.txt** 



## Contribution
Contributions are welcomed. Please follow the guidelines when contributing. :)

## **Note:**
This project is based on real-world challenges and aims to contribute to the identification and mitigation of hate speech in the Afaan Oromo language on social media platforms.
