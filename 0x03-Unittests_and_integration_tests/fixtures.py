#!/usr/bin/env python3
org_payload = {
    "login": "testorg",
    "id": 123456,
    "repos_url": "https://api.github.com/orgs/testorg/repos",
    "url": "https://api.github.com/orgs/testorg"
}

repos_payload = [
    {"name": "repo1", "license": {"key": "mit"}},
    {"name": "repo2", "license": {"key": "apache-2.0"}},
    {"name": "repo3", "license": {"key": "gpl-3.0"}},
    {"name": "repo4", "license": {"key": "apache-2.0"}},
    {"name": "repo5", "license": None}
]

expected_repos = ["repo1", "repo2", "repo3", "repo4", "repo5"]

apache2_repos = ["repo2", "repo4"]