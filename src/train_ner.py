import spacy
from spacy.training import Example
import json
import os

# Load a blank Vietnamese model
nlp = spacy.blank("vi")
ner = nlp.add_pipe("ner")

# Add new labels to the model
labels = ["PRODUCT", "PRICE", "QUANTITY", "CUSTOMER", "START_TIME", "END_TIME", "BUSINESS_NAME", "SALE_RESULT"]
for label in labels:
    ner.add_label(label)

# Read training data
with open("../data/output.json", "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

# Convert training data
examples = []
for data in TRAIN_DATA:
    if "text" in data:
        doc = nlp.make_doc(data["text"])
        entities = [(ent["start"], ent["end"], ent["label"]) for ent in data["entities"]]
        examples.append(Example.from_dict(doc, {"entities": entities}))

# Train the model
optimizer = nlp.begin_training()
for epoch in range(30):  # Increase the number of epochs
    losses = {}
    nlp.update(examples, sgd=optimizer, losses=losses)
    print(f"Epoch {epoch+1}, Loss: {losses}")

# Create directory if it doesn't exist
output_dir = "../models/model_ner"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the trained model
nlp.to_disk(output_dir)
print("✅ Model saved to 'models/model_ner'")

# Function to process new text and return results in JSON format
def process_text(text):
    doc = nlp(text)
    result = {"text": text, "entities": []}
    for ent in doc.ents:
        result["entities"].append({
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_
        })
    return result

# Read data from input.txt and process
with open("../data/input.txt", "r", encoding="utf-8") as f:
    input_texts = f.read().split("======")

results = []
for text in input_texts:
    text = text.strip()
    if text:
        results.append(process_text(text))

# Save results to JSON file
output_file = "../data/processed_output.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"✅ Results saved to '{output_file}'")