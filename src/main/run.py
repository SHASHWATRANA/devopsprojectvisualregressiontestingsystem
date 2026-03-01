import os
from src.main.screenshot import capture_screenshot
from src.main.visual_regression import compare_images
from src.main.report_generator import generate_report

def main():
    baseline_path = "tests/testdata/baseline/home.png"
    current_path = "tests/testdata/current/home.png"
    diff_path = "tests/testdata/diff/diff_home.png"
    report_path = "tests/testdata/report.html"

    url = os.getenv("URL", "https://example.com")
    threshold = float(os.getenv("THRESHOLD", "1.0"))

    print("\n========== VISUAL REGRESSION CLI ==========\n")
    print(f"URL: {url}")
    print(f"Threshold: {threshold}%\n")

    capture_screenshot(url, current_path, headless=True)

    if not os.path.exists(baseline_path):
        os.makedirs(os.path.dirname(baseline_path), exist_ok=True)
        os.rename(current_path, baseline_path)
        print("Baseline created.")
        return

    result = compare_images(baseline_path, current_path, diff_path, threshold)
    generate_report(result, baseline_path, current_path, diff_path, report_path)

    print("Status:", result["status"])
    print("Difference:", result["difference_percentage"], "%")

if __name__ == "__main__":
    main()
