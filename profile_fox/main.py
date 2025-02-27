
import argparse
import configparser
import os
import subprocess
import time

PARSER = argparse.ArgumentParser(description='Open tab in specific firefox profile.')
PARSER.add_argument("--debug", action='store_true')
action_mx = PARSER.add_mutually_exclusive_group()
action_mx.add_argument('--set-profiles', type=str, help="Read from this page")
action_mx.add_argument('--profiles-file', action='store_true')
action_mx.add_argument('--list', action='store_true', help="List available profiles")
PARSER.add_argument("name_and_rest", type=str, nargs="*", help="Name of profile to open")

args = PARSER.parse_args()


PROFILES_PATHS = [
    os.path.expanduser("~/snap/firefox/common/.mozilla/firefox/profiles.ini"),
    os.path.expanduser("~/.mozilla/firefox/profiles.ini")
]



def main():
    profiles_path, *_ = [x for x in PROFILES_PATHS if os.path.exists(x)]

    if args.profiles_file:
        print(profiles_path)
        return

    if args.list:
        config = configparser.ConfigParser()
        config.read(profiles_path)
        for x in config.sections():
            if x.startswith("Profile"):
                print(config.get(x, "Name"))
        return

    name, *rest = args.name_and_rest

    if not name:
        raise ValueError("Must specificy a name")

    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(profiles_path)

    for run_section in config.sections():
        if config.get(run_section, "Name", fallback=None) == name:
            break
    else:
        raise ValueError(f"Could not find {name} in {profiles_path}")


    default_profile = None

    for x in config.sections():
        if not x.startswith("Profile"):
            continue

        default = config.get(x, "Default", fallback=None)
        if default == "1":
            if default_profile:
                raise Exception(f'More than one default profile in {profiles_path}')
            default_profile  = x
        elif default in ("0", None):
            pass
        else:
            raise ValueError(f"Default for profile {x} has a strange value {default!r}")

    for x in config.sections():
        if config.get(x, "Name", fallback=None) == name:
            break
    else:
        raise ValueError(f"Could not find {name} in {profiles_path}")


    use_last = config.get('General', 'StartWithLastProfile')
    disable_default(config, default_profile)
    previous_default = config.get(run_section, "Default", fallback=0)
    try:
        config.set(run_section, "Default", "1")
        config.set('General', 'StartWithLastProfile', "1")

        with open(profiles_path, 'w') as configfile:
            config.write(configfile, space_around_delimiters=False)

        if args.debug:
            print("Using profile")
            with open(profiles_path) as stream:
                print(stream.read())

        subprocess.Popen(["firefox"] + rest)
        time.sleep(0.3)
    finally:
        if previous_default is not None:
            config.set(run_section, "Default", str(previous_default))

        config.set('General', 'StartWithLastProfile', use_last)
        restore_default(config, default_profile)

        with open(profiles_path, 'w') as configfile:
            config.write(configfile, space_around_delimiters=False)


def disable_default(config, default_profile):
    config.set(default_profile, "Default", "0")

def restore_default(config, default_profile):
    config.set(default_profile, "Default", "1")
