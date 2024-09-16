from jgcmlib.jgabcli import main as jgabcli_main

from jgcmlib.jgabcli import main_mid2score as jgabcli_main_mid2score

import jgcmlib as oabclib

from jghfmanager.jgthfcli import main as jgthfcli_main
import jghfmanager as ohflib

def wfohfi_then_oabc_foreach_json_files():
    print("Run Inferences then convert to abc commands foreach json files in the current directory.")
    jgthfcli_main()
    import os
    from jgcmlib.jgcmhelper import pto_post_just_an_abc_file,extract_abc_from_json_to_abc_file
    #list all json files
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    for json_file in json_files:
        print(f"Processing {json_file}")
        abc_filename = extract_abc_from_json_to_abc_file(json_file)
        res_musicsheet_svg_filepath, res_audio_filepath, res_midi_filepath =  pto_post_just_an_abc_file(abc_filename,score_ext="jpg")
        
def say_hello():
    print("Hello, World!")
    

def __help__():
    print("This is a practice package to experiment with Orpheus's goals.")
    print("The following commands are available:")
    print("oabc")
    print("omid2score")
    print("say_hello_orpheuspypractice")
    
