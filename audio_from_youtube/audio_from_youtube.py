#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Source: twitter
Purpose: Transcribe audio from Youtube (Not Working)
Require package: 
    - pytube
    - whisper (pip install git+https://github.com/openai/whisper.git)
"""

import argparse

import pytube
import whisper


# --------------------------------------------------
def get_args():
    """Get Youtube URL and output file name from user input"""
    parser = argparse.ArgumentParser(
        description = 'Transcribe audio from Youtube (Not Working)',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'url', 
        metavar = 'Youtube URL',
        default = '',
        help = "Complete Youtube URL as string",
        type=str)

    parser.add_argument(
        '-a', '--audio', 
        metavar = 'Audio file name', 
        default = 'tmp.mp4',
        help = "Audio's file name with extension",
        type = str)

    parser.add_argument(
        '-o', '--output', 
        metavar = 'txt_name', 
        default = 'output.txt',
        help = "txt's file name with extension",
        type = str)

    return parser.parse_args()

# -------------------------------------------
def get_youtube_video(url: str):
    """Get Youtube video from url"""
    video = pytube.YouTube(url)
    return video

# -------------------------------------------
def get_youtube_audio(youtube_video, 
audio_file: str = 'tmp.mp4'):
    """Get Youtube audio from video"""
    audio = youtube_video.streams.get_audio_only()
    audio.download(filename = audio_file)
    return audio

# -------------------------------------------
def transcribe_audio(audio_file: str = 'tmp.mp4'):
    """Get text from audio"""
    model = whisper.load_model('small')
    text = model.transcribe(audio_file)
    return text

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    video = get_youtube_video(args.url)
    get_youtube_audio(video, args.audio)
    text = transcribe_audio(args.audio)
    print(text['text'])

# --------------------------------------------------
if __name__ == '__main__':
    main()
    #python audio_from_youtube.py "https://"