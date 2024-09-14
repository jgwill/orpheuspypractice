
echo "Installing dependencies"
odep install_abc2midi &>/dev/null && echo "abc2midi installtion ran successfully" || echo "abc2midi installation failed"
odep install_imagemagick&>/dev/null && echo "ImageMagick installation ran successfully" || echo "ImageMagick installation failed"
odep install_musescore &>/dev/null && echo "Musescore installation ran successfully" || echo "Musescore installation failed"

echo "--------------------------"

if [ "$(odep is_musescore_installed)" == "True" ];then echo "Musescore dependencies are ok";fi
if [ "$(odep is_imagemagick_installed)" == "True" ];then echo "Image convertions dependencies are ok";fi
if [ "$(odep is_abc2midi_installed )" == "True" ];then echo "MIDI Conversion dependencies are ok";fi
