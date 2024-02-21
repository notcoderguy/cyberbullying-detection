# Cyberbullying Detection API

## !! ARCHIVE !!

This repo is a public archive now, further development will be done on new repo [nirodh](https://github.com/notcoderguy/nirodh).

## Overview

The Cyberbullying Detection API is a fast and efficient tool for detecting instances of cyberbullying in text. It provides a simple endpoint `/analyse` where you can submit text, and it will respond with a classification indicating whether cyberbullying is detected and the type of cyberbullying if applicable.

## Table of Contents

- <a href="#endpoint">Endpoint</a>
- <a href="#how-to-use">How to Use</a>
- <a href="#response">Response</a>
- <a href="#planned-roadmap">Planned Roadmap</a>

## Endpoint

### `/analyse`

This is the main endpoint of the API for analyzing text data for cyberbullying. Users can post a JSON object with the text they want to analyze.

<strong>HTTP Method:</strong> POST

<strong>Request Format:</strong>

<pre><code>{
    "text": "Women are meant in kitchen."
}
</code></pre>

<strong>Response Format:</strong>

<pre><code>{
    "status": 1,
    "message": "Cyberbullying on the basis of gender is detected.",
    "label": "gender"
}
</code></pre>

## How to Use

1. <strong>Clone the Repository:</strong>
<pre><code>git clone &lt;repository-url&gt;
</code></pre>

2. <strong>Install Dependencies:</strong>
<pre><code>pip install -r requirements.txt
</code></pre>

3. <strong>Run the API:</strong>
<pre><code>uvicorn main:app --host 0.0.0.0 --port 8000 --reload
</code></pre>

4. <strong>Make POST Requests:</strong>
- Send a POST request to <code>http://localhost:8000/analyse</code> with the JSON payload containing the text you want to analyze.

### Response

The API response will contain the following fields:

- <strong>status</strong>: An integer indicating the status of the analysis. <code>1</code> indicates cyberbullying is detected, <code>0</code> means no cyberbullying is detected.
- <strong>message</strong>: A message describing the analysis result.
- <strong>label</strong>: If cyberbullying is detected, this field specifies the type of cyberbullying detected.

### Planned Roadmap

- [ ] <strong>Data Logging and Feedback Mechanism:</strong> Implement a data logging system and a feedback mechanism to collect user-generated data and feedback for model refinement (as discussed earlier).

- [ ] <strong>Image Analysis:</strong> Extend the API to support image analysis for detecting cyberbullying in images. Users should be able to submit images for analysis.

- [ ] <strong>Multilingual Support:</strong> Add support for multiple languages to make the API more versatile and accessible.

- [ ] <strong>User Authentication:</strong> Implement user authentication to track and analyze usage patterns, which can help improve the service over time.

- [ ] <strong>Model Fine-tuning:</strong> Continuously update and fine-tune the model with new data to enhance its accuracy and effectiveness.

- [ ] <strong>Documentation:</strong> Expand and improve the API documentation to make it more user-friendly and informative.

- [ ] <strong>Scalability:</strong> Ensure the API can handle a growing number of requests by optimizing its performance and potentially deploying it on a scalable infrastructure.
