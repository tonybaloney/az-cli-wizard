from rich.progress import track
import inquirer
import re
import subprocess
import json


def _az_cli_json(cmd):
    _cmd = subprocess.run(cmd, capture_output=True, shell=True)
    if _cmd.returncode != 0:
        print("Please configure the az CLI first:")
        print(_cmd.stderr)
        exit()

    return json.loads(_cmd.stdout)


def get_locations():
    return _az_cli_json("az account list-locations --output json")


def get_runtimes():
    return _az_cli_json("az webapp list-runtimes --linux --output json")


def main():
    locations = get_locations()
    runtimes = get_runtimes()
    questions = [
        inquirer.Text("name", message="Application Name"),
        inquirer.Text("description", message="Brief description of your app"),
        inquirer.List(
            "location",
            message="Which Azure Datacenter?",
            choices=[location["displayName"] for location in locations],
        ),
        inquirer.List(
            "runtime",
            message="Which Application Runtime?",
            choices=runtimes,
        ),
    ]
    answers = inquirer.prompt(questions)
    print(answers)
