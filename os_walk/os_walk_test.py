import os
# this demo is to test os.path.walk()
#   that will visit every folder under
#       specified path
#   and call following function

ext_of_interest = (".ico", ".py")

def callback(arg, dirpath, namelist):
    # for each name in namelist
    for filename in namelist:
        # path_name = path + '\' + name
        path_name = os.path.join(dirpath, filename)

        # splitext() : filename = name.ext -> name, .ext
        n, ext = os.path.splitext(filename)

        # if file's extension is one of our interests
        if ext in ext_of_interest:
            # add the path_name to the big list
            arg.append(path_name)

spec_path = "c:\msysgit"

big_list = []

os.path.walk(spec_path, callback, big_list)

print big_list
