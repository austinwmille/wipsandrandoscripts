# this script has a block of code missing from line 7

import boto3
import os

# Configure AWS Polly with your credentials
pol..ace with y


# Create an audio output directory if it doesn't exist
os.makedirs("audio_outputs", exist_ok=True)

# Iterate through text files in the `tifu_posts` folder
for filename in os.listdir("tifu_posts"):
    if filename.endswith(".txt"):
        with open(f"tifu_posts/{filename}", "r", encoding="utf-8") as file:
            lines = file.readlines()
            content = ''.join(lines[4:])  # Skip title and metadata lines

        # Generate TTS audio with Amazon Polly
        response = polly_client.synthesize_speech(
            Text=content,
            OutputFormat="mp3",
            VoiceId="Matthew"  # Choose a voice like "Joanna" or "Matthew" for a natural tone
        )

        # Save the audio stream to a file
        audio_filename = f"audio_outputs/{filename.replace('.txt', '.mp3')}"
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(response["AudioStream"].read())
        print(f"Voiceover saved as {audio_filename}")
