#!/usr/bin/env python3
"""Github Org Client"""
from utils import get_json


class GithubOrgClient:
    """Client for interacting with GitHub organization data."""
    
    def __init__(self, org_name):
        """Initialize with organization name."""
        self._org_name = org_name
    
    @property
    def _public_repos_url(self):
        """Generate URL for organization's public repositories."""
        return f"https://api.github.com/orgs/{self._org_name}/repos"
    
    def public_repos(self):
        """Fetch list of public repository names for the organization."""
        repos = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos if repo.get("name")]

def get_json(url):
    """Helper function to fetch JSON data from a URL."""
    response = requests.get(url)
    return response.json()