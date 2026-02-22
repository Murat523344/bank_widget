import pytest

from src.external_api import api_call, process_api_data


def test_api_call_success() -> None:
    response = api_call()
    assert response["status"] == "success"


@pytest.mark.parametrize(
    "data",
    [
        ({"id": 1, "name": "test"}),
        ({"id": 2, "name": "example"}),
    ]
)
def test_api_call_data(data: dict) -> None:
    result = process_api_data(data)
    assert result["processed"] is True
    assert result["id"] == data["id"]
