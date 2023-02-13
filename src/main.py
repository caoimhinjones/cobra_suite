# Need sys for arguments
import sys

# Import root modules
import modules.check_version

# Main Script
if __name__ == '__main__':

    ##################################################################
    #
    # Arguments
    #
    ##################################################################

    # Get Command name - e.g. docker run -rm cobra COMMAND_NAME
    if len(sys.argv) > 1:
        command_name = sys.argv[1]
    else:
        command_name = ""

    ##################################################################
    #
    # Determine program path based on command_name
    #
    ##################################################################

    # cobra version
    if command_name == "cobra_version":
        modules.check_version.check_cobra_version()

    # python_version
    else:
        modules.check_version.check_python_version()
