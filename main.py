import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


class Plot:

    def __init__(self, json_file):
        self.df = pd.read_json(json_file)
        self.save_dir = Path('plots')

    def draw_plots(self):

        plot_paths = []

        if self.save_dir.is_dir():
            for file in self.save_dir.iterdir():
                file.unlink()

        self.save_dir.mkdir(exist_ok=True)

        for column in self.df.columns[3:]:
            plt.figure(visible=False)
            plt.title(column)
            self.df.plot(x='name', y=column)
            plot_path = self.save_dir / f'{column}.png'
            plt.savefig(plot_path)
            plot_paths.append(plot_path)
            plt.close()
        return plot_paths


if __name__ == '__main__':
    plotter = Plot('deviation.json')
    paths = plotter.draw_plots()
    print('Plots saved in "plots" directory')
