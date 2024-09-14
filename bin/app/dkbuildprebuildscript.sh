rm -rf dist
rm -rf ../app/scripts
cp -r ../../scripts scripts
rm -rf ../app/samples
cp -r ../../samples samples

(cd ../.. && python setup.py sdist bdist_wheel) && \
	cp -r ../../dist/ dist/ || exit 1

