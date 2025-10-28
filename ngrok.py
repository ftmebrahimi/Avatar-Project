from pyngrok import ngrok
import signal

ngrok.set_auth_token("your ngrok api token")
listener = ngrok.connect(
    addr="localhost:3000",
    metadata="avatar agent public url",
)
print(f"Please click on the text below {listener}")
print("Tunnel is running. Press Ctrl+C to stop.")
try:
    signal.pause()
except KeyboardInterrupt:
    print("Shutting down tunnel.")
finally:
    ngrok.kill()
