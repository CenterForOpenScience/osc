#!/bin/sh
set -e   # if there's an error, stop running
set -x   # print each command as it runs
pelican content -s build.py
ghp-import output -m "Regenerate site"
git checkout gh-pages
echo "osc.centerforopenscience.org" > CNAME
git add CNAME
git commit -m "commit CNAME file"
git checkout master
git push origin gh-pages

