#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

def generic_parser(filename, options, **kwargs):
    data = (
        pd.read_csv(
            filename,
            comment="#",
            header=None,
            skiprows=options.get("skiprows", 1),
            delimiter=options.get("delimiter", ","),
            usecols=options["columns"].keys(),
            names=options["columns"].values(),
        )
        .assign(**options.get("scaling", {}))
    )

    return data


FILE_PARSER = {
  "generic_parser": generic_parser
}


def parse_file(parser, filename, **kwargs):
    return FILE_PARSER[parser](filename=filename, **kwargs)
