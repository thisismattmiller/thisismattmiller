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
python3 build_index.py
cd ..
hugo -s dev/
mv dev/public/* .
python3 build_zip.py
git add .
git commit -m 'release'
git push