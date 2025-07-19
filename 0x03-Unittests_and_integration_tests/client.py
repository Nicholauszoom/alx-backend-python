#!/usr/bin/env python3

from utils import get_json

class GithubOrgClient:
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        self._org_name = org_name

    @property
    def _public_repos_url(self):
        return self.ORG_URL.format(org=self._org_name) + "/repos"

    def public_repos(self):
        json_payload = get_json(self._public_repos_url)
        return [repo["name"] for repo in json_payload if repo.get("name")]

    def has_license(self, repo, license_key):
        return repo.get("license", {}).get("key") == license_key