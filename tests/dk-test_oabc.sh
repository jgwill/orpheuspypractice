
# Run the test in docker container
(cd bin/testapp && \
	dkrun bash /tests/test_oabc.sh &>/dev/null && echo "oabc Ok"||echo "oabc failed")


