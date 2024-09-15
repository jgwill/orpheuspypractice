
# Run the test in docker container
(cd bin/testapp && \
	dkrun bash /tests/test_musescore3_mid_2_score.sh &>/dev/null && echo "Score Convertion Ok"||echo "Score convertion failed")


