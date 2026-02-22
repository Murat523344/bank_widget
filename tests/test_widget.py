import pytest

from src.widget.widget import get_date, render_widget


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2023-02-22", "22.02.2023"),
        ("2019-08-26", "26.08.2019"),
    ]
)
def test_get_date(input_date: str, expected: str) -> None:
    result = get_date(input_date)
    assert result == expected


def test_render_widget() -> None:
    output = render_widget()
    assert output == "Widget rendered successfully"
