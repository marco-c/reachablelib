# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse

from reachablelib import perform_analysis


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", help="Paths to the index files", nargs='+', type=str, required=True)
    parser.add_argument("--source", help="Path of the source source files", type=str, required=True)
    parser.add_argument("--target", help="Path of the target source files", type=str, required=True)

    args = parser.parse_args()

    ret = perform_analysis(args.index, args.source, args.target, None)
    print(ret)


if __name__ == "__main__":
    main()
