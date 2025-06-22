# 🩺 Symptoms Extractor (AI Mini Project)

This project is a simple NLP-based tool that **extracts symptoms and duration** from patient complaints using **spaCy** and **regular expressions**.

## 🧠 Features

- Identifies common symptoms (e.g., fever, cough, headache)
- Extracts duration phrases (e.g., "for 3 days", "since Monday")
- Saves the extracted data to a JSON file
- Interactive command-line interface

## 📥 Sample Input

```bash
Enter patient complaint: I've been having a sore throat and cough for 5 days.
{
  "symptoms": [
    "sore throat",
    "cough"
  ],
  "duration": [
    "for 5 days"
  ]
}
git clone https://github.com/yogaprriya-ai/symptoms-extractor
cd symptom-extractor
pip install spacy
python -m spacy download en_core_web_sm
python symptoms-extractor.py



