# Avatar Agent (LiveKit + Simli + Groq Integration)

This project demonstrates how to create a **real-time AI-powered talking avatar** using [LiveKit Agents](https://github.com/livekit/agents), [Simli](https://simli.ai/), and Groq-hosted OpenAI-compatible APIs.

The avatar listens, thinks, and responds naturally with speech, using the following components:

-  **Speech-to-Text (STT)** — Whisper Large V3 Turbo (via Groq API)  
-  **Language Model (LLM)** — Llama 3.1 8B Instant (Groq API)  
-  **Text-to-Speech (TTS)** — PlayAI TTS Voice  
-  **Voice Activity Detection (VAD)** — Silero  
-  **Avatar Rendering** — Simli  

The `avatar_agent.py` script connects all these modules into a single interactive AI experience, while `ngrok.py` creates a public tunnel to make your local avatar accessible from anywhere.

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the Avatar Agent locally.

### 1️⃣ Install Python Dependencies

First, install all required Python packages:
pip install -r requirements.txt

### 2️⃣ Clone and Run LiveKit Agents Playground

git clone https://github.com/livekit/agents-playground.git
cd agents-playground
npm install
npm run dev

### 3️⃣ Run the Avatar Agent

python avatar_agent.py download-files
python avatar_agent.py start

***Before running, open avatar_agent.py and replace the empty API key fields with your own credentials.
### 4️⃣ Start ngrok Tunnel
python ngrok.py

Once started, ngrok will print a public URL similar to:
Please click on the text below http://xxxx-xx-xx-xx.ngrok.io
Tunnel is running. Press Ctrl+C to stop.
Use that URL to access or share your live avatar demo.
