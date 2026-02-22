import pytest
from src.utils import read_json

def test_read_json_valid(tmp_path):
    file = tmp_path / "data.json"
    file.write_text('[{"amount": 100, "currency": "USD"}]')
    result = read_json(file)
    assert isinstance(result, list)
    assert result[0]["amount"] == 100

def test_read_json_empty(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text('')
    result = read_json(file)
    assert result == []

def test_read_json_not_list(tmp_path):
    file = tmp_path / "not_list.json"
    file.write_text('{"amount": 100}')
    result = read_json(file)
    assert result == []

def test_read_json_missing():
    result = read_json("missing.json")
    assert result == []