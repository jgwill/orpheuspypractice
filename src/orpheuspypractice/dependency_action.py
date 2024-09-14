from .dependency_manager import DependencyManager



def install_musescore():
    manager = DependencyManager()
    manager.install_package("musescore3")

def remove_musescore():
    manager = DependencyManager()
    manager.remove_package("musescore3")

def is_musescore_installed():
    manager = DependencyManager()
    return manager.is_package_installed("musescore3")

def install_imagemagick():
    manager = DependencyManager()
    alt_package="imagemagick-6.q16"
    image_magick_package = "imagemagick"
    cpackage=image_magick_package
    manager.install_package(cpackage)

def remove_imagemagick():
    manager = DependencyManager()
    alt_package="imagemagick-6.q16"
    image_magick_package = "imagemagick"
    cpackage=image_magick_package
    manager.remove_package(cpackage)

def is_imagemagick_installed():
    manager = DependencyManager()    
    image_magick_command = "convert"
    return manager.is_package_installed(image_magick_command)

def install_abc2midi():
    manager = DependencyManager()
    manager.install_package("abcmidi")

def remove_abc2midi():
    manager = DependencyManager()
    manager.remove_package("abcmidi")

def is_abc2midi_installed():
    manager = DependencyManager()
    midi_converter = "abc2midi"
    return manager.is_package_installed(midi_converter)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Manage dependencies. Here are the available actions: install_musescore, remove_musescore, is_musescore_installed, install_imagemagick, remove_imagemagick, is_imagemagick_installed, install_abc2midi, remove_abc2midi, is_abc2midi_installed")
    parser.add_argument("action", help="The action to perform")
    args = parser.parse_args()
    action = args.action
    if action == "install_musescore":
        install_musescore()
    elif action == "remove_musescore":
        remove_musescore()
    elif action == "is_musescore_installed":
        print(is_musescore_installed())
    elif action == "install_imagemagick":
        install_imagemagick()
    elif action == "remove_imagemagick":
        remove_imagemagick()
    elif action == "is_imagemagick_installed":
        print(is_imagemagick_installed())
    elif action == "install_abc2midi":
        install_abc2midi()
    elif action == "remove_abc2midi":
        remove_abc2midi()
    elif action == "is_abc2midi_installed":
        print(is_abc2midi_installed())
    else:
        print(f"Unknown action: {action}")

def __help__():
    print("This is a practice package to experiment with Orpheus's goals.")
    print("The following commands are available:")
    print("install_musescore")
    print("remove_musescore")
    print("is_musescore_installed")
    print("install_imagemagick")
    print("remove_imagemagick")
    print("is_imagemagick_installed")
    print("install_abc2midi")
    print("remove_abc2midi")
    print("is_abc2midi_installed")
    print("say_hello")
    
    
if __name__ == "__main__":
    main()