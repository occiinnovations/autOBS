from obswebsocket import obsws, requests
from obs_module import obs_stuff

obs_client = obsws("127.0.0.1", 4455, "YOUR_PASSWORD")

OBS_CONTROL_DICT = {
    4: lambda client: client.connect(),
    5: lambda client: client.disconnect(),

    6: requests.StartRecord(),
    7: requests.StopRecord(),

    8: requests.SetCurrentProgramScene(sceneName="Scene"),
    9: requests.SetCurrentProgramScene(sceneName="Scene 2"),

    10: obs_stuff.OBSscenes,

    11: requests.SetCurrentPreviewScene(sceneName="Scene 1"),
    12: requests.SetCurrentPreviewScene(sceneName="Scene 2"),

    13: requests.TriggerStudioModeTransition(),

    14: requests.ToggleVirtualCam(),
}
