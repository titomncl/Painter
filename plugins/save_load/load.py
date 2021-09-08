from CommonTools.save_load.controller import Controller

from Painter.plugins.save_load.save_load import SaveLoad
from Painter.common_ import main_window


def main():
    instance = Controller(SaveLoad().load, "Load", main_window(),
                          SaveLoad().root, SaveLoad().project, SaveLoad().buttons)
