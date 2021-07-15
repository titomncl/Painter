import substance_painter

from PySide2 import QtWidgets as Qw

from Painter.common_ import qt_instance

from Painter.plugins.save_load import save, load
from Painter.plugins.new_project import create_project


class Menu:
    def __init__(self):

        self.menu = Qw.QMenu("VSPA_TOOLS", qt_instance().get_main_window())
        qt_instance().add_menu(self.menu)

        self.menu_actions()

    def __del__(self):
        self.menu.clear()
        substance_painter.ui.delete_ui_element(self.menu)
        self.menu = None

    def add_actions(self, title, action):
        act = Qw.QAction(title, self.menu)
        act.triggered.connect(action)

        self.menu.addAction(act)

    def add_separator(self):
        self.menu.addSeparator()

    def menu_actions(self):
        self.add_actions("New project", self.new_prj_action)
        self.add_separator()
        self.add_actions("Save", self.save_action)
        self.add_actions("Load", self.load_action)

    def new_prj_action(self):
        create_project.main()

    def save_action(self):
        save.main()

    def load_action(self):
        load.main()


CUSTOM_MENU_PLUGIN = None


def start_plugin():
    global CUSTOM_MENU_PLUGIN
    CUSTOM_MENU_PLUGIN = Menu()


def close_plugin():
    global CUSTOM_MENU_PLUGIN
    del CUSTOM_MENU_PLUGIN


if __name__ == '__main__':
    start_plugin()
