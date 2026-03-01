from datetime import datetime
import os

def generate_report(result, baseline_path, current_path, diff_path, output_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <html>
    <head>
        <title>Visual Regression Report</title>
        <style>
            body {{ font-family: Arial; }}
            .pass {{ color: green; font-weight: bold; }}
            .fail {{ color: red; font-weight: bold; }}
            img {{ max-width: 400px; border: 1px solid #ccc; margin: 10px; }}
        </style>
    </head>
    <body>
        <h1>Visual Regression Test Report</h1>
        <p><strong>Timestamp:</strong> {timestamp}</p>
        <p><strong>Status:</strong> 
            <span class="{result['status'].lower()}">{result['status']}</span>
        </p>
        <p><strong>Difference Percentage:</strong> {result['difference_percentage']}%</p>
        <p><strong>Threshold:</strong> {result['threshold']}%</p>

        <h2>Baseline Image</h2>
        <img src="../baseline/home.png">

        <h2>Current Image</h2>
        <img src="../current/home.png">
    """

    if os.path.exists(diff_path):
        html_content += """
        <h2>Difference Image</h2>
        <img src="../diff/diff_home.png">
        """

    html_content += """
    </body>
    </html>
    """

    with open(output_path, "w") as f:
        f.write(html_content)
