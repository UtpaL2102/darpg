import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import gradio as gr
model_id = "sanket003/whisper-for-darpg"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch.float32, low_cpu_mem_usage=False, use_safetensors=True
)
processor = AutoProcessor.from_pretrained(model_id)
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch.float32,
    generate_kwargs={"language": "english","task":"translate"},
    return_timestamps= True
)

def transcribe_audio(audio, file):
    if audio:
        result = pipe(audio)
    elif file:
        result = pipe(file)
        pass
    else:
        result = {"text": "No input provided."}
    return result["text"]

iface = gr.Interface(
    title="DARPG WHISPER MODEL",
    fn=transcribe_audio,
    inputs=[
        gr.Audio(sources="microphone", type="filepath", label="Record from Microphone"),
        gr.File(type="filepath", label="Upload Audio File"),
    ],
    outputs=["textbox"],
    description="Choose either microphone input or upload an audio file.",
)
iface.launch(share=True)
