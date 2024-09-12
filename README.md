
# Movie Recommendation System - Content-Based Filtering



# Overview

This project is a Content-Based Filtering Movie Recommendation System that suggests movies similar to a given movie based on its content. The system processes raw movie data, converts it into a structured format, and then uses  vectorization techniques to provide recommendations.

# Features

# Content-Based Filtering
Recommends movies similar to a selected movie by analyzing the content of the movies.

# Data Preprocessing
Raw data is cleaned and transformed into meaningful data using advanced data processing techniques.
# Text Processing
Utilizes NLTK's Porter Stemmer to remove similar words, enhancing the accuracy of recommendations.

# Vectorization
Converts movie descriptions into vectors, enabling the calculation of cosine similarities between movies.

# Top-N Recommendations
The system returns the top 5 closest movies based on the cosine similarity score.



# Libraries and Tools Used
Python: Core programming language for the project.

Pandas: Used for data manipulation and transformation.

Scikit-learn: Provides tools for vectorization and calculating cosine similarity.

NLTK (Natural Language Toolkit): Used for text processing, particularly with the 
Porter Stemmer to standardize similar words.

Jupyter Notebook: For interactive development and documentation.
