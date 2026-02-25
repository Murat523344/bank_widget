from typing import Any

from src.utils import read_json


def test_read_json_valid(tmp_path: Any) -> None:
    file_path = tmp_path / "operations.json"
    file_path.write_text('[{"id": 1, "amount": 100}]', encoding="utf-8")

    result = read_json(str(file_path))
    assert isinstance(result, list)
    assert result[0]["id"] == 1
    assert result[0]["amount"] == 100


def test_read_json_empty_file(tmp_path: Any) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text('', encoding="utf-8")

    result = read_json(str(file_path))
    assert result == []


def test_read_json_nonexistent_file() -> None:
    result = read_json("nonexistent.json")
    assert result == []


def test_read_json_invalid_json(tmp_path: Any) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text('{"id": 1, "amount": 100}', encoding="utf-8")  # не список, а словарь

    result = read_json(str(file_path))
    assert result == []
