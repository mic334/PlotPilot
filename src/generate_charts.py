import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def create_parabola(output_dir="examples"):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    x = np.linspace(-5, 5, 50)
    y = x ** 2

    df = pd.DataFrame({
        "x": x,
        "y": y
    })

    csv_path = output_dir / "parabola.csv"
    png_path = output_dir / "parabola.png"

    df.to_csv(csv_path, index=False)

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.title("Parabola")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig(png_path)
    plt.close()

    print(f"Saved: {csv_path}")
    print(f"Saved: {png_path}")


if __name__ == "__main__":
    create_parabola()