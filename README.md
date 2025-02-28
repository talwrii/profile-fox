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

# About me
I am @readwithai. I make tools related to [reading](https://readwithai.substack.com/p/what-is-reading-broadly-defined), research and [agency](https://readwithai.substack.com/p/reading-and-agency
) sometimes using [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian).

I have a habit of making linux productivity tools. You can read about them [here](https://readwithai.substack.com/s/technical-miscellany).

You might be interested in:

1. [curlfire](https://github.com/talwrii/curlfire), a tool to use firefox cookies from the command line
2. [zshnip](https://github.com/facetframer/zshnip) a command line snippet for zsh.
3. Reading by summary of [Note take in Obsidian](https://readwithai.substack.com/p/note-taking-with-obsidian-much-of).

You can follow me on [X](https://x.com/readwithai) or my [blog](https://readwithai.substack.com/).
