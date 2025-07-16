📚 Audiobook Generator – Documentation
======================================

Turn your Markdown book chapters into high-quality audiobooks using flexible text-to-speech engines like **ElevenLabs**,
**gTTS**, or **pyttsx3**.  
This project is ideal for authors who want to **self-publish audiobooks** from existing `.md` files with minimal effort.

* * *

🚀 Features
-----------

* ✅ Convert chapters in `.md` format to `.mp3` files

* ✅ Choose between multiple TTS engines: `google`, `pyttsx3`, `elevenlabs`

* ✅ Language and voice configurable

* ✅ Automatically cleans Markdown syntax for natural narration

* ✅ Works with Poetry & CLI

* ✅ Ready for integration with Findaway Voices, Spotify Audiobooks, Google Play Books

* * *

📁 Project Structure
--------------------

```text
scripts/
├── generate_audiobook.py        # Main script with CLI
├── tts/
│   ├── base.py                  # Abstract TTSAdapter interface
│   ├── pyttsx3_adapter.py       # Offline voice (robotic)
│   ├── gtts_adapter.py          # Google TTS
│   └── elevenlabs_adapter.py    # ElevenLabs neural voices
```

* * *

⚙️ Installation
---------------

1. **Clone the repository**

```bash
git clone https://github.com/your-user/your-repo.git
cd your-repo
```

2. **Install dependencies with Poetry**

```bash
poetry install
```

3. **(Optional) Set your ElevenLabs API key**

```bash
export ELEVENLABS_API_KEY=your-api-key
```

* * *

🧠 How It Works
---------------

1. You place your book chapters as `.md` files in a folder (e.g., `manuscript/en/`)

2. The system:

    * Cleans the Markdown

    * Removes images, links, code blocks, etc.

    * Converts the plain text to `.mp3` using the selected TTS engine

3. You get an audiobook folder with clean `.mp3` files for each chapter

* * *

🧼 Markdown Cleanup Details
---------------------------

Before generating audio, the text is automatically cleaned to ensure a natural listening experience:

* ✅ Removes images (`![alt](url)`)

* ✅ Converts links (`[text](url)` → `text`)

* ✅ Strips bold/italic, headings, code blocks, tables

* ✅ Removes HTML tags

* ✅ Reduces multiple blank lines

* * *

🖥️ Usage Example
-----------------

### 🔊 Generate audiobook using ElevenLabs

```bash
poetry run generate-audiobook \
  --input manuscript/en \
  --output audiobook/output/en \
  --engine elevenlabs \
  --voice Rachel \
  --lang en
```

### 📢 Google TTS (Free, online)

```bash
poetry run generate-audiobook \
  --input manuscript/de \
  --output audiobook/output/de \
  --engine google \
  --lang de
```

### 🖥 pyttsx3 (Offline, robotic voice)

```bash
poetry run generate-audiobook \
  --input manuscript/en \
  --output audiobook/output/en \
  --engine pyttsx3 \
  --voice "english" \
  --rate 180
```

* * *

🧩 Command-Line Options
-----------------------

| Option     | Description                                   |
|------------|-----------------------------------------------|
| `--input`  | Folder containing Markdown files              |
| `--output` | Output folder for MP3 files                   |
| `--engine` | TTS engine: `google`, `pyttsx3`, `elevenlabs` |
| `--lang`   | Language code: `en`, `de`, `es`, etc.         |
| `--voice`  | Voice name or ID (depends on engine)          |
| `--rate`   | Speech rate (used in pyttsx3 only)            |

* * *

📦 Supported TTS Engines
------------------------

| Engine       | Description                         | Internet Required | Best For                   |
|--------------|-------------------------------------|-------------------|----------------------------|
| `elevenlabs` | Studio-quality AI voices (paid API) | ✅ Yes             | 🎧 Professional audiobooks |
| `google`     | Google Translate TTS (free)         | ✅ Yes             | 📘 Casual audio drafts     |
| `pyttsx3`    | Local OS voice engine (robotic)     | ❌ No              | 🧪 Debugging, offline use  |

* * *

🛠 Tips for Publishing
----------------------

If you're publishing via **Findaway Voices**, **Google Play**, or **Spotify Audiobooks**:

* Export one `.mp3` file per chapter

* Use consistent naming like `01 - Chapter One.mp3`

* Optionally add intro/outro tracks manually

* Normalize volume with tools like `ffmpeg` or `Auphonic`

* Use `.zip` to bundle the audio for platforms that require uploads

* * *

🧪 Testing Locally
------------------

Try this dry run:

```bash
poetry run generate-audiobook \
  --input test/chapters \
  --output test/audio \
  --engine google \
  --lang en
```

Check the generated MP3s in `test/audio`.

* * *

🆘 Troubleshooting
------------------

| Problem                 | Solution                                                |
|-------------------------|---------------------------------------------------------|
| Output sounds robotic   | Use `elevenlabs` or `google` instead of `pyttsx3`       |
| ElevenLabs error        | Make sure your API key is set via `ELEVENLABS_API_KEY`  |
| TTS fails with Markdown | Make sure `.md` files contain only text and valid UTF-8 |
| Voice not recognized    | Check available voices for the engine you're using      |

* * *

📄 License
----------

This project is open source. You can use it for personal or commercial audiobook generation, but check the **TTS engine
licenses** (e.g. ElevenLabs API has usage restrictions).

* * *

🙋🏻 Need help?
---------------

Create an issue on GitHub or reach out at: `your-email@example.com`

* * *
