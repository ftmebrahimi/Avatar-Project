import logging
import os

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    WorkerType,
    cli,
)
from livekit.plugins import openai, simli,silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.agents import JobProcess

logger = logging.getLogger("simli-avatar-example")
logger.setLevel(logging.INFO)

load_dotenv(override=True)

def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: JobContext):
    session = AgentSession(
        vad=ctx.proc.userdata["vad"],
        stt=openai.STT(
        model="whisper-large-v3-turbo",
        base_url="https://api.groq.com/openai/v1",
        language="en",
        api_key="your api key",
        ),
        llm=openai.LLM(model= "llama-3.1-8b-instant", base_url = 'https://api.groq.com/openai/v1',
         api_key = "your api key"),
        tts=openai.TTS(model="playai-tts", 
        base_url = 'https://api.groq.com/openai/v1',
        voice="Judy-PlayAI",
        api_key="your api key",),
        turn_detection=MultilingualModel(),
    )
    

    simliAPIKey = "your simliAPIKey"
    simliFaceID = "4cce0ca0-550f-42d8-b500-834ffb35e0af"

    simli_avatar = simli.AvatarSession(
        simli_config=simli.SimliConfig(
            api_key=simliAPIKey,
            face_id=simliFaceID,
        ),
    )
    await simli_avatar.start(session, room=ctx.room)

    # start the agent, it will join the room and wait for the avatar to join
    await session.start(
        agent=Agent(instructions="Talk to me! just answer in less than four short sentences"),
        room=ctx.room,
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
