import json

from src.llm import extract_chart_data
from src.exporter import save_all_outputs
from src.compare import plot_csv_comparison


def main():
    image_path = "examples/parabola.png"

    print("[MAIN] PlotPilot started")
    print(f"[MAIN] Input image: {image_path}")

    result = extract_chart_data(image_path)

    print("[MAIN] Final parsed result:")
    print(json.dumps(result, indent=2))

    print("[MAIN] Saving outputs...")
    save_all_outputs(result)

    print("[MAIN] Done.")

    plot_csv_comparison(
    predicted_csv="outputs/points.csv",
    ground_truth_csv="examples/parabola.csv"
    )


if __name__ == "__main__":
    main()