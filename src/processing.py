from typing import Dict, List


def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return sorted(data, key=lambda x: x["date"])
