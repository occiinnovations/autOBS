# autOBS

A lightweight Python tool that turns OBS Studio into a local web API server so you can control your scenes, recording, and camera inputs using numbers.

## How it Works
The script runs a fast local server using FastAPI. When another script (like a computer vision loop or a hardware controller) sends a single number to the server, it instantly fires the matching action inside OBS via WebSockets.

* **Number 1**: Start Recording
* **Number 2**: Stop Recording
* **Number 3**: Switch to Scene 1
* **Number 4**: Switch to Scene 2

## Scaling Strategy
Instead of keeping 15 different cameras constantly streaming and destroying your computer's USB bus bandwidth or CPU, this setup uses a demand-driven approach: it disables the camera streams when they aren't actively being watched, allowing a heavy multi-camera grid to run safely on a standard machine.

## Quick Start
1. Enable the WebSocket server in OBS (Tools -> WebSocket Server Settings) on port `4454`.
2. Run your server file:
   ```bash
   python main.py
   ```
3. Run your interactive test script in a second terminal to trigger commands with raw integers:
   ```bash
   python test.py
   ```
