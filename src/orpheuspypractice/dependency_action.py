from dependency_manager import DependencyManager

def install_musescore():
    manager = DependencyManager()
    manager.install_package("musescore3/jammy")

def remove_musescore():
    manager = DependencyManager()
    manager.remove_package("musescore3/jammy")

def is_musescore_installed():
    manager = DependencyManager()
    return manager.is_package_installed("musescore3/jammy")

def __help__():
    print("This is a practice package to experiment with Orpheus's goals.")
    print("The following commands are available:")
    print("install_musescore")
    print("remove_musescore")
    print("is_musescore_installed")
    print("say_hello")