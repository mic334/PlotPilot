import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_csv_comparison(
    predicted_csv="outputs/points.csv",
    ground_truth_csv="examples/parabola.csv",
    output_path="outputs/comparison_plot.png"
):
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True)

    pred = pd.read_csv(predicted_csv)
    true = pd.read_csv(ground_truth_csv)

    plt.figure()

    plt.plot(
        true["x"],
        true["y"],
        label="Ground truth",
        linewidth=2
    )

    plt.plot(
        pred["x"],
        pred["y"],
        marker="o",
        linestyle="--",
        label="LLM extracted points"
    )

    plt.title("Ground truth vs LLM extracted points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    plt.savefig(output_path)
    plt.close()

    print(f"[COMPARE] Comparison plot saved to: {output_path}")