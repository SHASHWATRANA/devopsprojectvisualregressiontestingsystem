from PIL import Image, ImageChops
import numpy as np
import os

def compare_images(baseline_path, current_path, diff_path, threshold=1.0):
    baseline = Image.open(baseline_path)
    current = Image.open(current_path)

    if baseline.size != current.size:
        return {
            "status": "FAIL",
            "reason": "Image dimensions mismatch",
            "difference_percentage": 100,
            "threshold": threshold
        }

    diff = ImageChops.difference(baseline, current)

    diff_array = np.array(diff.convert("L"))
    diff_pixels = np.count_nonzero(diff_array)
    total_pixels = diff_array.size

    difference_percentage = (diff_pixels / total_pixels) * 100

    if diff_pixels > 0:
        diff.save(diff_path)

    status = "PASS" if difference_percentage <= threshold else "FAIL"

    return {
        "status": status,
        "difference_percentage": round(difference_percentage, 4),
        "threshold": threshold
    }
