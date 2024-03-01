Using the Whisper Large v3 model with its 1.5 billion parameters, we transcribed the audio segments and generated our own Textual Dataset.
With the generated textual dataset in hand, we then fine-tuned the Whisper Small model, which boasts 245 million parameters. Despite its resource-friendly architecture, the Whisper Small model demonstrated exceptional accuracy in transcriptions.


| Step  | Training Loss | Validation Loss | WER      |
|-------|----------------|------------------|----------|
| 200   | 0.902800       | 0.843902         | 90.673   |
| 400   | 0.446000       | 0.556607         | 92.189   |
| 600   | 0.178900       | 0.553851         | 86.706   |
| 800   | 0.062500       | 0.640933         | 83.893   |
| 1000  | 0.023100       | 0.716296         | 85.017   |


To See our working Model run the app.ipynb file on google colab
