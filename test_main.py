"""Provide tests for example handler."""
import unittest
from unittest.mock import MagicMock

from typing_extensions import Self

import main


class TestMain(unittest.TestCase):
    """Provide tests for main script."""

    def test_main(self: Self) -> None:
        """
        The main function should be successful.

        :return:
        """

        github_util = MagicMock()
        main.main(github_util=github_util,
                  repo_name='test-repo',
                  commit_sha='test-commit-sha',
                  tag_name='test-tag')

        github_util.tag_commit.assert_called_once_with('test-repo', 'test-commit-sha', 'test-tag')
