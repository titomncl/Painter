import os
import sys

if sys.version_info > (3,):
    import typing

    if typing.TYPE_CHECKING:
        from Odin import Asset, Shot
        from typing import Optional, Union

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

        buttons["Assets"] = ["SHD"]
        buttons["Shots"] = []

        return buttons

    def save(self, item="", dpt=""):
        # type: (Optional[Union[Asset, Shot]], str) -> None
        """.
        Args:
            item: name of the asset
            dpt: department of the file: MOD, RIG, SHD

        """
        path = os.path.join(item.paths["PATH"], item.name, dpt).replace("\\", "/")
        path = self.glob_recursive(path, "VERSION")

        filename = concat(item.name, dpt, "001" + PAINTER_EXT, separator="_")
        filepath_ = concat(path, filename, separator="/")


        save_as(filepath_)

    def new_project(self, item, dpt):
        mesh = mesh_file(item.paths["PUBLISH"], item.name, "LD")

        create_project(mesh)

        self.save(item, dpt)

    def glob_recursive(self, path, endswith):
        for dir_path, dirs, _ in os.walk(path):
            for dir in dirs:
                file_path = os.path.join(dir_path, dir).replace("\\", "/")
                if file_path.endswith(endswith):
                    return file_path

def main():
    instance = Controller(Create().new_project, "Create", main_window(),
               Create().root, Create().project, Create().buttons)

    instance.ui.shots_btn.setEnabled(False)
