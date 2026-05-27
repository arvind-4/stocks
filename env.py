"""Load environment variables from .env files."""

import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

ENV_FILES = [
    BASE_DIR / ".env",
    BASE_DIR / ".env.local",
]


def load_env_file(path: pathlib.Path) -> None:
    """Parse a simple KEY=VALUE .env file into os.environ."""
    if not path.exists():
        return

    with path.open() as f:
        for line_raw in f:
            line = line_raw.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            key = key.strip()
            value = value.strip().strip('"').strip("'")

            os.environ[key] = value


def load_env() -> None:
    """Load all .env files into the environment."""
    for env_file in ENV_FILES:
        load_env_file(env_file)
