from pyngrok import ngrok
import signal
ngrok.set_auth_token("31PIVUUImUOcfEfnvDg7VtTlDmb_4KSxGwbjT138krGZReDNB")

listener = ngrok.connect(
    addr="localhost:3000",
    metadata="example listener metadata from python",
)
print(f"Please click on the text below {listener}")
print("Tunnel is running. Press Ctrl+C to stop.")
try:
    signal.pause()
except KeyboardInterrupt:
    print("Shutting down tunnel.")
finally:
    ngrok.kill()