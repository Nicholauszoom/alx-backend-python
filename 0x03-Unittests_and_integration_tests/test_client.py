#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Define test data
        test_org = "test-org"
        test_repos = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}}
        ]
        test_url = f"https://api.github.com/orgs/{test_org}/repos"

        # Set up mock responses
        mock_get_json.return_value = test_repos
        
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            # Configure the mock property to return the test URL
            mock_public_repos_url.return_value = test_url
            
            # Create client instance and call public_repos
            client = GithubOrgClient(test_org)
            result = client.public_repos()

            # Verify results
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(result, expected_repos)

            # Verify mocks were called correctly
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()