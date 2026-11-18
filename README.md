# autOBS

A lightweight Python tool that turns OBS Studio into a local web API server so you can control your scenes, recording, and camera inputs using numbers.

AutOBS is designed to connect to numerous different sources, and centralize them. This is helpful for large livestreams. AutOBS will be getting combined with the project [churchswap](https://github.com/occiinnovations/churchswap) to form 'Nodary'.

## File Directory

```text
Nodary/
│
├── docs/
│   └── masterkey.md          # integer opcode reference key for AI agents
│
├── src/
│   ├── lm_studio_module/
│   │   └── mvp_connect.py    # MCP server bridging LM Studio / agents to FastAPI
│   │
│   ├── obs_module/
│   │   ├── __init__.py
│   │   ├── obs_controls.py   # dictionary of controls from OBS
│   │   └── obs_stuff.py      # OBS connection & scene helper functions
│   │
│   ├── main.py               # central FastAPI control server
│   └── test.py               # manual CLI script for terminal integer input
│
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How it Works

The program runs a server using FastAPI. When another script (terminal input, eventlistener, etc) sends a single number to the server, it verifies if the integer is in a specific module dictionary (for now OBS), and runs the associated function.

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

## Quick Start

1. Enable the WebSocket server in OBS (Tools -> WebSocket Server Settings) on port `4454`.
2. Run your server file:

   ```bash
   python src/main.py
   ```

3. Run the test script in a second terminal to trigger commands with keyboard integers:

   ```bash
   python src/test.py
   ```

### Connect Your MCP Client (LM Studio or Claude Desktop)

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

## License

This project is licensed under the **MIT License**. see the [LICENSE](LICENSE) file for details.
