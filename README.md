# Advanced use of CLIP for scene context understanding

Zero-shot scene analysis with [OpenAI CLIP](https://github.com/openai/CLIP) (`openai/clip-vit-base-patch32` via [Hugging Face Transformers](https://huggingface.co/docs/transformers)). Images are interpreted in three layers—co-occurring entities, activities, and high-level themes—using text prompts scored against the image embedding.

## Features

- **Layered prompts**: object pairs (e.g. `person and dog`), interaction phrases, and thematic context strings.
- **Ranked outputs**: softmax scores over each phrase set; dominant pick per layer plus full rankings.
- **Batch processing**: all supported images under a folder; one JSON result file per image.

## Requirements

- Python 3.8+
- PyTorch (CPU or CUDA; install the wheel that matches your environment from [pytorch.org](https://pytorch.org))
- Dependencies listed in `requirements.txt`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you use a GPU, install a CUDA-enabled PyTorch build before or after `pip install -r requirements.txt` so it matches your driver.

## Usage

1. Place images in the `images` directory (supported extensions: `.png`, `.jpg`, `.jpeg`, `.webp`).
2. Run:

```bash
python main.py
```

For each image, the script writes `<image_filename>.json` alongside the image with ranked phrases and a short summary.

## Output format

Each JSON file includes:

| Field | Description |
|--------|-------------|
| `image_name` | Base filename of the processed image |
| `basic_objects` | Ranked list of `(phrase, score)` for formatted object pairs |
| `inferred_interactions` | Ranked interactions |
| `deduced_themes` | Ranked thematic contexts |
| `dominant_phrases` | Highest-scoring phrase per layer |
| `summary_text` | Comma-separated dominant phrases |

Scores are softmax probabilities over the corresponding phrase list for that layer.

## How it works

1. **Object layer**: CLIP compares the image to all pairwise combinations of labels in `basic_objects`, formatted as `"A and B"`, to surface likely co-occurring entities.
2. **Interaction layer**: The same image is scored against a fixed list of activity-style phrases.
3. **Theme layer**: Broader scenario phrases capture overall context.

This is **vision–language matching**, not a separate object detector: all layers use the same CLIP image–text similarity. Extend or replace the lists in `main.py` to suit your domain.

## Methodology and phrase design

**Object phrases** emphasize coverage of common scene elements (people, animals, vehicles, environment) informed by widely used vision datasets and everyday scenes.

**Interaction phrases** describe activities that often co-occur with those objects (e.g. walking, driving, playing fetch).

**Thematic phrases** aggregate object and activity cues into short scenario descriptions (e.g. commute, park leisure, urban settings).

Phrases can be refined by evaluating outputs on representative images and adjusting lists for precision versus recall. The hierarchical structure mirrors how humans move from “what is present” to “what is happening” to “what kind of situation is this,” while still relying on a single CLIP scoring pipeline per layer.

## Project layout

```
.
├── main.py              # CLIP model, prompts, and batch runner
├── requirements.txt
├── images/              # Input images (and generated *.json results)
└── README.md
```

## License

Specify a license in the repository root if you intend others to reuse this code.
