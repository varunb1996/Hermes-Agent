import os


def write_file(filename, content):

    os.makedirs(
        "workspace",
        exist_ok=True
    )

    path = f"workspace/{filename}"

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)

    return path