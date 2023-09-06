import zipfile
import socket
import datetime

machine = socket.gethostname()
last_run: datetime = datetime.datetime.now() - datetime.timedelta(2)
datapath: str =  "D:\\DATAexperiments\\EDGAR"    if machine.upper().startswith("LANDFALL")    else "C:\\DATAexperiments\\EDGAR"

submissions_file: str = f"{datapath}\\submissions.zip"
companyfacts_file: str = f"{datapath}\\companyfacts.zip"

submissions = zipfile.PyZipFile(submissions_file)
companyfacts = zipfile.PyZipFile(companyfacts_file)

submissions_extracted = [
    submissions.extract(a, datapath)
    for a in submissions.infolist()
    if datetime.datetime(*a.date_time) > last_run
]



companyfacts_extracted = [
    companyfacts.extract(a, datapath)
    for a in companyfacts.infolist()
    if datetime.datetime(*a.date_time) > last_run
]

