
import pytest
from findmyorder import findmyorder


def test_dynaconf_is_in_testing_env():
    assert return_a_value() == "On Testing"


def test_search():
    fmo = findmyorder()
    assert fmo.search('buy btc') == True
    assert fmo.search('hello') == False


def test_hello():
    print("Hello, World!")