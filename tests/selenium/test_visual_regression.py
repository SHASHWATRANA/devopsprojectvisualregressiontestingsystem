import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.screenshot import capture_screenshot

def test_capture():
    save_path = "tests/testdata/current/home.png"
    capture_screenshot("https://example.com", save_path)

    assert os.path.exists(save_path)
