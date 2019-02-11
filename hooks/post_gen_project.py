import os
from shutil import which
from subprocess import Popen, PIPE


def cleanup_requirements_file(file_name, items_to_remove):
    with open(file_name, "r") as fh:
        data = fh.read()
    os.remove(file_name)
    data = data.split("\n")
    data = [d for d in data if d not in items_to_remove]
    with open(file_name, "w") as fh:
        fh.write("\n".join(data))


dependencies_to_remove = []

for req_type in ["", "-dev"]:
    cleanup_requirements_file("requirements{}.txt".format(req_type), dependencies_to_remove)

if which("black"):
    process = Popen(["black", "."], stderr=PIPE, stdout=PIPE)
    _, _ = process.communicate()

if which("isort"):
    process = Popen(["isort", "-rc", "."], stdout=PIPE, stderr=PIPE)
    _, _ = process.communicate()
