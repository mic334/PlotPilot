import json
import csv
from pathlib import Path

import matplotlib.pyplot as plt


def ensure_output_dir(output_dir="outputs"):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    return output_dir


def save_json(data, output_path="outputs/result.json"):
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[SAVE] JSON saved to: {output_path}")


def save_points_csv(data, output_path="outputs/points.csv"):
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True)

    rows = []

    for series in data.get("series", []):
        series_name = series.get("name", "series_1")

        for point in series.get("points", []):
            rows.append({
                "series": series_name,
                "x": point.get("x"),
                "y": point.get("y")
            })

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["series", "x", "y"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"[SAVE] CSV saved to: {output_path}")


def save_reconstructed_plot(data, output_path="outputs/reconstructed_plot.png"):
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True)

    plt.figure()

    for series in data.get("series", []):
        points = series.get("points", [])

        x = [p.get("x") for p in points]
        y = [p.get("y") for p in points]

        plt.plot(x, y, marker="o", label=series.get("name", "series_1"))

    plt.title("Reconstructed chart")
    plt.xlabel(data.get("x_axis", {}).get("label") or "x")
    plt.ylabel(data.get("y_axis", {}).get("label") or "y")
    plt.grid(True)
    plt.legend()
    plt.savefig(output_path)
    plt.close()

    print(f"[SAVE] Plot saved to: {output_path}")


def save_all_outputs(data, output_dir="outputs"):
    output_dir = ensure_output_dir(output_dir)

    save_json(data, output_dir / "result.json")
    save_points_csv(data, output_dir / "points.csv")
    save_reconstructed_plot(data, output_dir / "reconstructed_plot.png")