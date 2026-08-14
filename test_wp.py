# test_wp.py
import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from WPP_Whatsapp import Create

def catchgenqr(qrCode, asciiQR, attempt, urlCode):
    print("QR received, attempt:", attempt)
    print("QR Code:", qrCode[:50] if qrCode else "None")

creator = Create(session="clinical", catchQR=catchgenqr, logQR=True)
client = creator.start()

if creator.state == 'CONNECTED':
    print("Connected!")
else:
    print("State:", creator.state)