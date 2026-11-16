# autOBS

A lightweight Python tool that turns OBS Studio into a local web API server so you can control your scenes, recording, and camera inputs using numbers.

AutOBS is designed to connect to numerous different sources, and centralize them. This is helpful for large livestreams. AutOBS will be getting combined with the project [churchswap](https://github.com/occiinnovations/churchswap) to form 'Nodary'.

## File Directory

```text
Nodary/
├── src/
│   ├── obs_module/
│   │   ├── __init__.py
│   │   ├── obs_controls.py
│   │   └── obs_stuff.py
│   ├── main.py
│   └── test.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How it Works

The program runs a server using FastAPI. When another script (terminal input, eventlistener, etc) sends a single number to the server, it verifies if the integer is in a specific module dictionary (for now OBS), and runs the associated function.

## Example

```python

OBS_CONTROL_DICT = {
   ...

    6: requests.StartRecord(),
    7: requests.StopRecord(),

    8: requests.SetCurrentProgramScene(sceneName="Scene"),
    9: requests.SetCurrentProgramScene(sceneName="Scene 2"),

    ...
}

```

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
