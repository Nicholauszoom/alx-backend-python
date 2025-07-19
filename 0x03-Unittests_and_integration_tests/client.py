#!/usr/bin/env python3
"""Github Org Client"""
from utils import get_json


class GithubOrgClient:
    """Client for GitHub organization"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Returns organization data"""
        return get_json(self.ORG_URL.format(self.org_name))
