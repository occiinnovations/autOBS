import uvicorn
from obswebsocket import obsws, requests
from fastapi import FastAPI

obs_client = obsws("127.0.0.1", 4454, "qfewbHU51sMudQNx")
obs_client.connect()

nodary_main = FastAPI()
OBS_CAM_RECORD = False
OBS_CAM_STOP_RECORD = False
OBS_MONITORONE = False
OBS_MONITORTWO = False

dict_action = {
    1: "OBS_CAM_RECORD",
    2: "OBS_CAM_STOP_RECORD",
    3: "OBS_MONITORONE",
    4: "OBS_MONITORTWO"
}


@nodary_main.post("/{incoming_integer}")
def catch_number(incoming_integer: int):
    global OBS_CAM_RECORD, OBS_CAM_STOP_RECORD, OBS_MONITORONE, OBS_MONITORTWO

    if incoming_integer in dict_action:
        action = dict_action[incoming_integer]

        if action == "OBS_CAM_RECORD":
            OBS_CAM_RECORD = True
            obs_client.call(requests.StartRecord())
        elif action == "OBS_CAM_STOP_RECORD":
            OBS_CAM_STOP_RECORD = True
            obs_client.call(requests.StopRecord())

        elif action == "OBS_MONITORONE":
            OBS_MONITORONE = True
            obs_client.call(requests.SetCurrentProgramScene(sceneName="Scene"))

        elif action == "OBS_MONITORTWO":
            OBS_MONITORTWO = True
            obs_client.call(
                requests.SetCurrentProgramScene(sceneName="Scene 2"))

    else:
        print("Not gonna work bud")


uvicorn.run(nodary_main, host="127.0.0.1", port=8000)
