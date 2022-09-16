from re import escape, split
import os

pkg_name = "libstdc++6"
pkg_ver = "4.7.2"
print(f"Checking package: {pkg_name}-{pkg_ver}")
pkg = {pkg_name}-{pkg_ver}

if "." in pkg_name and not pkg_name.rsplit(".", 1)[-1][0].isdigit():
    p_name = escape(pkg_name.rsplit(".", 1)[0]).replace("\\|", "|")
    p_type = "|".join([escape(p.rsplit(".", 1)[-1]) for p in pkg_name.split("|")])
    if "/" in pkg:
        pkg_name = split("-[0-9.]+", pkg_name.rstrip("/").split("/")[-1])[0].split(".")[0].strip("\\/")
        pkg_type = ""
else:
    p_name = escape(pkg_name).replace("\\|", "|")
    p_type = ""

print(p_name)
print(p_type)
print("rpm -qa | grep -P \'^(%s)-[0-9.]+.*?(%s)\'" % (p_name, p_type))
print("sudo yum provides %s | grep -P \'^(%s)-[0-9.]+.*?(%s)\'" %(os.path.commonprefix(p_name.split("|")), p_name,
                                                                  p_type))