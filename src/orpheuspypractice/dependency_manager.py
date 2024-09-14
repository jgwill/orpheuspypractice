import subprocess

class DependencyManager:
    def __init__(self):
        pass

    def install_package(self, package_name):
        try:
            subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
            print(f"{package_name} has been installed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package_name}: {e}")

    def remove_package(self, package_name):
        try:
            subprocess.run(["sudo", "apt-get", "remove", "-y", package_name], check=True)
            print(f"{package_name} has been removed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove {package_name}: {e}")

    def is_package_installed(self, package_name):
        try:
            result = subprocess.run(["which", package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode().strip() != ""
        except subprocess.CalledProcessError:
            return False
    
    def is_package_installed1(self, package_name):
        try:
            result = subprocess.run(["dpkg", "-s", package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "install ok installed" in result.stdout.decode()
        except subprocess.CalledProcessError:
            return False