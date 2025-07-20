#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Test cases for GithubOrgClient.public_repos"""

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that public_repos returns expected list of repo names"""
        expected_repos = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = expected_repos
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"

        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2", "repo3"])
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")
        mock_public_repos_url.assert_called_once()

        def public_repos(self, license=None):
            """Return list of public repo names, optionally filter by license"""
            repos = get_json(self._public_repos_url)
            if license:
                return [repo["name"] for repo in repos
                    if repo.get("license") and repo["license"].get("key") == license]
        return [repo["name"] for repo in repos]

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos_with_license(self, mock_public_repos_url, mock_get_json):
        """Test public_repos returns repos with given license only"""
        payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}},
        ]
        mock_get_json.return_value = payload
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"

        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), ["repo1", "repo3"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()
