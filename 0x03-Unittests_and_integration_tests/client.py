#!/usr/bin/env python3
"""Github Org Client"""
from utils import get_json


class GithubOrgClient:
    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch the organization data"""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")


    @property
    def _public_repos_url(self):
        """Extract repos URL from org data"""
        return self.org.get("repos_url")
