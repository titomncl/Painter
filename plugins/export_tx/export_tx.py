import os
import re

from distutils.dir_util import copy_tree

from CommonTools import os_
from CommonTools.concat import concat
from Painter.plugins.export_tx import export_config
from Painter.common_ import export_project_textures


def compute_new_version_folder(path):
    folders = os.listdir(path)

    if folders:
        version_folder_pattern = re.compile(r"\d{3}")

        version_folders = list(set([f for f in folders if version_folder_pattern.match(f)]))

        version_folders.sort()

        last_folder = version_folders[-1]
    else:
        last_folder = "000"

    if last_folder.isdigit():
        version = int(last_folder) + 1
        version = str(version).zfill(3)

        return version
    else:
        e = concat(path, " is incorrect.")
        raise ValueError(e)


def export():
    path = os.environ["ITEM_PATH"]
    name = os.environ["ITEM_NAME"]
    task = os.environ["ITEM_TASK"]

    export_path = os.path.join(path, name, task)

    export_path = os.path.join(os_.glob_path_recursive(export_path, "TEXTURES"), "VERSION").replace("\\", "/")

    version = compute_new_version_folder(export_path)

    version_path = os.path.join(export_path, version)

    os_.make_dirs(version_path)

    config = export_config.config(version_path, name)

    export_project_textures(config)

    return version_path


def export_publish():
    publish = os.environ["ITEM_PUBLISH"]
    name = os.environ["ITEM_NAME"]
    task = os.environ["ITEM_TASK"]

    export_path = os.path.join(publish, name, task)

    version_path = export()

    copy_tree(version_path, export_path)
