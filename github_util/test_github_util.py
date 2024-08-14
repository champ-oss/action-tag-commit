"""Provides tests for GitHub utility."""
import unittest
from unittest.mock import MagicMock

from github import UnknownObjectException, GithubException
from typing_extensions import Self

from github_util.github_util import GitHubUtil


class TestGitHubUtil(unittest.TestCase):
    """Provides tests for GitHub utility."""

    def setUp(self: Self) -> None:
        """Set up the requirements for testing."""
        self.github_session = MagicMock()
        self.github_util = GitHubUtil(access_token='test123',
                                      organization_name='test-org',
                                      github_session=self.github_session)

    def test_get_repo_commit_with_success(self: Self) -> None:
        """Validate the get_repo_commit function is successful."""
        self.assertIsNotNone(self.github_util.get_repo_commit(repo=MagicMock(), commit='123'))

    def test_get_repo_commit_with_unknown_object_exception(self: Self) -> None:
        """Validate the get_repo_commit function handles an exception."""
        repo = MagicMock()
        repo.get_commit.side_effect = UnknownObjectException(400)
        self.assertIsNone(self.github_util.get_repo_commit(repo=repo, commit='123'))

    def test_get_repo_commit_with_github_exception(self: Self) -> None:
        """Validate the get_repo_commit function handles an exception."""
        repo = MagicMock()
        repo.get_commit.side_effect = GithubException(status=422, message='No commit found for SHA: foo')
        self.assertIsNone(self.github_util.get_repo_commit(repo=repo, commit='123'))

    def test_get_repo_with_success(self: Self) -> None:
        """Validate the get_repo function is successful."""
        self.assertIsNotNone(self.github_util.get_repo(repo_name='test-repo-1'))

    def test_get_repo_with_unknown_object_exception(self: Self) -> None:
        """Validate the get_repo function handles an exception."""
        self.github_session.get_organization.return_value.get_repo.side_effect = UnknownObjectException(400)
        self.assertIsNone(self.github_util.get_repo(repo_name='test-repo-1'))

    def test_get_repo_with_github_exception(self: Self) -> None:
        """Validate the get_repo function handles an exception."""
        self.github_session.get_organization.return_value.get_repo.side_effect = GithubException(status=422,
                                                                                                 message='Not found')
        self.assertIsNone(self.github_util.get_repo(repo_name='test-repo-1'))

    def test_tag_commit(self: Self) -> None:
        """Validate the tag_commit function is successful."""
        self.assertIsNone(self.github_util.tag_commit(repo_name='test-repo-1', commit='123', tag='test-tag'))

    def test_tag_commit_with_repo_not_found(self: Self) -> None:
        """Validate the tag_commit function handles a repository not found."""
        self.github_session.get_organization.return_value.get_repo.return_value = None
        self.assertIsNone(self.github_util.tag_commit(repo_name='test-repo-1', commit='123', tag='test-tag'))

    def test_tag_commit_with_ref_not_found(self: Self) -> None:
        """Validate the tag_commit function handles a ref not found."""
        self.github_session.get_organization.return_value. \
            get_repo.return_value.get_git_ref.side_effect = UnknownObjectException(400)
        self.assertIsNone(self.github_util.tag_commit(repo_name='test-repo-1', commit='123', tag='test-tag'))

    def test_tag_commit_with_github_exception(self: Self) -> None:
        """Validate the tag_commit function handles a ref not found."""
        self.github_session.get_organization.return_value. \
            get_repo.return_value.get_git_ref.side_effect = GithubException(status=422, message='Not found')
        self.assertIsNone(self.github_util.tag_commit(repo_name='test-repo-1', commit='123', tag='test-tag'))

    def test_tag_commit_with_create_git_ref_not_found(self: Self) -> None:
        """Validate the tag_commit function handles a ref not found."""
        self.github_session.get_organization.return_value. \
            get_repo.return_value.get_git_ref.side_effect = UnknownObjectException(400)

        self.github_session.get_organization.return_value. \
            get_repo.return_value.create_git_ref.side_effect = UnknownObjectException(400)
        self.assertIsNone(self.github_util.tag_commit(repo_name='test-repo-1', commit='123', tag='test-tag'))
