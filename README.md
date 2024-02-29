Our Solution aims to optimize and enhance an existing open-source speech-to-text transcription Model named Whisper large v3 specifically tailored for accurately converting citizen feedback calls related to grievances into English text. Focusing on the Whisper model, we undertake a multi-step approach to improve transcription accuracy for calls in Hindi, English, and Hinglish. 
The project involves  segmenting audio files into 30-second intervals, utilizing the Whisper Large/V3 API for Transcription. 

The provided hackathon dataset available on the Website solely consisted of audio recordings, lacking the crucial textual 
data necessary for training. To overcome this, we employed the powerful Whisper Large v3 model with its 1.5 billion 
parameters. This model, renowned for its speech-to-text capabilities, generated the missing textual data by transcribing 
the audio segments and cleaning the resulting textual dataset. 

Our approach involved segmenting the audio files into 30-second intervals for efficient processing Since Whisper Small 
variant, is designed to process relatively short sequences of audio input and By segmenting the audio into 30-second 
intervals, we align with the model's architecture and its ability to handle shorter audio sequences effectively.

With the generated textual dataset in hand, we fine-tuned the Whisper Small model, which, despite its resource-friendly 245 
million parameters, demonstrated exceptional accuracy in transcriptions. The goal was to refine this model for precise transcriptions 
and accurate responses to citizen feedback. 

We then fine-tune the Whisper Small model using this cleaned dataset, enhancing its performance and 
accuracy. 

To facilitate user interaction and evaluation, we integrated a Gradio UI, providing a convenient interface for testing the
model's performance

By leveraging cutting-edge technologies like AI and ML, we strive to deliver a disruptive and citizen-centric solution for
efficient and accurate transcription of diverse feedback calls, addressing real-world challenges in citizen service
management.
 
The resulting system not only addresses the specific challenges in citizen service management but also showcases the 
potential of AI and ML technologies in public service domains. The final output is a functional prototype capable of handling feedback 
calls in Hindi, English, and Hinglish, offering improved efficiency, usability, and accuracy.



