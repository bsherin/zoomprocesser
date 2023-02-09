import re
import datetime
import sys
import csv


def merge_rows(frow, srow):
    nrow = frow
    nrow["end"] = srow["end"]
    nrow["duration"] = get_duration(nrow["start"], nrow["end"])
    nrow["text"] = nrow["text"] + " " + srow["text"]
    return nrow


def get_duration(start_string, end_string):
    fstring = "%H:%M:%S"
    endsecs, endmsec = re.findall("(.*?)\.(.*)", end_string)[0]
    endobj = datetime.datetime.strptime(endsecs, fstring)
    endobj = endobj + datetime.timedelta(seconds=(int(endmsec) / 1000))
    startsecs, startmsec = re.findall("(.*?)\.(.*)", start_string)[0]
    startobj = datetime.datetime.strptime(startsecs, fstring)
    startobj = startobj + datetime.timedelta(seconds=(int(startmsec) / 1000))
    ddelta = endobj - startobj
    return ddelta.total_seconds()


def do_process(file, merge=True):
    fstring = "%H:%M:%S"
    # fname = sys.argv[1]

    ftext = file.read()
    new_dlist = []

    ents = re.findall(r"(\d\d\:\d\d:\d\d\.\d\d\d) --> (\d\d\:\d\d:\d\d\.\d\d\d).*\n([^\r\n]*)[\r\n]", ftext)
    for ent in ents:
        sparse = re.findall("(.*?)\: (.*)", ent[2])
        if len(sparse) == 0:
            speaker = "empty"
            txt = ent[2]
        else:
            speaker = sparse[0][0]
            txt = sparse[0][1]

        endstring, endmsec = re.findall("(.*?)\.(.*)", ent[1])[0]
        endobj = datetime.datetime.strptime(endstring, fstring)
        endobj = endobj + datetime.timedelta(seconds=(int(endmsec) / 1000))
        startstring, startmsec = re.findall("(.*?)\.(.*)", ent[0])[0]
        startobj = datetime.datetime.strptime(startstring, fstring)
        startobj = startobj + datetime.timedelta(seconds=(int(startmsec) / 1000))
        ddelta = endobj - startobj
        new_row = {"start": ent[0],
                   "end": ent[1],
                   "duration": ddelta.total_seconds(),
                   "speaker": speaker,
                   "text": txt}
        new_dlist.append(new_row)

    if merge:
        temp_dlist = []
        prow = None
        for r in new_dlist:
            new_r = r
            if prow is None:
                prow = new_r
            elif new_r["speaker"] == prow["speaker"]:
                prow = merge_rows(prow, new_r)
            else:
                temp_dlist.append(prow)
                prow = new_r
        if prow is not None:
            temp_dlist.append(prow)
        new_dlist = temp_dlist

    outname = file.name + ".csv"
    with open(outname, 'w', newline='') as csvfile:
        fieldnames = ['start', 'end', 'duration', 'speaker', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dic in new_dlist:
            writer.writerow(dic)


if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname) as f:
        do_process(f)
