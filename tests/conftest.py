"""Test configuration for AWS Architecture Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "aws-architecture-agent", "category": "Cloud Engineering"}
