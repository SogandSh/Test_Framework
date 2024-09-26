import pytest
from core import get_device
from lib.android import Android


@pytest.fixture(scope="module")
def android_interface_module(request):
    env_name = request.node.get_closest_marker("env_name").args[0]
    android_devices_name = request.node.get_closest_marker("android_dev").args[0]
    intf = init_android_interface(android_devices_name, env_name)
    yield intf
    cleanup_android_interface(intf)


def init_android_interface(android_devices_name, env_name):
    android_device = get_device(env_name, android_devices_name)
    android_env = android_device["android_env"]
    intf = Android(android_env)
    return intf


def cleanup_android_interface(intf):
    intf.close()
