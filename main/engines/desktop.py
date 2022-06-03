import ctypes
import platform
import subprocess
from abc import ABC, abstractmethod


class BaseDesktop(ABC):
    @abstractmethod
    def change_wallpaper(self, image_path: str) -> None:
        pass


class MacDesktop(BaseDesktop):
    def change_wallpaper(self, image_path: str) -> None:
        script = f"""/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "{image_path}"
        end tell
        END"""

        subprocess.Popen(script, shell=True)
        subprocess.call(["killall Dock"], shell=True)


class WindowsDesktop(BaseDesktop):
    def change_wallpaper(self, image_path: str) -> None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)


def _change_desktop_wallpaper(desktop: BaseDesktop, image_path: str) -> None:
    desktop.change_wallpaper(image_path)


def change_desktop_wallpaper(image_path: str) -> None:
    platform_name = platform.system()

    if platform_name == "Darwin":
        _change_desktop_wallpaper(MacDesktop(), image_path)
    elif platform_name == "Windows":
        _change_desktop_wallpaper(WindowsDesktop(), image_path)
