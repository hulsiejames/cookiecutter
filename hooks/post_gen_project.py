"""Apply the optional local Git setup after project generation."""

import subprocess

INITIALISE = "{{ cookiecutter.init_git }}".lower() == "true"
PUBLISH = "{{ cookiecutter.push_repository }}".lower() == "true"
REMOTE = {{ cookiecutter.github_url|tojson }}


def main() -> None:
    """Commit the generated files and optionally publish to the supplied remote."""
    if PUBLISH and not INITIALISE:
        raise SystemExit("Enable init_git before selecting push_repository.")
    if not INITIALISE:
        return
    commands = [
        ["git", "init", "--initial-branch=main"],
        ["git", "add", "--all"],
        ["git", "commit", "--message=Initial package scaffold"],
        ["git", "remote", "add", "origin", REMOTE],
    ]
    if PUBLISH:
        commands.append(["git", "push", "--set-upstream", "origin", "main"])
    try:
        for command in commands:
            subprocess.run(command, check=True)
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(
            f"Git setup failed: {error}. Check Git authentication and author settings, "
            "or generate again with init_git=false and push_repository=false."
        ) from error
    print(f"Git repository ready; origin is {REMOTE}")


if __name__ == "__main__":
    main()
