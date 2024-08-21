# action-tag-commit

A GitHub Action which creates a git tag in a repository for a commit

[![.github/workflows/test.yml](https://github.com/champ-oss/action-tag-commit/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/champ-oss/action-tag-commit/actions/workflows/test.yml)
[![.github/workflows/release.yml](https://github.com/champ-oss/action-tag-commit/actions/workflows/release.yml/badge.svg)](https://github.com/champ-oss/action-tag-commit/actions/workflows/release.yml)

## Features

- Supports creating a tag in a remote repository (assuming permission exists)

## Example Usage

```yaml
name: example

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: champ-oss/action-tag-commit@main
        with:
          repo-name: my-repo
          commit-sha: c24c9fe3b3baa0179555913e94224fee5be361cf
          tag-name: test
          token: ${{ secrets.GITHUB_TOKEN }}
          organization: champ-oss
```

## Parameters

| Parameter    | Required | Description                   |
|--------------|----------|-------------------------------|
| repo-name    | true     | Repository name to create tag |
| commit-sha   | true     | Commit SHA to tag             |
| organization | true     | GitHub organization name      |
| tag-name     | true     | Tag to add to the repository  |
| token        | false    | GitHub Token or PAT           |

