#!/bin/bash

rm -fr 404.html
rm -fr about
rm -fr categories
rm -fr css
rm -fr dist
rm -fr img
rm -fr post
rm -fr index.html
rm -fr index.xml
rm -fr series
rm -fr sitemap.xml
rm -fr tags
cd dev
uv run build_index.py || { echo "build_index.py failed, aborting release"; exit 1; }
cd ..
hugo -s dev/
mv dev/public/* .
uv run build_zip.py
git add .
git commit -m 'release'
git push