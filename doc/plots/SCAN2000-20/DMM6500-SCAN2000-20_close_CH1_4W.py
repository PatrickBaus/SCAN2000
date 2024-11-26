import pandas as pd
import matplotlib
import seaborn as sns

colors = sns.color_palette("colorblind")
phi = (5**0.5 - 1) / 2  # golden ratio

plot = {
    "description": None,
    "title": "Keithley DMM6500 SCAN2000-20 close CH1 4W",
    "show": True,
    "output_file": None,
    'crop': {
        "crop_index": "date",
        "crop_range": None,
    },
    "legend_position": "upper left",
    "crop_secondary_to_primary": True,
    "plot_size": (10, 3),
    "primary_axis": {
        "axis_settings": {
            "x_label": r"Time in \unit{\s}",
            "y_label": None,
            "invert_x": False,
            "invert_y": False,
            "y_fixed_order": None,
            "x_fixed_order": -6,
            "x_scale": "lin",
            "y_scale": "lin",
            "grid": {
                "visible": False,
            }
        },
        "x-axis": "date",
        "plot_type": "absolute",
        "use_downsampling": False,
        "columns_to_plot": {
            "D0": {
                "plot_type": "plot",
                "settings": {
                    "label": r"CLK",
                    "color": colors[0],
                    "linewidth": 1,
                    "marker": "",
                    "drawstyle": "steps-pre",
                }
            },
            "D2": {
                "plot_type": "plot",
                "settings": {
                    "label": r"Data",
                    "color": colors[3],
                    "linewidth": 1,
                    "marker": "",
                    "drawstyle": "steps-pre",
                }
            },
            "D1": {
                "plot_type": "plot",
                "settings": {
                    "label": r"LATCH",
                    "color": colors[2],
                    "linewidth": 1,
                    "marker": "",
                    "drawstyle": "steps-pre",
                }
            },
        },
    },
    "files": [
        {
            "filename": "SCAN2000-20/data/DMM6500-SCAN2000-20_close_CH1_4W.csv",
            "show": True,
            "parser": "generic_parser",
            "options": {
                "skiprows": 22,
                "columns": {
                    0: "date",
                    1: "D7",
                    2: "D6",
                    3: "D5",
                    4: "D4",
                    5: "D3",
                    6: "D2",
                    7: "D1",
                    8: "D0",
                },
                "scaling": {
                    "D0": lambda data: data["D0"] * 0.9 - 0,
                    "D1": lambda data: data["D1"] * 0.9 - 2,
                    "D2": lambda data: data["D2"] * 0.9 - 1,
                },
            },
        },
    ],
}