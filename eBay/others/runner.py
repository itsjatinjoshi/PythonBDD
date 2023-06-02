import argparse
import os
import pathlib
import platform
import subprocess
from datetime import datetime


def add_web_driver_path():
    print("Adding Webdriving to the Path.")
    current_fir_path = pathlib.Path(__file__).parent.absolute()

    if platform.system() == 'Darwin':
        webdriver_path = os.path.join(current_fir_path, 'webdrivers', 'mac')
    elif platform.system() == 'Windows':
        webdriver_path = os.path.join(current_fir_path, 'webdrivers', 'windows')
    elif platform.system() == 'Linux':
        webdriver_path = os.path.join(current_fir_path, 'webdrivers', 'linux')
    else:
        raise Exception("Unknown platform, Unable to add webdrivers to path")

    current_path = os.environ['PATH']
    new_path = webdriver_path+';'+current_path
    os.environ['PATH'] = new_path

def get_unique_run_id():
    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    elif os.environ.get("CUSTOM_BUILD_NUMBER"):
        unique_run_id = os.environ.get("CUSTOM_BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime('%Y%m%d%H%M%S')

    os.environ["UNIQUE_RUN_ID"] = unique_run_id

    return unique_run_id


def create_output_dir(prefix='result_'):
    global run_id
    if not run_id:
        raise Exception("Variable 'Run ID' is no available. Unable to create a folder")
    current_fir_path = pathlib.Path(__file__).parent.absolute()
    dir_to_create = os.path.join(current_fir_path, prefix + str(run_id))
    os.mkdir(dir_to_create)

    print('Created Output directory: ', dir_to_create)

    return dir_to_create


if __name__ == '__main__':
    run_id = get_unique_run_id()
    print(run_id)
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=False, help="Location of the script file")
    parser.add_argument('--behave_options', type=str, required=False, help="String for behave Option."
                                                                           " E.g tags like '-t <tag name>")

    args = parser.parse_args()
    test_dir = args.test_dir
    behave_options = '' if not args.behave_options else args.behave_options

    output_dir = create_output_dir()
    json_output_dir = os.path.join(output_dir, 'json_report_out.json')
    junit_output_dir = os.path.join(output_dir, 'junit_report_out.json')

    command = f'behave -k --no-capture ' \
              f'-f json.pretty -o {json_output_dir} ' \
              f'--junit --junit-directory {junit_output_dir}' \
              f'{behave_options} ' \
              f'{test_dir}'

    print("Running Command : ", command)

    response = subprocess.run(command, shell=True)
