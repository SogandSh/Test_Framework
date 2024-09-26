import sys
from pathlib import Path
from importlib import import_module
import os

def get_environment(name):
    files = []
    for path in sys.path:
        if Path(path + "/data/").is_dir():
            for file in os.listdir(path + "/data/"):
                if file.endswith(".py") and file not in files:
                    files.append(file)
    # print(f"files: {files}")
    envs = {}
    for file in files:
        file = file.strip('.py')
        try:
            envs[file] = import_module("data." + file).DICT__ENV
        except AttributeError:
            pass
    # print(f"envs: {envs}")
    return envs[name]


def get_device(env_name, dev_name):
    """ extract device data from environment"""
    dev = get_environment(env_name)
    subpath_names = dev_name.split('.')
    for level in range(0, len(subpath_names)):
        if (subpath_names[level] in dev.keys()):
            dev = dev[subpath_names[level]]
        # else:
        #     raise()
    return dev