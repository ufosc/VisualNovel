import sys
from pathlib import Path
from zipfile import ZipFile

commit_hash = sys.argv[1]

files = Path("dist").glob('*')

for a_file in files:
    if not a_file.is_file():
        continue

    if a_file.suffix == ".zip":
        platform = a_file.stem.split("-")[-1].removesuffix(".zip")

        if platform == "win":
            print("Extracting", a_file)
            with ZipFile(a_file, 'r') as zip_ref:
                zip_ref.extractall(f"dist/BytesOfLove-{platform}-{commit_hash}")
            print("Extracted", a_file)
        else:
            # due to https://github.com/actions/upload-artifact?tab=readme-ov-file#permission-loss,
            # we don't want to extract the file in the fears of losing certain permissions
            # windows doesn't care though
            print("Renaming", a_file)
            a_file.rename(f"dist/BytesOfLove-{platform}-{commit_hash}.zip")

    elif a_file.suffix == ".bz2":
        # see above
        print("Renaming", a_file)
        a_file.rename("dist/BytesOfLove-linux-" + commit_hash + ".tar.bz2")