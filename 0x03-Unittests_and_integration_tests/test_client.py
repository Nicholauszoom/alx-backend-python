#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Define the test payload
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        
        # Configure the mock for get_json to return the test payload
        mock_get_json.return_value = test_payload
        
        # Define the test URL
        test_url = "https://api.github.com/orgs/testorg/repos"
        
        # Use patch as a context manager to mock _public_repos_url
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("testorg")
            
            # Call the public_repos method
            repos = client.public_repos()
            
            # Assert that the returned repos match the expected list
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)
            
            # Verify that the mocked property and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()