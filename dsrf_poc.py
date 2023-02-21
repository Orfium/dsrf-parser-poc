import csv
import os
from constants import SOUND_RECORDING_HEADERS, COMPOSITION_HEADERS, HEAD_RELEASES, RECORDS, SALES_USAGES, RESOURCES


class TsvDialect(csv.Dialect):
    delimiter = '\t'
    quotechar = ''
    escapechar = '\\'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_NONE


def write_to_file(resources: dict):
    if not resources:
        return

    for resource in resources.values():
        line = ""
        for item in resource.values():
            if item is not None:
                line += str(item)
            line += ";"

        with open(f"r_out_{os.getenv('FILE')}", "a") as file:
            file.write(f"{line[:-1]}\n")


def run():
    file = open(os.getenv("FILE"), 'rt', encoding='utf-8')

    recordings_count = 0
    compositions_count = 0

    resources = {}
    release = {}

    for line in csv.reader(file, dialect=TsvDialect):
        if line[0].startswith('#'):
            continue

        record = line[0]
        dict_line = dict(zip(RECORDS[record], line[1:]))

        if record in HEAD_RELEASES:
            # Initialize new block
            write_to_file(resources)
            resources = {}
            release = {"HEAD_RELEASE": dict_line["ReleaseReference"]}

        if record in RESOURCES:
            recordings_count += 1

            resource_info = [recordings_count,
                             dict_line["Title"],
                             dict_line["DisplayArtistName"],
                             None,
                             dict_line["ISRC"],
                             0,
                             None]

            resources[dict_line["ResourceReference"]] = dict(zip(SOUND_RECORDING_HEADERS, resource_info))

        if record in SALES_USAGES:
            if dict_line["TransactedResource"] in resources.keys():
                if record == "SU01.02":
                    resources[dict_line["TransactedResource"]]["Views"] += int(dict_line["Usages"])

                if record == "SU02.02":
                    resources[dict_line["TransactedResource"]]["Views"] += int(dict_line["NumberOfStreams"])

            if dict_line["TransactedRelease"] == release["HEAD_RELEASE"]:
                for item in resources.values():
                    if record == "SU01.02":
                        item["Views"] += int(dict_line["Usages"])

                    if record == "SU02.02":
                        item["Views"] += int(dict_line["NumberOfStreams"])


if __name__ == "__main__":
    run()
