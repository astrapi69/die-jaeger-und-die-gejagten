# scripts/generate_audiobook.py
import os
import argparse
from pathlib import Path
from scripts.tts.base import TTSAdapter

# Change the current working directory to the root directory of the project
# (Assumes the script is located one level inside the project root)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

def get_tts_adapter(engine: str, lang: str, voice: str, rate: int) -> TTSAdapter:
    if engine == "google":
        from scripts.tts.gtts_adapter import GoogleTTSAdapter
        return GoogleTTSAdapter(lang=lang)
    elif engine == "pyttsx3":
        from scripts.tts.pyttsx3_adapter import Pyttsx3Adapter
        return Pyttsx3Adapter(voice=voice, rate=rate)
    elif engine == "elevenlabs":
        from scripts.tts.elevenlabs_adapter import ElevenLabsAdapter
        api_key = os.getenv("ELEVENLABS_API_KEY")
        return ElevenLabsAdapter(api_key=api_key, voice=voice, lang=lang)
    else:
        raise ValueError(f"Unsupported engine: {engine}")


def generate_audio_from_markdown(input_dir: Path, output_dir: Path, tts: TTSAdapter):
    for md_file in sorted(input_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        out_path = output_dir / f"{md_file.stem}.mp3"
        print(f"Generating: {out_path.name}")
        tts.speak(text, out_path)


def main():
    parser = argparse.ArgumentParser(description="Generate audiobook from markdown files")
    parser.add_argument("--input", type=Path, required=True, help="Input folder with markdown files")
    parser.add_argument("--output", type=Path, required=True, help="Output folder for audio files")
    parser.add_argument("--lang", type=str, default="en", help="Language code (e.g. 'en', 'de')")
    parser.add_argument("--voice", type=str, default=None, help="Voice ID or name (pyttsx3 only)")
    parser.add_argument("--rate", type=int, default=200, help="Speech rate (pyttsx3 only)")
    parser.add_argument("--engine", type=str, choices=["google", "pyttsx3"], default="google",
                        help="TTS engine to use")

    args = parser.parse_args()
    tts = get_tts_adapter(args.engine, args.lang, args.voice, args.rate)
    generate_audio_from_markdown(args.input, args.output, tts)
