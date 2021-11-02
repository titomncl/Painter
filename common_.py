import substance_painter

from CommonTools.concat import concat


def test():
    print("")


def qt_instance():
    return substance_painter.ui


def main_window():
    return qt_instance().get_main_window()


def filepath():
    return substance_painter.project.file_path()


def save_as(filepath_):
    substance_painter.project.save_as(filepath_, substance_painter.project.ProjectSaveMode.Full)


def open_file(filepath_):
    substance_painter.project.open(filepath_)


def normal_map_format():
    return substance_painter.project.NormalMapFormat.OpenGL


def tangent_space():
    return substance_painter.project.TangentSpace.PerVertex


def uv_tile_workflow():
    return substance_painter.project.ProjectWorkflow.UVTile


def project_settings():
    settings = substance_painter.project.Settings(import_cameras=False,
                                                  normal_map_format=normal_map_format(),
                                                  tangent_space_mode=tangent_space(),
                                                  project_workflow=uv_tile_workflow(),
                                                  default_texture_resolution=2048)

    return settings


def mesh_file(path, name_, quality="LD"):
    filename = concat(name_, "_MOD_", quality, ".abc")
    return concat(path, name_, "MOD", quality, filename, separator="/")

def create_project(mesh):
    substance_painter.project.create(mesh_file_path=mesh,
                                     settings=project_settings())


def export_project_textures(config):
    return substance_painter.export.export_project_textures(config)