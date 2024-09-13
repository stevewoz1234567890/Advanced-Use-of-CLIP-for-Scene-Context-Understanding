import os
import json
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from itertools import combinations

model_name = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_name)
processor = CLIPProcessor.from_pretrained(model_name)

basic_objects = [
    "person",
    "girl",
    "boy",
    "man",
    "woman",
    "cat",
    "dog",
    "car",
    "tree",
    "bicycle",
    "dolphin",
    "shark",
]
interactions = [
    "playing fetch",
    "driving",
    "walking",
    "sitting",
    "riding a bicycle",
    "running",
    "capturing a photo",
]
thematic_contexts = [
    "leisure time in a park",
    "morning commute",
    "outdoor exercise",
    "urban environment",
    "aquarium",
]


def generate_combinations(objects):
    return list(combinations(objects, 2))  # Generate combinations of pairs only


def format_combinations(combinations):
    formatted_combinations = []
    for combination in combinations:
        formatted_combinations.append(f"{combination[0]} and {combination[1]}")
    return formatted_combinations


def analyze_image(image_path):
    image = Image.open(image_path)

    def get_top_phrases(phrases):
        inputs = processor(
            text=phrases, images=image, return_tensors="pt", padding=True
        )
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image

        if logits_per_image.numel() == 0:
            print("No predictions for input image:", image_path)
            return []

        probs = logits_per_image.softmax(dim=1)
        scores, indices = probs.topk(len(phrases), dim=1)

        top_phrases = [
            (phrases[idx], score.item()) for idx, score in zip(indices[0], scores[0])
        ]
        return top_phrases

    # Generate and format combinations of basic objects
    object_combinations = generate_combinations(basic_objects)
    formatted_combinations = format_combinations(object_combinations)

    # Step 1: Identify Basic Objects
    detected_objects = get_top_phrases(formatted_combinations)

    # Step 2: Infer Interactions
    inferred_interactions = get_top_phrases(interactions)

    # Step 3: Deduce Thematic Contexts
    deduced_themes = get_top_phrases(thematic_contexts)

    # Combine dominant phrases
    dominant_phrases = {
        "basic_object": max(detected_objects, key=lambda x: x[1])[0],
        "interaction": max(inferred_interactions, key=lambda x: x[1])[0],
        "thematic_context": max(deduced_themes, key=lambda x: x[1])[0],
    }

    # Prepare summary text
    summary_text = ", ".join(
        phrase for phrase in dominant_phrases.values() if phrase is not None
    )

    # Prepare output JSON
    result = {
        "image_name": os.path.basename(image_path),
        "basic_objects": detected_objects,
        "inferred_interactions": inferred_interactions,
        "deduced_themes": deduced_themes,
        "dominant_phrases": dominant_phrases,
        "summary_text": summary_text if summary_text else "No clear theme",
    }

    return result


def process_directory(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(directory, filename)
            try:
                print(f"Processing {image_path}")
                result = analyze_image(image_path)
                results.append(result)
                with open(f"{image_path}.json", "w") as f:
                    json.dump(result, f, indent=4)
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

    return results


# Main script execution
input_directory = "images"
process_directory(input_directory)
