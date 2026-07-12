from unittest.mock import mock_open, patch

import pytest

from read_lines import read_lines


def test_read_lines_returns_expected_lines():
    mocked_content = "line 1\nline 2\nline 3\n"

    with patch("builtins.open", mock_open(read_data=mocked_content)) as mocked_file:
        result = read_lines("file.txt")

    assert result == ["line 1\n", "line 2\n", "line 3\n"]
    mocked_file.assert_called_once_with("file.txt", "r")


def test_read_lines_raises_file_not_found_error():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("no_file.txt")
