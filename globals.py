import os


PAINTER_EXT = ".spp"

PROJECT_PATH = os.environ["PROJECT_ENV"]
DEV_PATH = os.environ["DEV_ENV"]
ROOT_PATH = os.environ["ROOT_PATH"]
PROJECT = PROJECT_PATH.split("/")[-1]
