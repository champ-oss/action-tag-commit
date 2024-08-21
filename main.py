"""Tags a commit sha."""
import logging
import os

from github_util.github_util import GitHubUtil

logging.basicConfig(
    format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main(github_util: GitHubUtil, repo_name: str, commit_sha: str, tag_name: str) -> None:
    """
    Handle the main execution of the script.

    :return: None
    """
    github_util.tag_commit(repo_name, commit_sha, tag_name)


if __name__ == '__main__':
    main(github_util=GitHubUtil(access_token=os.getenv('TOKEN'), organization_name=os.getenv('ORGANIZATION')),
         repo_name=os.getenv('REPO_NAME'),
         commit_sha=os.getenv('COMMIT_SHA'),
         tag_name=os.getenv('TAG_NAME'))
