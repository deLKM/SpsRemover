import pyperclip
import time


class Clipboard:
    @staticmethod
    def clipboard_get() -> str:
        """Get the contents of the system's clipboard."""
        data = pyperclip.paste()
        return data

    @staticmethod
    def process_chinese(string: str) -> str:
        """Check if a given string contains Chinese characters."""
        if any("\u4e00" <= char <= "\u9fff" for char in string):
            return string.replace(" ", "")
        else:
            return string

    @staticmethod
    def clipboard_set(string: str) -> None:
        """Set the contents of the system's clipboard."""
        pyperclip.copy(string)

    def main(self):
        """Continuously check for changes in the clipboard and return them when they occur."""
        print("Clipboard monitoring started")

        recent_content = Clipboard.process_chinese(self.clipboard_get())
        while True:
            new_content = Clipboard.process_chinese(self.clipboard_get())
            if new_content != recent_content:
                recent_content = new_content
                self.clipboard_set(recent_content)

            """Check every 1ms"""
            time.sleep(0.1)


if __name__ == "__main__":
    cb = Clipboard()
    cb.main()

