"""Execute a project notebook in place without requiring jupyter-nbconvert."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient


def main() -> None:
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    notebook_path = (project_root / args.notebook).resolve()
    if not notebook_path.is_relative_to(project_root):
        raise ValueError("Notebook must be inside the project workspace")

    with notebook_path.open("r", encoding="utf-8") as handle:
        notebook = nbformat.read(handle, as_version=4)

    client = NotebookClient(
        notebook,
        timeout=args.timeout,
        kernel_name="python3",
        allow_errors=False,
        resources={"metadata": {"path": str(notebook_path.parent)}},
    )
    client.execute()

    temporary_path = notebook_path.with_suffix(notebook_path.suffix + ".executed")
    with temporary_path.open("w", encoding="utf-8") as handle:
        nbformat.write(notebook, handle)
    temporary_path.replace(notebook_path)
    print(f"Executed {notebook_path.relative_to(project_root)}")


if __name__ == "__main__":
    main()
