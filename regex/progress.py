# -*- coding: utf-8 -*-
import re
import os
import pprint
import re_test as ret

if "__main__" == __name__:
    # read file
    found = ret.get_proj_id_list(ret.txt_fname)
    
    proj_id = found[4]
    
    original_path = ret.cd_proj_repo(proj_id)
    
    print os.listdir(os.curdir)
    
    os.chdir(original_path)
    
