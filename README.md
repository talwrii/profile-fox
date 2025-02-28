# Profile fox
Open tabs in certain firefox profiles from the command line.

# Installation
`pipx install profile-fox`

# Usage
First create a few profiles.

Then run: `profile-fox profile_name www.test.com`

This will open `www.test.com` in a particular profile. Note that if no URL is provided a new window will be created.

# Details
This script follows the approach suggested by toc777 on [stackoverflow](https://stackoverflow.com/questions/4679702/from-a-shell-script-open-a-new-tab-in-a-specific-instance-of-firefox), by modifying firefox's `profiles.ini` file to change the default firefox to use before running firefox. It ensure that `StartWithLastProfile` when running. `profiles.ini` is restored after this script has rile

# Edge cases

You may have problems if your `profiles.ini` file is in a strange place.
You can set the location that profile-fox looks for profiles by running `profile-fox --set-profiles`
