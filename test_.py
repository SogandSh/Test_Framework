import pytest
from fixture.restfixure import rest_interface_module
from fixture.iosfixture import ios_interface_module
from fixture.androidfixture import android_interface_module

pytestmark = [pytest.mark.env_name("Product_env"), pytest.mark.rest_dev("rest"), pytest.mark.ios_dev("ios"),
              pytest.mark.android_dev("android")]


def test_sample_1(rest_interface_module, ios_interface_module, android_interface_module):
    rest_interface_module.get()

