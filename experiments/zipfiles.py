import zipfile
import socket
import datetime

machine = socket.gethostname()
submissions_file: str = (
    "D:\DATAexperiments\EDGAR\submissions.zip"
    if machine.upper().startswith("LANDFALL")
    else "C:\DATAexperiments\EDGAR\submissions.zip"
)

companyfacts_file: str = (
    "D:\DATAexperiments\EDGAR\companyfacts.zip"
    if machine.upper().startswith("LANDFALL")
    else "C:\DATAexperiments\EDGAR\companyfacts.zip"
)

submissions = zipfile.PyZipFile(submissions_file)
companyfacts = zipfile.PyZipFile(companyfacts_file)
submissions_extracted = [
    submissions.extract(a)
    for a in submissions.infolist()
    if datetime.datetime(*a.date_time) > datetime.datetime(2023, 9, 2)
]

companyfacts_extracted = [
    companyfacts.extract(a)
    for a in companyfacts.infolist()
    if datetime.datetime(*a.date_time) > datetime.datetime(2023, 9, 2)
]
