import spacy
import re
import json

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Custom symptom list (expand if you want)
SYMPTOMS = [
    "headache", "fever", "cough", "sore throat", "nausea",
    "fatigue", "vomiting", "diarrhea", "pain", "chills", "dizziness", "rash"
]

def extract_symptoms_and_duration(text):
    doc = nlp(text.lower())

    # Find symptoms
    found_symptoms = [sym for sym in SYMPTOMS if sym in text.lower()]

    # Find duration using regex
    duration_patterns = [
        r"for\s+\d+\s+\w+",
        r"since\s+\w+",
        r"\d+\s+(days?|weeks?|months?)",
        r"over\s+the\s+\w+"
    ]
    found_durations = []
    for pattern in duration_patterns:
        match = re.search(pattern, text.lower())
        if match:
            found_durations.append(match.group())

    result = {
        "symptoms": found_symptoms,
        "duration": found_durations
    }

    return result

# Run example
if __name__ == "__main__":
    patient_input = input("Enter patient complaint: ")
    result = extract_symptoms_and_duration(patient_input)
    print("\nExtracted:")
    print(json.dumps(result, indent=2))

    # Optional: Save to file
    with open("extracted_data.json", "w") as f:
        json.dump(result, f, indent=2)
    print("\n✅ Result saved to extracted_data.json")

