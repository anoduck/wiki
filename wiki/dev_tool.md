```text
#  ____               _____           _ _
# |  _ \  _____   __ |_   _|__   ___ | (_)_ __   __ _
# | | | |/ _ \ \ / /   | |/ _ \ / _ \| | | '_ \ / _` |
# | |_| |  __/\ V /    | | (_) | (_) | | | | | | (_| |
# |____/ \___| \_/     |_|\___/ \___/|_|_|_| |_|\__, |
#                                               |___/
```

Dev Tooling
===========

> Not your normal set of tools.

The Wax Philosophical
----------------------

A less wise version of myself would have scoffed at the concept of dev tooling, and labeled it as unnecessary
fluff or superfluous conveniences. Now that I have come into to wisdom, these conveniences aid in an often
forgotten principle we cherish, uniformity. Programming is not as much a science as it is a form of artistic
expression. The ability to uniformly create is what smoothes the lines and removes distractions from the focal
point of one's creation. 

Intro
-----

Development tooling, often referred to as simply "tooling", are applications and/or scripts that aid
programmers with their workflow and ease tasks such as creating documentation, maintaining standards, and
keeping consistent styling. 

List of Tools
-------------

### Commitizen

Commitizen is compatible with all programming languages because it integrates and is focused on git commit
messages and git tags. There is a less involved version available, which one can install with NPM called
`git-cz`. Regardless, Commitizen is usally installed as a python package, and is integrated on a per
repository basis. What it does is provide a rather convenient dialogue to maintain the 
[conventional commit](https://conventionalcommits.org) standard. This standard effects versioning as well as
commit messages.

### Pre-Commit

Pre-commit is another development that integrates with git and primarily is focused on the execution of
[git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks). Mainly the hook that is run before
changes are commited to git. It is mostly used to run linters before commiting the code.

### Husky

Husky is similar to pre-commit, in that it works with Git's native hooks, except that Husky is purposefully
tuned to work with Node.js. Husky possesses a much smaller footprint than pre-commit, and in many ways is both
more flexible and extensible. It can handle processing both Node.js scripts and shell scripts, which provides
an easy user experience.

### Bump-My-Version

BMV is used to quickly make modifications and manage software versioning. It is a more full featured of "git
bump", and it is also configured and initialized per repository.

#### Creating a fresh config

```bash
bump-my-version sample-config --no-prompt --destination .bumpversion.toml
```

### Scriv

Scriv is new to us, as in fifteen minutes ago, but it claims to provide a means to generate and manage
changelogs which is another one of the many forms of documentation developers are supposed to provide.

Scriv could be nice, but isn't very reasonable to use. It does not use standard formatting for generation of
changelogs. Changelogs are not a unified document, but rather directory of changelogs where each entry is a
seperate file. Furthermore, in order to change this formatting one has to know Jinja templating, which is
unnecessary, and should be something more universal and common.

#### Configuration

As with most dev tooling, configuration is performed per repository basis. Scriv looks for configuration
values in four places; `setup.cfg`, `tox.ini`, `pyproject.toml`, and `scriv.ini`. If none of these files are
found it simply uses it's default values. There are two or three environmental variables that can be managed
in the git config. 

#### Usage

Scriv manages changelogs with four commands; `create`, `collect`, `github-release`,
and `print`. Using `create` will generate a new entry file in the `changelog.d` directory. Executing `collect`
with compile all of the entry files into a unified document.
