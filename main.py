import uvicorn
from obswebsocket import obsws, requests
from fastapi import FastAPI

obs_client = obsws("127.0.0.1", "port", "EnterOBSKey")
obs_client.connect()

nodary_main = FastAPI()
OBS_CAM_RECORD = False
OBS_CAM_STOP_RECORD = False
OBS_MONITORONE = False
OBS_MONITORTWO = False


@nodary_main.post("/{incoming_integer}")
def catch_number(incoming_integer: int):
    global OBS_CAM_RECORD, OBS_CAM_STOP_RECORD, OBS_MONITORONE, OBS_MONITORTWO

    if incoming_integer == 1:
        OBS_CAM_RECORD = True
        obs_client.call(requests.StartRecord())

    elif incoming_integer == 2:
        OBS_CAM_STOP_RECORD = True
        obs_client.call(requests.StopRecord())

    elif incoming_integer == 3:
        OBS_MONITORONE = True
        obs_client.call(requests.SetCurrentProgramScene(sceneName="Scene"))

    elif incoming_integer == 4:
        OBS_MONITORTWO = True
        obs_client.call(requests.SetCurrentProgramScene(sceneName="Scene 2"))

    else:
        print("Not gonna work bud")


uvicorn.run(nodary_main, host="127.0.0.1", port="insert_port")
