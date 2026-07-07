"""Generic Git service."""

from pathlib import Path

from git import Repo
from git.exc import GitCommandError


class GitService:
    """Wrapper around GitPython."""

    def __init__(self, repository, username=None, token=None):
        self.repository = Path(repository)

        if not self.repository.exists():
            raise FileNotFoundError(
                f"Repository not found: {self.repository}"
            )

        self.repo = Repo(self.repository)
        self.username = username
        self.token = token


    @property
    def current_branch(self):
        """Return current branch name."""
        return self.repo.active_branch.name

    @property
    def current_commit(self):
        """Return current commit hash."""
        return self.repo.head.commit.hexsha

    def checkout(self, branch):
        """Checkout existing branch."""
        self.repo.git.checkout(branch)

    def pull(self):
        """Pull latest changes."""
        self.repo.remotes.origin.pull()

    def branch_exists(self, branch):
        """Check whether branch exists."""
        return branch in [h.name for h in self.repo.heads]

    def create_branch(self, branch):
        """Create new branch and checkout."""

        if self.branch_exists(branch):
            self.checkout(branch)
            return

        self.repo.git.checkout("-b", branch)

    def add(self, path):
        """Stage file."""

        path = Path(path)

        relative = path.relative_to(self.repository)

        self.repo.index.add([str(relative)])

    def commit(self, message):
        """Commit staged changes."""

        if not self.repo.is_dirty(untracked_files=True):
            return self.repo.head.commit

        return self.repo.index.commit(message)

    def push(self, branch):
        """Push branch to origin."""

        self.repo.git.push(
            "--set-upstream",
            "origin",
            branch,
        )

    def status(self):
        """Return git status."""

        return self.repo.git.status()

    def is_clean(self):
        """Return True if repository is clean."""

        return not self.repo.is_dirty(
            untracked_files=True
        )

    def configure_remote(self):
        """Temporarily configure origin URL with PAT."""

        if not self.username or not self.token:
            return

        remote = (
            f"https://{self.username}:{self.token}"
            "@github.com/amitgupta369/nac-aci-simple-example.git"
        )

        self.repo.git.remote(
            "set-url",
            "origin",
            remote,
        )