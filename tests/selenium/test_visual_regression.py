import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.screenshot import capture_screenshot
from src.main.visual_regression import compare_images

def test_visual_regression():
    baseline_path = "tests/testdata/baseline/home.png"
    current_path = "tests/testdata/current/home.png"
    diff_path = "tests/testdata/diff/diff_home.png"

    url = "https://example.com"

    capture_screenshot(url, current_path)

    if not os.path.exists(baseline_path):
        os.rename(current_path, baseline_path)
        assert True
        return

    result = compare_images(baseline_path, current_path, diff_path, threshold=1.0)

    assert result["status"] == "PASS"
