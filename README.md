# Multi class classifier model for media tags
This model forms part of the web app I created for the Qloo LLM Hackathon. It receives formated tags from media entities and clasiffies them to narrative components such as characters, genres, subgenres...

## Dataset
- Source: The model was trained with around 450 labeled tags from the Qloo api taste usage and related entity tags. 
- Description: It is a combination from movies, books and tv_shows, and cross domain entities like artists and destinations. Here an example with base format: "urn:tag:keyword:media": "dragonfly"
- Preprocessing: The tags were formated to match a format like "keyword:media:dragonfly", mainting the type,source and value. 

## Model
- Type of model: The initial model relies on the pretrained DistilBERT. Semi-supervised Learning was employed. 

## Training 
- Hardware: Training was performed on a GPU (T4) on Google Colab.
- Training Time: Approximately 50 minutes.
  
## Evaluation
Overall accuracy of around 74

## Usage 
The model can classify tags suchs as" wildlife" as part of the topics of a narrative, "child in forest" as a story's character...
