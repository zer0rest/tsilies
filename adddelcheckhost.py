# This script is responsible for adding new hosts, deleting old hosts and checking
# the JSON file to ensure that no fields are left empty or contain invalid data.

# Import the sys module, used to receive cmd arguments.
import sys

# Import the re modulr used to do pattern matching when parsing the arguments
import re

# Import the os module used to read enviroment variables.
import os

# Define a variable to store the help message.
HELP_MSG = """ This script is used to add/delete new hosts from the hosts.json file.
    Options:
    -add: This flag uses the addHost() function to add new hosts.
    If the -env variable is used the function retrieves the values from environment variables instead of the STDIN.
    Parameters:
        -host: The nickname of the new host.
        -loc: The location of the new host.
        -hown: The individual/team that owns this host and will be notified on status changes.
        -4addr: The IPv4 address of the host.
        -6addr: The IPv6 address of the host.
        -mag: The monitoring agent(s) responsible for monitoring the host.
        -aldown: The alert method(s) used to alert the host owner when the host changes status to down.
        -alup: The alert method(s) used to alert the host owner when the host changes status to up.
        -grace: The period in seconds, the platform needs to wait before alerting the host owners.
    -del: This flag uses the delHost() function to delete old hosts.
    Parameters:
        -host: The nickname of the host to be deleted.
    -help / -h: This flag prints this help message.
            """


# Initialise the argument variables.
HOSTNAME = "NULL"
LOCATION = "NULL"
HOST_OWNER = "NULL"
HOST_V4 = "NULL"
MONITOR_AGENT = "NULL"
HOST_V6 = "NULL"
ALERT_METHOD_DOWN = "NULL"
ALERT_METHOD_UP = "NULL"
GRACE_PERIOD = "NULL"

# Define the variable used to store the arguments array.
ARGUMENTS = sys.argv

# Define the variable used to store the arguments count.
# We subtract one, cause the first argument is the name of the script itself.
ARG_COUNT = len(sys.argv) - 1

# If the flag is -add, then choose the addHost() function.
if ARGUMENTS[1] == "-add":
    # If the -env parameter is set, retrieve the data from enviroment variables.
    if "-env" in ARGUMENTS:
        # Make sure that all enviroment variables have values and are not empty.
        #If everything is okay, load the enviroment variable value to the respective local variable.
        if os.environ['HOST']:
            HOST = os.environ["HOST"]
        else:
            print "Host enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["GRACE_PERIOD"]:
            GRACE_PERIOD = os.environ["GRACE_PERIOD"]
        else:
            print "Grace Period variable has no value, exiting."
            sys.exit(1)

        if os.environ["HOST_OWNER"]:
            HOST_OWNER = os.environ["HOST_OWNER"]
        else:
            print "Host Owner enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["LOCATION"]:
            LOCATION = os.environ["LOCATION"]
        else:
            print "Location enviroment variable has no value, exiting."
            sys.exit(1)

        # Make sure that all enviroment variables have values and are not empty.
        if os.environ["MONITORING_AGENT"]:
            HOST = os.environ["MONITORING_AGENT"]
        else:
            print "Monitoring agent enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["HOST_V4"]:
            HOST_v4 = os.environ["HOST_V4"]
        else:
            print "Host IPv4 address enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["HOST_V6"]:
            HOST_V6 = os.environ["HOST_V6"]
        else:
            print "Host IPv6 address enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["ALERT_METHOD_DOWN"]:
            ALERT_METHOD_DOWN = os.environ["ALERT_METHOD_DOWN"]
        else:
            print "Alert Method Down enviroment variable has no value, exiting."
            sys.exit(1)

        if os.environ["ALERT_METHOD_UP"]:
            ALERT_METHOD_UP = os.environ["ALERT_METHOD_UP"]
        else:
            print "Alert Method Up enviroment variable has no value, exiting."
            sys.exit(1)

    else:
        # Check what parameter is passed and load its' value to the respective variable.
        if "-host" in ARGUMENTS:
            POS = ARGUMENTS.index("-host")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Host argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Host argument has no value, exiting"
                sys.exit(1)
            else:
                HOSTNAME = ARGUMENTS[POS+1]

        if "-loc" in ARGUMENTS:
            POS = ARGUMENTS.index("-loc")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Location argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Location argument has no value, exiting"
                sys.exit(1)
            else:
                LOCATION = ARGUMENTS[POS+1]

        if "-hown" in ARGUMENTS:
            POS = ARGUMENTS.index("-hown")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Host Owner argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Host Owner argument has no value, exiting"
                sys.exit(1)
            else:
                HOST_OWNER = ARGUMENTS[POS+1]

        if "-mag" in ARGUMENTS:
            POS = ARGUMENTS.index("-mag")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Monitoring agent argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Monitoring Agent argument has no value, exiting"
                sys.exit(1)
            else:
                MONITOR_AGENT = ARGUMENTS[POS+1]

        if "-4addr" in ARGUMENTS:
            POS = ARGUMENTS.index("-4addr")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Host IPv4 Address argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Host IPv4 Address argument has no value, exiting"
                sys.exit(1)
            else:
                HOST_V4 = ARGUMENTS[POS+1]

        if "-6addr" in ARGUMENTS:
            POS = ARGUMENTS.index("-6addr")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Host IPv6 Address argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Host IPv6 Address argument has no value, exiting"
                sys.exit(1)
            else:
                HOST_V6 = ARGUMENTS[POS+1]

        if "-aldown" in ARGUMENTS:
            POS = ARGUMENTS.index("-aldown")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Alert down argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Alert down argument has no value, exiting"
                sys.exit(1)
            else:
                ALERT_METHOD_DOWN = ARGUMENTS[POS+1]

        if "-alup" in ARGUMENTS:
            POS = ARGUMENTS.index("-alup")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Alert up argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Alert up Argument has no value, exiting"
                sys.exit(1)
            else:
                ALERT_METHOD_UP = ARGUMENTS[POS+1]

        if "-grace" in ARGUMENTS:
            POS = ARGUMENTS.index("-grace")
            # If the argument is the last argument passed, there is no need to check for
            # another argument.
            if POS == ARG_COUNT:
                print "Grace period argument has no value, exiting"
                sys.exit(1)
            # We add 1 cause the value of the argument is right after the argument itself, in the array.
            # If the next item in the array is a command, no value has been passed to the previous argument
            elif re.match("(^-(host|loc|hown|mag|4addr|6addr|grace|aldown|alup))", ARGUMENTS[POS+1]):
                print "Grace period argument has no value, exiting"
                sys.exit(1)
            else:
                GRACE_PERIOD = ARGUMENTS[POS+1]



# If the flag is -del, then choose the delHost() function.
elif ARGUMENTS[1] == "-del":
    # Check if the enviroment flag is set. If that's the case,
    if "-env" in ARGUMENTS:
    # Make sure that all enviroment variables have values and are not empty.
    #If everything is okay, load the enviroment variable value to the respective local variable.
        if os.environ['HOST_DEL']:
            HOST = os.environ["HOST_DEL"]
        else:
            print "Host-to-be-deleted enviroment variable has no value, exiting."
            sys.exit(1)
    else:
        if "-host" in ARGUMENTS:
            HOST = ARGUMENTS[3]

# If the flag is -chk, then choose the checkHost() function.
elif ARGUMENTS[1] == "-chk":
    print "check"

# If the flag is -help or -h, print the help message.
elif ARGUMENTS[1] == "-help":
    print HELP_MSG

# Otherwise there is an error so notify the user and exit with status code 1
else:
    print "error"
    sys.exit(1)

# STATUS = ""
# LAST_DOWN = ""

# Create the function used to add new JSON "host" objects to hosts.json
# def addHost():
#     with open("hosts.json", "r+") as hostfile:
#         # Load the list of objects into a var
#         # In Python's terms the objects in hosts.json are translated to a list of
#         # python dictionaries.
#         hosts = json.load(hostfile)
#     #test host info dictionary
#     #host_inf = {"hostname":"edgerouter01", "location":"lamdc01", "host-owner":"zer0net-noc",
#     #            "monitor-agent":"agent-1", "host-v4":"10.0.20.1", "host-v6":"NULL",
#     #            "alert-method-down":"email-message", "alert-method-up":"sms-message", "grace-period":"0s",
#     #            "status":"up", "last-down":"1530248404"}
#     # Receive the message containing the host info and store it in a variable.
#     hostinfo = str(message.payload)
#     # Create dictionary where host information will be added to append to the json
#     # file.
#     newdata = {}
#     newdata['hostname'] = host_inf['hostname']
#     newdata['location'] = host_inf['location']
#     newdata['host-owner'] = host_inf['host-owner']
#     newdata['monitor-agent'] = host_inf['monitor-agent']
#     newdata['host-v4'] = host_inf['host-v4']
#     newdata['host-v6'] = host_inf['host-v6']
#     newdata['alert-method-down'] = host_inf['alert-method-down']
#     newdata['alert-method-up'] = host_inf['alert-method-up']
#     newdata['grace-period'] = host_inf['grace-period']
#     newdata['status'] = host_inf['status']
#     newdata['last-down'] = host_inf['last-down']
#
#     # Append the dictionary containing information about the new host to the list
#     # of dictionaries.
#     hosts.append(newdata)
#
#     # Load the new object to the hosts.json file
#     # The indent=4 parameter is used to make the hosts.json file more readable.
#     # To do that it adds 4 spaces aka a 'Tab' before on new line.
#     with open("hosts.json", "r+") as hostfile:
#         json.dump(hosts, hostfile, indent=4, sort_keys=True)
# addHost()