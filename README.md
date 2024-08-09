This project is an emotion detection from user text. the model is trained with [Google's Goemotions dataset](https://github.com/google-research/google-research/tree/master/goemotions).

The Google GoEmotions dataset is a large-scale, fine-grained for emotion classification in text, developed by Google Research. It contains over 58009 English Reddit comments that have been annotated for 27 emotion categories and a 'neutral' category. The emotions include common ones like 'joy', 'sadness', and 'anger' as well as more nuanced emotions such as 'admiration', 'caring', and 'embarrassment'. This project focuses on training and evaluating the trained model to understand emotional expression in text.

## Build the Docker Image
To build the Docker image, ensure the working directory contains the 'dockerfile' and run the following command in the terminal.

```
docker build -t emotion-detection-app .
```

## Run the Docker Container
To run the docker image, run the following command:

```
docker run -p 8501:8501 emotion-detection-app
```

This maps port 8501 on the local machine to port 850 in the Docker container, where Streamlit serves the app.
