import subprocess

def install_dependencies():
    packages = ["selenium==4.0.0", "webdriver_manager"]
    for package in packages:
        subprocess.check_call(["python", "-m", "pip", "install", package])

if __name__ == "__main__":
    install_dependencies()
