# Nodary

Nodary is a modular Python tool that uses a local API server to control your applications such as Webots and OBS in one spot using a variety of inputs.

This repo is designed to connect to a large amount of applications and connect them in one place. This is helpful for livestreams, repetitive simulation tests, and desktop automation tasks.

Nodary will soon be having the project [churchswap](https://github.com/occiinnovations/churchswap) integrated to a module, in which YOLO will be able to act as an input source.

## File Directory

```text
Nodary/
│
├── .github/
├── docs/
│   └── masterkey.md               # integer opcode reference key
│
├── src/
│   ├── lm_studio_module/
│   │   └── mvp_connect.py         # MCP 
│   │
│   ├── obs_module/
│   │   ├── __init__.py
│   │   ├── obs_controls.py        # dictionary of controls from OBS
│   │   └── obs_stuff.py           # OBS helper functions
│   │
│   ├── pyautogui_module/
│   │   ├── __init__.py
│   │   └── keyboard_auto.py       # dictionary of PyAutoGUI keyboard & hotkey controls
│   │
│   ├── webots_module/
│   │   ├── __init__.py
│   │   ├── webots_controls.py     # dictionary of Webots function integers
│   │   └── webots_functions.py    # Webots functions 
│   │
│   ├── main.py                    # central FastAPI control server
│   └─ test.py                     # manual integer input 
│
├── .env                           # Create your own .env after cloning
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How it Works

The program runs a server using FastAPI. When another script (terminal input, eventlistener, etc) sends a single number to the server, it verifies if the integer is in a specific module dictionary and runs the associated function.

## Quick Start

1. Download dependencies:

   ```bash
   python -m pip install requirements.txt
   ```
   
2. Enable the WebSocket server in OBS (Tools -> WebSocket Server Settings) on port `4454`.
3. Run your server file:

   ```bash
   python src/main.py
   ```

4. Run the test script in a second terminal to trigger commands with keyboard integers:

   ```bash
   python src/test.py
   ```

Add the following entry to your client's `mcp.json` / `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nodary": {
      "command": "python",
      "cwd": "/path/to/Nodary",
      "args": ["src/lm_studio_module/mvp_connect.py"]
    }
  }
}
```

Once it is added, run this:

   ```bash
   python src/lm_studio_module/mvp_connect.py
   ```

### Example

```python
OBS_CONTROL_DICT = {
    4: lambda client: client.connect(),
    5: lambda client: client.disconnect(),

    6: requests.StartRecord(),
    7: requests.StopRecord(),

    8: requests.SetCurrentProgramScene(sceneName="Scene"),
    9: requests.SetCurrentProgramScene(sceneName="Scene 2"),

    10: obs_stuff.OBSscenes,  # Custom Function created to easily display all scenes in detail using GetSceneList() underneath
    ...
}
```

## License

This project is licensed under the **MIT License**. see the [LICENSE](LICENSE) file for details.
