import ConfigParser
import os


CONFIG_FILE = "config.ini"

# Config Parser definition
Config = ConfigParser.ConfigParser()
Config.read(CONFIG_FILE)


# This will parse the config file and extract the fields
def config_section_map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print ("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# Self explanatory
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]



