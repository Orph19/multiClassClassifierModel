# Multi class classifier model for media tags
This model forms part of the web app I created for the Qloo LLM Hackathon. It receives formatted tags from media entities and classifies them into narrative components such as characters, genres, subgenres...

## Model and Dataset
- Model Type: The initial model is based on the pre-trained DistilBERT architecture, and semi-supervised learning was used for training.
- Training Data: The model was trained on approximately 450 labeled tags from the Qloo API, including taste usage and related entities.
- Data Description: The dataset is a combination of tags from movies, books, TV shows, and cross-domain entities like artists and destinations. A base format example is: "urn:tag:keyword:media": "dragonfly".
- Preprocessing: Tags were preprocessed into a format like "keyword:media:dragonfly", which maintains the tag's type, source, and value.
  
## Training and Evaluation
- Hardware: Training was performed on a GPU (T4) on Google Colab.
- Training Time: Approximately 40 minutes.
- Overall accuracy of around 74

## Usage
This model can classify tags into narrative components. For example, it can identify "wildlife" as a topic of a narrative and "child in forest" as a character. You can find a complete list of all the categories in the int_to_category.json file.

## Local Installation
1. Install Python dependencies: 
Navigate to the project directory in your terminal and install the required packages.
```
pip install -r requirements.txt
```
2. Run the local server:
Execute the app.py file to start the server. This will make the tag classification model available to receive requests.

©2025 Orph19. All Rights Reserved.
