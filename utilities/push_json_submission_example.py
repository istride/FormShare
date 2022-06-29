import glob
import os

import requests
from requests.auth import HTTPDigestAuth

"""
This script uploads submissions into FormShare.
It is useful when submissions are coming from External sources like Ona
Each submission must be a directory containing the JSON and medias files. For example:
/home/me/submissions/submission_001/submission_001.json
/home/me/submissions/submission_001/image1.jpg
/home/me/submissions/submission_001/image2.jpg
/home/me/submissions/submission_002/submission_002.json
/home/me/submissions/submission_002/image1.jpg
/home/me/submissions/submission_002/image2.jpg
/home/me/submissions/submission_002/image3.jpg

path_to_submissions = /home/me/submissions/*/

"""

path_to_submissions = "/path/to/the/submissions/*/"
url_to_project = "http://localhost:5900/user/me/project/my_project"
assistant_to_use = "assistant"
assistant_password = "123"

for a_directory in glob.iglob(path_to_submissions):
    files = {}
    files_array = []
    for a_file in glob.iglob(a_directory + "*"):
        files_array.append(a_file)
        file_name = os.path.basename(a_file)
        files[file_name] = open(a_file, "rb")
    if files:
        r = requests.post(
            url_to_project + "/push_json",
            auth=HTTPDigestAuth(assistant_to_use, assistant_password),
            files=files,
        )
        print(files_array)
        print(r.status_code)
