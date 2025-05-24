# 🧠 Emotion Recognition Assistant (Sentiment Analysis Component)

This repository showcases my contribution to the **Emotion Recognition Assistant**, a graduation project developed at Yarmouk University. The overall goal of the project is to help individuals who have difficulty interpreting emotions in speech and text — such as those with autism, alexithymia, social anxiety, or traumatic brain injury (TBI).

> 🔍 **Note:** This repository focuses specifically on the **Sentiment Analysis** portion of the project. Due to academic policy, full implementation details and datasets are not shared publicly.

---

## 📌 Project Summary

The Emotion Recognition Assistant is an intelligent application designed to detect:
- **Emotions from speech**
- **Sentiment from text**

It provides real-time emotional feedback to users through an accessible web interface. While the full project includes multiple machine learning modules, my contribution was centered on **text-based sentiment classification**.

---

## 🧩 My Contribution: Sentiment Analysis

For the sentiment analysis component, I combined datasets from **Kaggle** and **Hugging Face** to build a well-balanced dataset with three sentiment classes:
- **Negative**
- **Neutral**
- **Positive**

To improve generalization and fairness in training, I carefully handled **class imbalance** by integrating datasets and applying **downsampling** where necessary — ensuring minimal data loss while preserving diversity.

I trained and evaluated **two deep learning models** for this task:
- **LSTM** (Long Short-Term Memory)
- **GRU** (Gated Recurrent Unit)

Both models were enhanced using attention mechanisms and regularization techniques to improve performance and reduce overfitting.

---

## 📈 Results

The models were evaluated on a large-scale test set using accuracy and confusion matrix analysis. Final results:

| Model | Accuracy |
|-------|----------|
| LSTM  | 91%      |
| GRU   | 90%      |

- Most misclassifications were between **positive** and **neutral**, which is less critical than reversing positive/negative sentiment.
- The LSTM model showed better balance across all classes, making it more suitable for real-world use.

---

## 🚀 Application Overview

The Emotion Recognition Assistant is a Streamlit-based web application that integrates both:

- **Speech Emotion Recognition**: Users can upload audio files to analyze emotional tone in speech.
- **Text Sentiment Analysis**: Users can input written text to detect underlying sentiment (negative, neutral, or positive).

The application provides real-time, intuitive feedback and is designed with accessibility in mind — particularly for users who experience difficulty in interpreting emotional cues.

> While the full system includes both speech and text analysis, this repository highlights the sentiment analysis (text) component as part of my individual contribution.

---


## 👩‍💻 Authors

- **Fadia Alhajjeh**
- **Rawan Ahmad**

Supervised by **Dr. Enas Alikhashashneh**  
*Yarmouk University, Department of Information Systems*

---

## 📜 License

This project is for academic and educational purposes only.
