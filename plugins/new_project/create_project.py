from collections import OrderedDict

from CommonTools.concat import concat
from CommonTools.save_load.controller import Controller

from Painter.globals import PROJECT_PATH, ROOT_PATH, PROJECT, PAINTER_EXT
from Painter.common_ import filepath, save_as, main_window, mesh_file, create_project


class Create(object):

    @property
    def root(self):
        return ROOT_PATH

    @property
    def project(self):
        return PROJECT

    @property
    def filepath(self):
        try:
            filepath_ = filepath()
            if PROJECT_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None
        except TypeError:
            return None


    @property
    def buttons(self):
        buttons = OrderedDict()

        buttons["SHD"] = {
            "CHARA": True,
            "PROPS": True,
            "SET": True,
            "FX": False,
        }

        return buttons

    def save(self, type_="", name_="", task_=""):
        """
        Args:
            type_ (str): chara, props, set
            name_ (str): name of the asset
            task_ (str): department of the file: MOD, RIG, SHD

        Returns:
            str, str: versioned and published filepath

        """
        filename = concat(name_, task_, "001" + PAINTER_EXT, separator="_")
        filepath_ = concat(PROJECT_PATH, "DATA/LIB", type_, name_, task_, "SCENE/VERSION", filename, separator="/")

        save_as(filepath_)

    def new_project(self, type_, name_, task_):
        mesh = mesh_file(self.root, self.project, type_, name_, "LD")

        create_project(mesh)

        self.save(type_, name_, task_)

def main():
    Controller(Create().new_project, "Create", main_window(),
               Create().root, Create().project, Create().buttons)
