# 🧠 Emotion Recognition Assistant (Sentiment Analysis Component)

This repository presents the **Sentiment Analysis** module of the *Emotion Recognition Assistant* project — a deep learning system developed to support individuals who face difficulties understanding emotional cues, such as those with autism, alexithymia, social anxiety, or traumatic brain injury (TBI). While the full project includes both audio-based emotion recognition and text-based sentiment classification, this repository focuses on the **text sentiment analysis** component only.

> 🔒 **Note:** Due to academic restrictions, full project code is not publicly available. This repository contains selected methods, dataset structure, and key insights.

---

## 📌 Project Overview

Understanding emotions is key to effective communication, but many people struggle with interpreting emotional cues. This project addresses that challenge by combining machine learning models to analyze:
- Emotions in speech
- Sentiment in text

This repository focuses on the **text-based sentiment analysis**, where models classify text into:
- **Negative**
- **Neutral**
- **Positive**

---

## 🗂 Dataset

The sentiment analysis dataset was created by combining sources from **Kaggle** and **Hugging Face** to achieve a balanced, high-quality corpus of 933,000 samples. Class imbalance was addressed using **downsampling**, which minimized data loss while improving generalization.

---

## 🧹 Preprocessing

Key preprocessing steps included:

- **Text Cleaning**
  - Lowercasing
  - URL & user mention removal
  - Repeated character reduction
  - Stop word removal
  - Stemming
- **Tokenization and Padding**
  - Vocabulary size: 55,000
  - Sequence length: 30 (based on histogram analysis)
- **Label Encoding**
  - Multi-class one-hot encoding

---

## 🧠 Model Architecture

Two RNN-based models were explored: **LSTM** and **GRU**, both enhanced with **Attention Mechanisms**.

### 🌀 LSTM (Final Model)
- Embedding Layer: 256-dim vectors
- Bidirectional LSTM (x2)
- Attention Layer
- Dense layers + Softmax
- Dropout + L2 Regularization

**Performance:**  
✅ **Final Accuracy:** 91%  
⚖️ Best balance between caution and confidence in classification

### ⚡ GRU
- Faster, fewer parameters than LSTM
- Performs well on positive class, but prone to overconfidence

**Performance:**  
✅ **Final Accuracy:** 90%  
⚠️ Sometimes misclassifies negative as positive

---

## 📊 Evaluation

Metrics used:
- **Accuracy**
- **Confusion Matrix** to assess precision across classes

**Common Misclassifications:**
- Positive → Neutral (acceptable)
- Negative → Neutral (preferable to mislabeling as positive)

These cautious misclassifications suggest the model errs on the side of neutrality, which is often desirable in real-world applications.

---

## 🚀 Application Preview

This module is part of a larger Streamlit-based app that allows users to:

- Input text and receive real-time sentiment analysis
- View results as negative, neutral, or positive
- Receive explanations powered by LLMs (e.g., GPT)

> 

---

## 🔧 Future Work

- Expand support for **multi-language sentiment classification**
- Include **sarcasm and contextual awareness**
- Integrate real-time analysis features for broader application use
- Improve robustness with more balanced, real-world text samples

---

## 📁 Disclaimer

The full project includes:
- Speech Emotion Recognition using CNNs and ViTs
- Custom loss functions and Squeeze-and-Excitation (SE) blocks
- Streamlit-based GUI for audio and text inputs

> However, **this public repository includes only the sentiment analysis portion** due to university restrictions.

---

## 👩‍💻 Authors

- **Fadia Alhajjeh**
- **Rawan Ahmad**

Supervised by **Dr. Enas Alikhashashneh**  
*Yarmouk University, Department of Information Systems*

---

## 📜 License

This project is for academic and educational purposes only.
