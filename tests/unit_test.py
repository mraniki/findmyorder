
import pytest
from findmyorder import findmyorder


def test_search():
    fmo = findmyorder()
    assert fmo.search('buy btc') == True
    assert fmo.search('hello') == False