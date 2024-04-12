import os
import pytest

@pytest.fixture
def log(request):
    if not os.path.exists("logs"):
        os.mkdir("logs")

    with open(f"logs/{request.node.name}.log", mode='w', encoding="utf-8") as log:
        yield log
