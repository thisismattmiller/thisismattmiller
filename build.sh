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
python build_index.py
cd ..
hugo -s dev/
mv dev/public/* .
git add .
git commit -m 'release'
git push