import apt
import apt.progress.text

class DependencyManager:
    def __init__(self):
        self.cache = apt.Cache()

    def install_package(self, package_name):
        self.cache.update()
        self.cache.open()
        pkg = self.cache[package_name]
        if pkg.is_installed:
            print(f"{package_name} is already installed.")
        else:
            pkg.mark_install()
            try:
                self.cache.commit(apt.progress.text.AcquireProgress(), apt.progress.text.InstallProgress())
                print(f"{package_name} has been installed.")
            except Exception as e:
                print(f"Failed to install {package_name}: {e}")

    def remove_package(self, package_name):
        self.cache.update()
        self.cache.open()
        pkg = self.cache[package_name]
        if not pkg.is_installed:
            print(f"{package_name} is not installed.")
        else:
            pkg.mark_delete()
            try:
                self.cache.commit(apt.progress.text.AcquireProgress(), apt.progress.text.InstallProgress())
                print(f"{package_name} has been removed.")
            except Exception as e:
                print(f"Failed to remove {package_name}: {e}")

    def is_package_installed(self, package_name):
        self.cache.update()
        self.cache.open()
        pkg = self.cache[package_name]
        return pkg.is_installed

# Example usage
if __name__ == "__main__":
    manager = DependencyManager()
    manager.install_package("musescore3/jammy")
    print("Is musescore3 installed?", manager.is_package_installed("musescore3/jammy"))
    manager.remove_package("musescore3/jammy")