import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.screenshot import capture_screenshot
from src.main.visual_regression import compare_images
from src.main.report_generator import generate_report

def test_visual_regression():
    baseline_path = "tests/testdata/baseline/home.png"
    current_path = "tests/testdata/current/home.png"
    diff_path = "tests/testdata/diff/diff_home.png"
    report_path = "tests/testdata/report.html"

    url = "https://example.com"

    print("\n========== VISUAL REGRESSION TEST ==========\n")

    capture_screenshot(url, current_path, headless=True)

    if not os.path.exists(baseline_path):
        print("Baseline not found. Creating baseline image...")
        os.makedirs(os.path.dirname(baseline_path), exist_ok=True)
        os.rename(current_path, baseline_path)
        print("Baseline created successfully.\n")
        assert True
        return

    result = compare_images(baseline_path, current_path, diff_path, threshold=1.0)

    print("Comparison Result:")
    print(f"Status: {result['status']}")
    print(f"Difference Percentage: {result['difference_percentage']}%")
    print(f"Threshold: {result['threshold']}%")

    generate_report(result, baseline_path, current_path, diff_path, report_path)

    print("\nReport generated at tests/testdata/report.html")
    print("\n===========================================\n")

    assert result["status"] == "PASS"
