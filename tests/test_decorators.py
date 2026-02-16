import pytest

from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def test_func(a, b):
        return a + b

    result = test_func(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "test_func ok" in captured.out


def test_log_console_error(capsys):
    @log()
    def test_func(a, b):
        raise ValueError("error")

    with pytest.raises(ValueError):
        test_func(1, 2)

    captured = capsys.readouterr()
    assert "test_func error: ValueError" in captured.out
    assert "Inputs: (1, 2), {}" in captured.out


def test_log_file_success(tmp_path):
    file_path = tmp_path / "log.txt"

    @log(filename=str(file_path))
    def test_func(a, b):
        return a + b

    result = test_func(1, 2)

    assert result == 3
    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    assert "test_func ok" in content


def test_log_file_error(tmp_path):
    file_path = tmp_path / "log.txt"

    @log(filename=str(file_path))
    def test_func(a, b):
        raise ValueError("error")

    with pytest.raises(ValueError):
        test_func(1, 2)

    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    assert "test_func error: ValueError" in content
    assert "Inputs: (1, 2), {}" in content
