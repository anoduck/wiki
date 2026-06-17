#! /usr/bin/env just --justfile
# Wiki JustFile
# Jun 2026 (c) Anoduck, The Anonymous Duck
# MIT License: https://anoduck.mit-license.org
# --------------------------------------------
today := `date +"%Y-%m-%dT%H:%M:%S%:z"`

default:
	@just --list

commit:
	git add .
	git commit -am "Commiting changes for {{today}}"
	git push
