from __future__ import print_function

from pathlib import Path

import os,shutil

projects = ["FastExpressionKit", "FastExpressionKit.BulkInsert"]
version = "1.2.0.0"
def c(s):
    print(">",s)
    err = os.system(s)
    assert not err

def nuke(pth):
    if os.path.isdir(pth):
        shutil.rmtree(pth)

startdir = Path(".").absolute()

for prjdir in projects:
    os.chdir(startdir / prjdir)
    nuke("bin")
    nuke("obj")

    def pack():
        c(f"dotnet pack -c Release /p:Version={version} /p:PubVer={version}")

    pack()
