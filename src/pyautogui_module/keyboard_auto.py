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

}
