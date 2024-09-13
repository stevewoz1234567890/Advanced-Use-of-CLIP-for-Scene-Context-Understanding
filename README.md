## Create venv
```bash
python3 -m venv venv
```

## Activate venv
```bash
source venv/bin/activate
```

## Install requirements
```bash
pip install -r requirements.txt
```

## Run the script
Put your image in the `images` folder and run the following command:

```bash
python main.py
```

[ChatGPT Chat Conversation](https://chatgpt.com/share/ab655c11-d152-4421-ad6d-f6bf8ef9c21d)

# Explain your choice of descriptive phrases and how they were developed or sourced.

## Choice of Descriptive Phrases and Their Development
When developing descriptive phrases for analyzing images using CLIP, the choice of phrases is critical to ensure accurate and comprehensive scene understanding. The phrases were chosen based on several factors:

1. Coverage of Common Objects and Activities:

    - The phrases need to cover a wide range of common objects, activities, and themes that are likely to appear in diverse images.

    - This ensures the model can recognize and interpret a variety of scenes accurately.

2. Hierarchical Structure:

    - The phrases are structured hierarchically into three categories: basic objects, interactions, and thematic contexts.

    - This hierarchy reflects different layers of interpretation, from simple object detection to complex scene understanding.

## Categories of Descriptive Phrases
1. Basic Objects:

    - Purpose: Identify fundamental elements present in the scene.
    - Examples: "dog", "car", "tree", "person", "bicycle".
    - Development:
        - Selected common objects that are frequently found in various scenes.
        - Included objects that are essential for understanding the context of many interactions and themes.
        - Sourced from datasets like ImageNet, COCO, and everyday observations to ensure comprehensive coverage.

1. Interactions:

    - Purpose: Infer the activities or events occurring in the scene based on the detected objects.
    - Examples: "playing fetch", "driving", "walking", "sitting", "riding a bicycle".
    - Development:
        - Chosen based on common human and animal activities.
        - Considered interactions that typically involve the previously identified objects.
        - Sourced from activity recognition datasets like AVA and from common verbs in everyday life.

1. Thematic Contexts:
    - Purpose: Deduce the broader context or theme of the scene by combining detected objects and inferred interactions.
    - Examples: "leisure time in a park", "morning commute", "outdoor exercise", "urban environment".
    - Development:
        - Created to represent typical scenarios that encompass multiple interactions and objects.
        - Themes are broader and provide a holistic understanding of the scene.
        - Developed by examining common contexts in visual data and human experiences.

## Development and Sourcing Strategy
1. Literature Review:

    - Reviewed existing research papers and datasets on scene understanding, object detection, and activity recognition.
    - Analyzed common categories and phrases used in these studies.

1. Datasets:

    - Leveraged well-known datasets such as ImageNet (for basic objects), COCO (for objects and simple interactions), and AVA (for complex interactions and activities).
    - These datasets provide a comprehensive set of labels that are commonly used in image analysis tasks.

1. Domain Knowledge:

    - Applied common sense and domain knowledge about everyday activities and environments.
    - Included phrases that represent typical human activities and common scenes encountered in daily life.

1. Iteration and Refinement:

    - Iteratively refined the list of phrases by testing with various images and adjusting based on the accuracy and comprehensiveness of the results.
    - Ensured that the chosen phrases covered a wide range of possible scenes without being too specific or too general.

## Examples of Descriptive Phrases and Their Utility
- Basic Objects:

    - "dog": Essential for recognizing pets and inferring activities like "playing fetch".
    - "car": Crucial for understanding scenes related to transportation or urban environments.
    - "person": Fundamental for almost all human-related activities and interactions.

- Interactions:

    - "playing fetch": Specific enough to identify a common activity involving dogs and humans.
    - "driving": Important for transportation-related themes and contexts.
    - "walking": A versatile interaction that can fit into various thematic contexts like "urban environment" or "outdoor exercise".

- Thematic Contexts:

    - "leisure time in a park": Captures a broad scenario involving multiple objects and interactions (e.g., people, dogs, trees, playing fetch).
    - "morning commute": Useful for scenes involving transportation, people in work attire, and urban settings.
    - "outdoor exercise": Encompasses various interactions like walking, jogging, and exercising, providing a clear context for fitness-related activities.

By structuring the descriptive phrases in a hierarchical manner and sourcing them from robust datasets and domain knowledge, the script can effectively analyze images and infer the likely activities and themes, providing a comprehensive scene understanding.

---

# Discuss the strategy used to layer the analysis from basic objects to thematic contexts.

1. Object Detection and Recognition
    - Purpose: The initial layer focuses on identifying and recognizing basic objects present in the scene.
    - Strategy:
        - Utilize object detection techniques to identify common objects such as people, animals, vehicles, and other relevant items.
        - Leverage pre-trained models or frameworks like YOLO, SSD, or Faster R-CNN for efficient and accurate object detection.
        - Extract features or embeddings representing detected objects to facilitate subsequent analysis.
1. Interaction Inference
    - Purpose: Once basic objects are identified, the next layer infers possible interactions or activities involving these objects.
    - Strategy:
        - Analyze spatial relationships between objects to infer potential interactions. For example, if a person is holding a ball and a dog is nearby, it suggests a possible interaction like "playing fetch".
        - Utilize contextual information and common sense to deduce likely activities based on the detected objects. For instance, if a person is seated in a car, it implies the activity of "driving".
        - Apply pre-defined sets of descriptive phrases representing common interactions to match against the detected objects and spatial arrangements.
1. Thematic Context Deduction
    - Purpose: The final layer deduces the broader thematic context or scenario in which the detected objects and interactions occur.
    - Strategy:
        - Integrate information from the previous layers to infer the overarching theme or context of the scene.
        - Consider the combination of detected objects, inferred interactions, and additional contextual cues (e.g., scene background, lighting conditions) to deduce thematic context.
        - Use domain-specific knowledge and heuristics to interpret the scene in a broader context. For example, if the detected objects and interactions suggest a gathering of people in an outdoor setting, it may indicate a "picnic" or "leisure time in a park" thematic context.
        - Apply predefined sets of descriptive phrases representing thematic contexts to match against the inferred interactions and detected objects, refining the interpretation based on the most likely thematic scenario.

### Integration and Optimization
- Layered Approach: Each layer builds upon the insights gained from the previous layers, leading to a progressively deeper understanding of the scene.
- Optimization: The analysis is optimized for efficiency and accuracy by leveraging pre-trained models, feature extraction techniques, and heuristic rules.
- Weighted Scoring: A weighted scoring system may be applied to prioritize certain objects, interactions, or thematic contexts based on their importance and relevance to the overall scene interpretation.
- Iterative Refinement: The analysis may involve iterative refinement and validation steps to improve accuracy and robustness, incorporating feedback from testing on diverse datasets and real-world scenarios.

### Conclusion
The strategy of layering the analysis from basic objects to thematic contexts ensures a systematic and comprehensive approach to scene understanding. By progressing through these layers, the script can accurately interpret the scene depicted in an image, providing valuable insights into the activities, interactions, and broader contextual information conveyed within the visual content.





