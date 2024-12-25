import pywinauto
import winrm

def main():
    """
    Logs in to a Windows VM using winrm and installs OpenText InfoArchive.
    """
    # Connect to the Windows VM using winrm.
    # server = "16.32.12.154"
    # domain = "CORPDOM"
    # username = "administrator"
    # password = "Cloud_123"
    # port = 5985
    server = "16.32.12.112"
    domain = "CORPDOM"
    username = "romie"
    password = "Administrator123!"
    port = 5985


    session = winrm.Session(server, auth=('{}@{}'.format(username,domain), password), transport='ntlm')
    result = session.run_cmd('ipconfig', ['/all']) # To run command in cmd
    result = session.run_ps('Get-Acl') # To run Powershell block


# host = 'YourWindowsHost'
# domain = 'YourDomain'
# user = 'YourDomainUser'
# password = 'YourPassword'
#
# session = winrm.Session(host, auth=('{}@{}'.format(user,domain), password), transport='ntlm')
# result = session.run_cmd('ipconfig', ['/all']) # To run command in cmd
# result = session.run_ps('Get-Acl') # To run Powershell block
#
#     with winrm.Session(server, auth=(username, password), port=port) as session:
#             # Install OpenText InfoArchive.
#             session.run_cmd("msiexec /i opentext-infoarchive-installer.msi")


if __name__ == "__main__":
    main()
