
# Expected to run from /app which mounts the repo root
abc_file="tests/an_ok_abc_file_for_test.abc"

_setup()
{

  #Must run this in the background in containers for processing.
  sudo Xvfb :99 -screen 0 1024x768x16 &>/dev/null &
}

_clean()
{
  (cd /tmp && rm -f *.abc *.svg *.mid *.mp3)
}
_clean
_setup && echo "Setup Ok"||echo "Setup failed"
cp $abc_file /tmp/my.abc
# Run the test in docker container
oabc my.abc && echo "oabc Ok"||echo "oabc failed"
