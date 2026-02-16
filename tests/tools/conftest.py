import pytest
from unittest.mock import patch
from datetime import datetime

@pytest.fixture
def mock_datetime():
      with patch("src.tools.time.datetime") as mock_dt:
          mock_dt.now.return_value = datetime(2025, 6, 15, 10, 30, 0)
          yield mock_dt