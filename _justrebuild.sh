rm -rf dist
pip install -U jgcmlib &>/dev/null;pip install -U jgcmlib &>/dev/null
pip freeze|grep jgcmlib
sleep 1
python setup.py sdist bdist_wheel

