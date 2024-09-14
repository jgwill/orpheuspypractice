rm -f /tmp/score.svg  &>/dev/null

musescore3 tests/an_ok_mid_file_for_musescore3_mid_2_score.mid -o /tmp/score.svg && \
	if [ -e /tmp/score.svg ]; then
		echo "musescore3 mid to score conversion OK"
	else
		echo "musescore3 mid to score conversion failed"
	fi || echo "musescore3 mid to score conversion failed"

