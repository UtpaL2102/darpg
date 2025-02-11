# Fine-tuning Open Source Whisper (Speech-to-Text) Model

## Overview
For the **DARPG Hackathon 2024**, **Problem Statement 3** involved evaluating and optimizing an Open Source speech-to-text model to accurately transcribe feedback calls related to citizen grievances into English text.

Since the textual output data was not provided, **Whisper LLM** was used to generate textual data for each audio dataset. This data was then stored in a `metadata.csv` file and, after preprocessing, was used to fine-tune the **Whisper Small LLM**.

### Project Explanation Video
Here's a YouTube video explaining our project: [Watch our project explanation on YouTube](https://youtu.be/qPTS3mdLkAY?si=SXOdFyvT-Hlq8QqY)

---
## Dataset Preparation
Prepare your **Audio** folder in the following format:

```
audio_dataset/
├── metadata.csv
└── data/
```

- **`metadata.csv`** contains the names of the audio files, their `audio_path`, and their corresponding transcriptions.
- **`data/`** folder contains all the audio files.

---
## Hackathon Workflow
### These are all the steps we followed during the hackathon:

![Workflow Diagram](./image.png)

### Steps:
1. **Data Collection**
   - Gathered Hindi, English, and Hinglish audio datasets based on customer grievances.
   - Segmented long feedback calls into smaller 30-second intervals.
   - Converted audio files to the same format (**MP3**/**WAV**).

2. **Generation of Textual Data**
   - Used **Whisper Large v2** (1.5 billion parameters) to generate transcriptions.
   - Transcriptions were stored in a CSV file, ensuring alignment with audio timestamps.

3. **CSV Data Pre-Processing**
   - **Audio Resampling**: Converted audio to **16kHz** to match Whisper’s input requirements.
   - **Data Cleaning**: Removed noise, punctuation, irrelevant words, and rephrased text.
   - **Trimming**: Ensured transcriptions fit within Whisper’s **448-token limit**.
   - **Alignment**: Verified that text labels matched audio timestamps.

4. **Fine-tuning Whisper Small**
   - Used the preprocessed CSV dataset to train the **Whisper Small** model (**245M parameters**).
   - Adjusted tokenization to improve **Hinglish transcription**.
   - Saved checkpoints for deployment.

5. **Evaluation & Benchmarking**
   - **Training Loss:** **0.02** (After 3600 steps)
   - **Validation Loss:** **0.72**
   - **WER:** **73%** (Aligned with Whisper Small’s benchmark WER from Hugging Face)
   - Compared our fine-tuned model's performance against baseline Whisper models.

6. **Deployment & UI Integration**
   - Integrated the fine-tuned model into a **Gradio UI** for user-friendly interaction.
   - Users can upload audio files and receive transcriptions in **real time**.
   - Supports Hindi, English, and Hinglish input.

---
## Deployment
We have deployed this model on **Hugging Face Spaces** for easy access and usage. You can try it out here:

👉 **[WHISPER-SPEECH-TO-TEXT-MODEL-FOR-DARPG](https://huggingface.co/spaces/sanket003/WHISPER-SPEECH-TO-TEXT-MODEL-FOR-DARPG)**

---
## Using the Model Locally
To use the model locally, run the `run_model.py` script, which contains a **Gradio interface** for easy interaction with the model.

```bash
python run_model.py
```

---
### Results: WER per Iteration
| Step  | Training Loss | Validation Loss | WER    |
|-------|--------------|----------------|--------|
| 200   | 0.902800     | 0.843902       | 90.673 |
| 400   | 0.446000     | 0.556607       | 92.189 |
| 600   | 0.178900     | 0.553851       | 86.706 |
| 800   | 0.062500     | 0.640933       | 83.893 |
| 1000  | 0.023100     | 0.716296       | 85.017 |

---
## Contributors
- **[Sanket Poojary]** - *Lead Developer*
- **[Priyadarshi Uttpal]** - *Lead Developer*

For inquiries, contact us at **[priyadarshiutpal06@gmail.com](mailto:priyadarshiutpal06@gmail.com)**

---
### License
This project is licensed under the **MIT License** - see the `LICENSE` file for details.

---
Thank you for checking out our project! 🚀

