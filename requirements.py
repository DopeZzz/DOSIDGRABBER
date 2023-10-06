import subprocess

def install_dependencies():
    packages = ["requests", "beautifulsoup4"]
    for package in packages:
        subprocess.check_call(["python", "-m", "pip", "install", package])

if __name__ == "__main__":
    install_dependencies()
