from src.tools.time import get_current_datetime

class TestGetDatetime:

    def test_no_arg_success(self, mock_datetime):
        result = get_current_datetime()
        assert result == "2025-06-15 10:30:00"
