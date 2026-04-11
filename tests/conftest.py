from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: restore shared in-memory state before each test.
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))

    yield

    # Cleanup: restore baseline after each test as well.
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
