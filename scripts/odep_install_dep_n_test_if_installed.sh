odep install_abc2midi
odep install_imagemagick
odep install_musescore

if [ "$(odep is_musescore_installed)" == "True" ];then echo "Musescore dependencies are ok";fi
if [ "$(odep is_imagemagick_installed)" == "True" ];then echo "Image convertions dependencies are ok";fi
if [ "$(odep is_abc2midi_installed )" == "True" ];then echo "MIDI Conversion dependencies are ok";fi
