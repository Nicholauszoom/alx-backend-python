#!/usr/bin/env python3
from typing import List, Optional
from client import get_json  # or wherever your helper lives

class GithubOrgClient:
    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def _public_repos_url(self) -> str:
        return f"https://api.github.com/orgs/{self.org_name}/repos"

    def public_repos(self, license: Optional[str] = None) -> List[str]:
        repos = get_json(self._public_repos_url)
        if license:
            return [repo["name"] for repo in repos
                    if repo.get("license") and repo["license"].get("key") == license]
        return [repo["name"] for repo in repos]
