import pyautogui as pyg

PY_AUTO_GUI_CONTROL_DICT = {

    25: lambda: pyg.press('enter'),
    26: lambda: pyg.press('f1'),

    27: lambda: pyg.press('ctrl'),
    28: lambda: pyg.press('ctrlleft'),
    29: lambda: pyg.press('ctrlright'),

    30: lambda: pyg.press('alt'),
    31: lambda: pyg.press('shift'),
    32: lambda: pyg.press('win'),

    33: lambda: pyg.press('up'),
    34: lambda: pyg.press('down'),
    35: lambda: pyg.press('right'),
    36: lambda: pyg.press('left'),

    37: lambda: pyg.hotkey('ctrl', 'c'),
    38: lambda: pyg.hotkey('ctrl', 'v'),

    39: lambda: pyg.hotkey('ctrl', '0'),
    40: lambda: pyg.hotkey('ctrl', '1'),
    41: lambda: pyg.hotkey('ctrl', '2'),
    42: lambda: pyg.hotkey('ctrl', '3'),
    43: lambda: pyg.hotkey('ctrl', '4'),
    44: lambda: pyg.hotkey('ctrl', '5'),
    45: lambda: pyg.hotkey('ctrl', '6'),
    46: lambda: pyg.hotkey('ctrl', '7'),
    47: lambda: pyg.hotkey('ctrl', '8'),
    48: lambda: pyg.hotkey('ctrl', '9'),
}
