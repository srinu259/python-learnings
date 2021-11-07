import re

subHostNames = [
    {
        "name": "master",
        "hostNames": ["MASTER2", "MASTER3"]
    },
    {
        "name": "worker",
        "hostNames": ["WORKER1", "WORKER2", "WORKER3"]
    }
]

nfs = {
    "nfsHostName": "pso-12-126.sac.swinfra.net",
    "nfsMountpoint": "/var/vols/itom"
}

for subHost in subHostNames:
    if "worker1" in subHost["name"].lower():
        print(subHost["name"])
        print("No worker on master")


# {%- for subHost in prd.target.subHostNames if "master" in subHost.name|lower -%}
# scenario - 1:
#   subHostNames is EMPTY, then its an evaulation mode, run setupNFS.sh
# scenario - 2:
#   subHostNames Master is EMPTY and primary-master name matches to nfsHostName, run setupNFS.sh
# scenario -3 :
#   subHostNames Master is NOT EMPTY, do not run setupNFS.sh

subHostNames = []
primary_master = "pso-12-126.sac.swinfra.net"

nfs1 = {
    "nfsHostName": "pso-12-126.sac.swinfra.net",
    "nfsMountpoint": "/var/vols/itom"
}

if subHostNames:
    print("1.Just run setupNFS.sh")

for subHost in subHostNames:
    if not "master" in subHost["name"].lower() and nfs["nfsHostName"] == primary_master:
        print("Just run setupNFS.sh")
    else:
        print("Not a self-hosted NFS")

# for subHost in linux.target.subHostNames if not 'master' in subHost.name and linux.target.nfs.nfsHostName == linux.target.hostNames[0]:
#     nfs_script = "setupNFS.sh"

if len(subHostNames) == 0:
    nfs_script = "setupNFS.sh"
else:
    nfs_script = "echo 'Not self hosted NFS'"

print(nfs_script)

success_keys = [
    "Exposing the folder|Not self hosted NFS|The NFS service was installed successfully|The NFS service was found to be already installed."
]

cmd_output = "a" \
             "b" \
             "c" \
             "Exposing the folder" \
             "d"

for pattern in success_keys:
    if not re.search(pattern, cmd_output):
        print(pattern)

# nginx template
loadBalancerTraffic = [
            { "name": "apphub",
              "port": 5443,
              "targetHost": ["master1", "master2", "worker1", "worker2", "worker3"],
              "targetPort": 32626
              },
            {  "name": "suite",
               "port": 3000,
               "targetHost": ["master1", "master2", "worker1", "worker2", "worker3"],
               "targetPort": 3000
               }
        ]

for traffic in loadBalancerTraffic:
    print(traffic["name"], traffic["port"], traffic["targetPort"])
    for trafficHost in traffic["targetHost"]:
        print(trafficHost)

#yum command
options = ""
out = "--skip-broken --refresh --allowerasing --nobest"
for opt in ["--skip-broken", "--refresh", "--allowerasing", "--nobest"]:
    if opt in str(out):
        options = options + " " + opt
command = "sudo yum update -y" + options
print(command)

