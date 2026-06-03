import subprocess


def execute_python(filename):

    path = f"workspace/{filename}"

    result = subprocess.run(

        ["python", path],

        capture_output=True,

        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }