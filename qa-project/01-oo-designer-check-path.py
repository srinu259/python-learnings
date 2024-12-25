# do not remove the execute function
def execute(path_to_check, os_type, windows_restricted_path, linux_restricted_path):

    windows_restricted_path = windows_restricted_path.split(",")
    linux_restricted_path = linux_restricted_path.split(",")
    print(windows_restricted_path, linux_restricted_path)
    if os_type.casefold() == "windows":
        restricted_path = check_windows_restricted_path(path_to_check, windows_restricted_path)
    else:
        restricted_path = check_linux_restricted_path(path_to_check, linux_restricted_path)

    if restricted_path:
        print("{} is restricted".format(path_to_check))
        return {"result": "Not Valid", "result_string": "{} is restricted".format(path_to_check)}
    else:
        print("{} is NOT restricted".format(path_to_check))
        return {"result": "Valid", "result_string": "{} is valid".format(path_to_check)}


def check_windows_restricted_path(path, windows_restricted_path):
    # windows_restricted_path = windows_restricted_path
    if path.__contains__(".."):
        # Canonical paths are NOT supported
        return True

    for restricted_path in windows_restricted_path:

        # check for wild path
        if restricted_path.__contains__("*"):
            restricted_path = restricted_path[0:-1]
            if path.find(restricted_path) >= 0:
                return True

        if restricted_path.startswith(path):
            return True
    return False


def check_linux_restricted_path(path, linux_restricted_path):
    # linux_restricted_path = ["/", "/opt/*", "/etc"]
    if path.__contains__(".."):
        # Canonical paths are NOT supported
        return True

    for restricted_path in linux_restricted_path:

        # check for wild path
        if restricted_path.__contains__("*"):
            restricted_path = restricted_path[0:-1]
            if path.find(restricted_path) >= 0:
                return True

        if restricted_path.startswith(path):
            return True
    return False


path_to_check, os_type = "c:\\Users", "Windows"
windows_restricted_path = "c:\\,c:\\Windows*"
# linux_restricted_path = ["/","/opt/","/etc","/bin","/sbin"]
linux_restricted_path = "/,/opt/,/etc,/bin,/sbin"

print(execute(path_to_check, os_type, windows_restricted_path, linux_restricted_path))
