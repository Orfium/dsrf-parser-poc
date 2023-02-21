import csv
import os
from constants import SOUND_RECORDING_HEADERS, COMPOSITION_HEADERS, RECORDS, \
    COMPOSITION_RECORDS, RESOURCE_RECORDS, \
    SALES_USAGES, RELEASES


class TsvDialect(csv.Dialect):
    delimiter = '\t'
    quotechar = ''
    escapechar = '\\'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_NONE


def write_to_file(resources: dict, compositions: dict):

    for resource in resources.values():
        line = ""
        for item in resource.values():
            if item is not None:
                line += str(item)
            line += ";"

        with open(f"r_out_{os.getenv('FILE')}", "a") as file:
            file.write(f"{line[:-1]}\n")

    for composition in compositions.values():
        line = ""
        for item in composition.values():
            if item is not None:
                line += str(item)
            line += ";"

        with open(f"c_out_{os.getenv('FILE')}", "a") as file:
            file.write(f"{line[:-1]}\n")


def run():
    file = open(os.getenv("FILE"), 'rt', encoding='utf-8')

    recordings_count = 0
    compositions_count = 0
    record_reference = None
    release = []
    resources = {}
    compositions = {}

    for line in csv.reader(file, dialect=TsvDialect):
        if line[0].startswith('#'):
            continue

        record = line[0]
        dict_line = dict(zip(RECORDS[record], line[1:]))

        if record in RELEASES:
            # Initialize new block

            write_to_file(resources, compositions)
            resources = {}
            compositions = {}
            record_reference = None
            release = dict_line["ReleaseReference"]

        # Resources and Works Records. Resources: [AS05, AS06]. Works: [AS06, MW02]-------------------------------------
        if record in RESOURCE_RECORDS:
            record_reference = dict_line["ResourceReference"]
            recordings_count += 1
            isrc = "ISRC"
            if record == "AS06":
                isrc = "ResourceISRC"

            resource_info = [recordings_count,
                             dict_line["ResourceTitle"],
                             dict_line["ResourceDisplayArtistName"],
                             None,
                             dict_line[isrc],
                             0,
                             None]

            resources[record_reference] = dict(zip(SOUND_RECORDING_HEADERS, resource_info))

        if record in COMPOSITION_RECORDS:
            compositions_count += 1

            composition_info = [compositions_count,
                                dict_line["MusicalWorkTitle"],
                                dict_line["MusicalWorkComposerAuthorName"],
                                None,
                                dict_line["MusicalWorkISWC"],
                                0,
                                None]
            compositions[record_reference] = dict(zip(COMPOSITION_HEADERS, composition_info))

            # Sales/Usage Reports. Records: [SU01.02, SU02.02]----------------------------------------------------------
            if record in SALES_USAGES:
                views = "Usages"
                if record == "SU02.02":
                    views = "NumberOfStreams"

                if dict_line["TransactedResource"] in resources.keys():
                    resources[dict_line["TransactedResource"]]["Views"] += int(dict_line[views])
                if dict_line["TransactedRelease"] == release:
                    for resource in resources.values():
                        resource['Views'] += int(dict_line[views])
                    for composition in compositions.values():
                        composition['Views'] += int(dict_line[views])


if __name__ == "__main__":
    run()
