# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_release.ipynb (unless otherwise specified).

__all__ = ['get_last_tag', 'get_commits', 'get_release_version', 'changelog_report', 'release_report', 'get_token',
           'make_git_release', 'get_tags', 'make_changelog']

# Cell
import os
import re
import subprocess
from fastcore.script import call_parse
from configparser import ConfigParser
from pathlib import Path

# Cell
def get_last_tag():
    "Get latest git tag"
    return subprocess.run(["git", "describe", "--tags", "--abbrev=0"],
                          capture_output=True).stdout.decode("utf").strip()

# Cell
def get_commits(from_tag=None, to="HEAD"):
    "Get commits `from_tag` to `to`"
    last_tag = from_tag if from_tag is not None else get_last_tag()
    commit_msgs = subprocess.run(["git", "log", f"{last_tag}..{to}", "--pretty=%s"],
                          capture_output=True).stdout.decode("utf").strip()
    return commit_msgs.split("\n")

# Cell
def get_release_version():
    "Get release version from settings.ini"
    project_path = str(Path(__file__).parent.parent)
    config = ConfigParser(delimiters=['='])
    config.read(os.path.join(project_path, 'settings.ini'))
    cfg = config['DEFAULT']
    return cfg["version"]

# Cell
def changelog_report(report_title, from_tag=None, to="HEAD"):
    "Changelog report `from_tag` to commit `to` using `report_title`"
    commit_msgs = get_commits(from_tag, to)
    bugfixes = [f"* {msg}" for msg in commit_msgs if re.search("\[FIX\]", msg)]
    docs = [f"* {msg}" for msg in commit_msgs if re.search("\[DOC\]", msg)]
    new_features = [f"* {msg}" for msg in commit_msgs if re.search("\[FEA\]", msg)]
    maintenance = [f"* {msg}" for msg in commit_msgs if re.search("\[MNT\]", msg)]
    report_bugfixes = "### Bugfixes:\n{}".format("\n".join(bugfixes)) if len(bugfixes) > 0 else ""
    report_docs = "### Documentation:\n{}".format("\n".join(docs)) if len(docs) > 0 else ""
    report_features = "### New features:\n{}".format("\n".join(new_features)) if len(new_features) > 0 else ""
    report_maintenance = "### Refactoring / Maintenance:\n{}".format("\n".join(maintenance)) if len(maintenance) > 0 else ""
    report_list = [report_title, report_features, report_bugfixes, report_docs, report_maintenance]
    report_list = [rep for rep in report_list if rep != ""]
    report = "\n\n".join(report_list)
    return report

# Cell
def release_report():
    "Create release report out of commit messages"
    release_version = get_release_version()
    return changelog_report(report_title="")

# Cell
def get_token():
    project_path = str(Path(__file__).parent.parent)
    with open(os.path.join(project_path, "token"), "r") as f:
        token = f.read().strip()
    return token

# Cell
@call_parse
def make_git_release():
    "Make a release as a git tag and publish to GitHub"
    # get token
    token = get_token()
    # get release version
    release_version = get_release_version()
    # get release report
    report = release_report()
    # authentificate with GitHub
    subprocess.run(["gh", "auth", "login", "--with-token", token])
    # create release on GitHub
    subprocess.run(["gh", "release", "create", release_version,
                    "-n", report, "-t", f"Release version {release_version}"])

# Cell
def get_tags():
    "Get git tags as a list"
    return subprocess.run(["git", "tag", "-l"], capture_output=True).stdout.decode("utf").strip().split("\n")

# Cell
@call_parse
def make_changelog():
    "Make changelog out of releases / git tags"
    project_path = str(Path(__file__).parent.parent)
    tags = get_tags()
    changelog_title = "# Release notes"
    reports = []
    for from_tag, to in zip(tags[:-1], tags[1:]):
        reports.append(changelog_report(report_title=f"## {to}", from_tag=from_tag, to=to))
    changelog = changelog_title + "\n\n" + "\n\n".join(reports[::-1])
    with open(os.path.join(project_path, "CHANGELOG.md"), "w") as f:
        f.write(changelog)