#!/bin/bash


# PROGRAM VARIABLES
# -----------------------------------------------------------------------------
env=env
app=app.py
port=8888
reqs=requirements.txt
# -----------------------------------------------------------------------------


# COMMANDS
# -----------------------------------------------------------------------------
Setup () {
	# Creates the virtual environment for all python packages to exist
	virtualenv $env

	# Activate environment (use python binary within env)
	source $env/bin/activate

	# Install python dependencies
	$env/bin/pip install -r $reqs
}

Start () {
	# Activate environment (use python binary within env)
	source $env/bin/activate

	# Run the server
	python $app --port=$port
}

Help () {
    echo "usage: $(basename $0) <command> [<args>]"
    echo 
    echo "These are the $(basename $0) commands: "
    echo "    start     Starts the server"
    echo "    setup     Runs setup configuartion, installing dependencies"
    echo "    help      Lists the available commands"
}

Invalid () {
	echo "Incorrect usage. See '$(basename $0) --help'."
}
# -----------------------------------------------------------------------------


# PROGRAM START
# -----------------------------------------------------------------------------
# Command line parsing
while [ "$1" != "" ]; do
    case $1 in
        start )		      	shift
                            start=1
                            ;;
        setup )				setup=1
                            ;;
        help )		       	Help
                            exit
                            ;;
        * )                 Invalid
                            exit 1
    esac
    shift
done

# Check invalid cominbations
invalid=0
invalid=$invalid || ($start != 1 && $setup != 1)
invalid=$invalid || ($start == 1 && $setup == 1)
if [[ $invalid == 1 ]]; then
	Help
	exit 1
fi

# Execute
if [[ $start == 1 ]]; then
	Start
elif [[ $setup == 1 ]]; then
	Setup
fi
# -----------------------------------------------------------------------------
