"""Make the template's setup guide available to generated READMEs."""

import json
from pathlib import Path


def main() -> None:
    """Read the guide from the temporary template checkout."""
    settings_file = Path("cookiecutter.json")
    settings = json.loads(settings_file.read_text(encoding="utf-8"))
    readme = Path("README.md").read_text(encoding="utf-8")
    heading = "## Template Details"
    _, separator, guide = readme.partition(heading)
    if not separator:
        raise SystemExit("README.md must contain a Template Details section.")
    settings["_template_details"] = heading + guide
    settings_file.write_text(json.dumps(settings, indent=4) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
