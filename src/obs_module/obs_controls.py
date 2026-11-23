from obswebsocket import obsws, requests
from obs_module import obs_stuff

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
    15: requests.StopVirtualCam(),
    16: requests.StartVirtualCam(),

    17: requests.StartStream(),
    18: requests.StopStream(),

    19: requests.PauseRecord(),
    20: requests.ResumeRecord()
}
