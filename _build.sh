export PYTHONPATH=$(pwd)/src
pip install -U jgtcmlib &>/dev/null
python bump_version.py
git commit setup.py -m "Bump version"
version=$(python setup.py --version)
git tag $version -m "Release $version"
git push origin $version
rm -rf dist;python setup.py sdist bdist_wheel;twine upload dist/*

