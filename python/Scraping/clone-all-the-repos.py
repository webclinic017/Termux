#!python

# Clone All Repos

import os
import argparse

parser = argparse.ArgumentParser(description="A python script to locate all git repositories on a filesystem and create a shell script to clone them all")
parser.add_argument("searchdir", help="Directory to search for git repositories for")
parser.add_argument("sshhostname", help="Hostname or SSH config name of the host you are cloning the repositories from")
parser.add_argument("--mr-register", action='store_true', default=False, help="If provided this will also output the script for mr register")
parser.add_argument("--create-dirs", action='store_true', default=False, help="If provided this will add a mkdir -p command in front of each git clone")
parser.add_argument("--git-clone-command",
                    help="Command used in place of git clone, will be the prefix to the repository",
                    default="git clone"
                    )

args = parser.parse_args()

clone_dir = "."


def find_all_git_repos(directory):
    for d in os.listdir(directory):
        if is_git_bare_repo(os.path.join(directory, d)):
            print_git(os.path.join(directory, d))
        elif os.path.isdir(os.path.join(directory, d)):
            find_all_git_repos(os.path.join(directory, d))


def is_git_bare_repo(directory):
    dirs_to_check = ["branches", "hooks", "info", "objects", "refs"]
    files_to_check = ["config", "description", "HEAD"]

    for dir in dirs_to_check:
        if not os.path.isdir(os.path.join(directory, dir)):
            return False

    for filename in files_to_check:
        if not os.path.isfile(os.path.join(directory, filename)):
            return False

    return True


def print_git(directory):
    dir_to_place_git_repo = directory[len(args.searchdir):].lstrip("/")
    if args.create_dirs:
        print("mkdir -p", os.path.dirname(dir_to_place_git_repo))
    print(args.git_clone_command + " " + args.sshhostname + ":" + directory + " " + dir_to_place_git_repo)
    if args.mr_register:
        print("mr register " + directory[len(args.searchdir):])


find_all_git_repos(args.searchdir)

