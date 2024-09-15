rm -f /tmp/score.svg  &>/dev/null

#Must run this in the background in containers for processing.
sudo Xvfb :99 -screen 0 1024x768x16 &>/dev/null &

musescore3 tests/an_ok_mid_file_for_musescore3_mid_2_score.mid -o /tmp/score.svg && \
	if [ -e /tmp/score-1.svg ]; then
		echo "musescore3 mid to score conversion OK"
	else
		echo "musescore3 mid to score conversion failed"
	fi || (echo "musescore3 mid to score conversion failed" && exit 1)

