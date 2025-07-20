#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized_class, parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")
        
        # Call the has_license method
        result = client.has_license(repo, license_key)
        
        # Assert that the result matches the expected value
        self.assertEqual(result, expected)

@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start patcher for requests.get
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        # Configure side_effect to return appropriate payloads based on URL
        def get_side_effect(url):
            mock_response = Mock()
            if url.endswith("/repos"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = cls.org_payload
            return mock_response
        
        cls.mock_get.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")
        
        # Call the public_repos method
        repos = client.public_repos()
        
        # Assert that the returned repos match the expected_repos fixture
        self.assertEqual(repos, self.expected_repos)

if __name__ == '__main__':
    unittest.main()