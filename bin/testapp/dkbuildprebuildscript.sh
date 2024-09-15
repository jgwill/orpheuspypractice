bdir=testapp
rm -rf ../$bdir/dist
rm -rf ../$bdir/scripts
cp -r ../../scripts scripts
rm -rf ../$bdir/samples
cp -r ../../samples samples
rm -rf ../$bdir/tests
cp -r ../../tests tests

(cd ../.. && python setup.py sdist bdist_wheel) && \
	cp -r ../../dist/ dist/ || exit 1

