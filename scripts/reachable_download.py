# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse

from reachablelib import fetch_and_unpack_latest_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Destination path", type=str)

    args = parser.parse_args()

    data = fetch_and_unpack_latest_data(args.path)
    print(f"Downloaded data: {data}")


if __name__ == "__main__":
    main()
