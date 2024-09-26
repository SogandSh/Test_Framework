import pytest
from core import get_device
from lib.ios import IOS


@pytest.fixture(scope="module")
def ios_interface_module(request):
    env_name = request.node.get_closest_marker("env_name").args[0]
    ios_devices_name = request.node.get_closest_marker("ios_dev").args[0]
    intf = init_ios_interface(ios_devices_name, env_name)
    yield intf
    cleanup_ios_interface(intf)


def init_ios_interface(ios_devices_name, env_name):
    ios_device = get_device(env_name, ios_devices_name)
    ios_env = ios_device["ios_env"]
    intf = IOS(ios_env)
    return intf


def cleanup_ios_interface(intf):
    intf.close()
