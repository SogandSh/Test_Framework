import pytest
from core import get_device
from lib.rest import Rest


@pytest.fixture(scope="module")
def rest_interface_module(request):
    env_name = request.node.get_closest_marker("env_name").args[0]
    rest_devices_name = request.node.get_closest_marker("rest_dev").args[0]
    intf = init_rest_interface(rest_devices_name, env_name)
    yield intf
    cleanup_rest_interface(intf)



def init_rest_interface(rest_devices_name, env_name):
    rest_device = get_device(env_name, rest_devices_name)
    rest_env = rest_device["rest_env"]
    intf = Rest(rest_env)
    return intf


def cleanup_rest_interface(intf):
    intf.close()
