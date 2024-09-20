rm -rf dist
pip install -U jgcmlib &>/dev/null;pip install -U jgcmlib &>/dev/null
pip freeze|grep jgcmlib
#jghfmanager
pip install -U jghfmanager &>/dev/null;pip install -U jghfmanager &>/dev/null
pip freeze|grep jghfmanager
sleep 1
python setup.py sdist bdist_wheel

