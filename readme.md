# Azure AI Services - Computer Vision OCR Streamlit App

A simple Streamlit application that utilizes the Azure Computer Vision API to perform Optical Character Recognition (OCR) on images.

## Table of Contents
- [How it Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the App](#running-the-app)
- [Usage](#usage)

## How it Works

This is a simple Streamlit app that uses the `Azure Computer Vision API` to perform OCR on an image.
The documentation for the Azure Computer Vision API can be found [here](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview-ocr).

The app allows you to upload an image, and then it sends the image to the Azure Computer Vision API to perform OCR. The app then displays the extracted text.

![](resource/screenshot.png)

## Prerequisites

- An active Azure account. If you don't have one, you can create a [free Azure account](https://azure.microsoft.com/free/).
- An Azure AI services multi-service account.

## Setup

1.  **Get Azure Credentials**:
    *   Navigate to your Azure AI services resource in the Azure portal.
    *   Under `Resource Management`, select `Keys and Endpoint`.
    *   Copy the `Endpoint` and one of the `Keys` (Subscription Key).
2.  **Configure the Application**:
    *   Open the `main.py` file.
    *   Replace `<YOUR_vision_base_url>` with your Azure Computer Vision API endpoint.
    *   Replace `<YOUR_subscription_key>` with your Azure Computer Vision API subscription key.

## Running the App

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the following command:
```bash
streamlit run main.py
```

## Usage

1.  Go to `http://localhost:8501` in your web browser.
2.  Upload an image file containing text using the file uploader.
3.  Click the 'Analyze' button.
4.  The OCR results (extracted text) will be displayed below the image.
