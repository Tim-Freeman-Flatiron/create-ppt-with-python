import subprocess

namespaces = ["1stdibs_uk", "converse_be", "converse_es", "converse_es_spanish", "converse_it", "converse_it_italian", "converse_nl", "converse_nl_dutch", "vans_ca"]
path = "/src/integrations/manifests/"
base_manifest = ".build.manifest"
old = "$INCLUDE triggermail_core.js$"
new = "$INCLUDE common/vanillajs/triggermail_core.js$"
modified = []

for namespace in namespaces:
    file_name = path + namespace + base_manifest
    try:
        with open(file_name, "r") as file:
            print("editing {}").format(file_name)
            content = file.read()
            file.close()

            output = open(file_name, "w")
            output.write(content.replace(old, new))
            output.close()

            modified.append(namespace)
    except:
        print("no such file named {}").format(file_name)
        pass

print("edited the build manifest of {} namespaces").format(len(modified))

watch_command = "python /src/integrations/tools/watch_js.py --once "

for namespace in modified:
    watch_namespace = watch_command + namespace
    subprocess.check_call(watch_namespace.split())
