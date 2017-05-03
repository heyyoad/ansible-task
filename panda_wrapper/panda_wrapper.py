import shlex
import subprocess
import argparse
from utils import *

# DEFINE HELP SECTION
help_parser = argparse.ArgumentParser(
    description='''HI FOLKS! This is a simple python ansible wrapper for PANDA's apps. currently no arguments are needed/used. 
    please see the config.ini file for self explanatory, IMPORTANT! configuration options''',
    epilog="""Enjoy and use wisely :)""")
help_args = help_parser.parse_args()

# PICK CONSTS
QUESTION_OPTION_1 = 'Would you like to install One app, Few apps, or All apps? '
CHOOSE_STRING_1 = 'Choose the app you would like to install '
CHOOSE_STRING_2 = 'Choose the app you would like to install (press SPACE to mark, ENTER to continue)'

# ANSIBLE PLAYBOOK CONFIG sDEFS
work_dir = config_section_map("general")['working_directory']
pri_key = work_dir + config_section_map("ansible_defaults")['private_key']
playbook_file = work_dir + config_section_map("ansible_defaults")['playbook_base']


# TODO generalize the script for other projects
# class AnsibleWrapper(object):
#     """Main Wrapper Class."""
#     def __init__(self, app_id):
#         self.app_id = app_id
#
#     def get_apps(self):
#
#
#
# class NodeAppsWrapper(AnsibleWrapper):
#     """Wrapper for node apps"""


# Option picker function, pick_type = 0 means one pick, other means multipick
# The rest is part of the pick package
def pick_option(pick_type, rtitle, options_array):
    title = rtitle
    options = options_array
    if pick_type == 0:
        option, index = pick(options, title)
        return option
    selected = pick(options, title, multi_select=True, min_selection_count=1)
    return selected


# this allows the user to pick the apps using the pick function
def choose_deployment_apps():
    # lets get the apps folder from configuration
    node_apps_dir = work_dir + config_section_map("nodeapps")['appsfolder']
    current_apps_in_folder = get_immediate_subdirectories(node_apps_dir)

    # Show the user the apps from the folder
    print "These are the apps ready for deployment:"
    for idx, val in enumerate(current_apps_in_folder):
        print(idx, val)
    raw_input("Press Enter to continue deployment process...")

    # Starting the apps picking process
    picked_option = pick_option(0, QUESTION_OPTION_1, ['One', 'Few', 'All'])

    if picked_option == 'One':
        picked_apps = pick_option(0, CHOOSE_STRING_1, current_apps_in_folder)
    elif picked_option == 'Few':
        picked_apps = pick_option(1, CHOOSE_STRING_2, current_apps_in_folder)
    elif picked_option == 'All':
        picked_apps = current_apps_in_folder

    return picked_apps


# this will parse the picked apps to the needed format for running as playbook extra vase
def parse_apps_to_vars(rapps_to_install):
    apps = {"apps": []}
    if isinstance(rapps_to_install, list):
        for app in rapps_to_install:
            if isinstance(app, tuple):
                current_app = {"appname": [x.strip() for x in str(tuple(app)).split("'")][1]}
                apps["apps"].append(current_app)
            else:
                current_app = {"appname": str(app)}
                apps["apps"].append(current_app)
    else:
        current_app = {"appname": str(rapps_to_install)}
        apps["apps"].append(current_app)

    extra_vars = '"' + str(apps) + '"'
    return extra_vars


# this will run the playbook with the required options
def run_playbook(rparsed_apps):
    ansible_command = "ansible-playbook --private-key=" + pri_key + " -i 'base,' -e " \
                      + rparsed_apps + " " + playbook_file
    cmd_split = shlex.split(ansible_command)

    try:
        subprocess.Popen(cmd_split, cwd=work_dir)
    except subprocess.CalledProcessError as error:
        print "there's an error running ansible-playbook: " + error.output


# Main
if __name__ == '__main__':
    try:
        from pick import *
    except ImportError:
        print 'Pick is not installed, please install with "pip install pick", and then run again '
        exit(1)

    # if pick is installed we can continue with the program
    apps_to_install = choose_deployment_apps()
    parsed_apps = parse_apps_to_vars(apps_to_install)
    run_playbook(parsed_apps)
