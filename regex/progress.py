# -*- coding: utf-8 -*-
import datetime
import os
import pprint
import re
import re_test as ret
import time

def proc_msg(msg):
    '''
    identify date within each commit
    '''

    '''
    commit fc8fb8e9b3a5174303d3733e1646d53a3dc5f638
    Author: naverdev <naverdev@naver.com>
    Date:   Tue Mar 4 06:58:15 2014 +0000
    
        initialized Git repository    
    '''
    pattern_string_1 = "commit.+Author:.+Date:\s+(.*?)$.*"
    lines = msg.split('\n')
    
    result = []
    
    for line in lines:
        if "Date:" == line.strip()[:5]:
            date_string = line[5:-5].strip()

            #print date_string
            result.append( time.strptime(date_string) )
            #print result[-1]
    return tuple(result)

def proc_name(arg, dirpath, name):
    if os.path.isfile(name):
        git_cmd_string = '''log %s''' % name
        print git_cmd_string
        msg = ret.git(git_cmd_string, bVerbose=False)
        print "len(msg) =", len(msg)
        print msg
        key = dirpath, name
        if not arg.has_key(key):
            arg[key] = [msg]
        else:
            arg[key].append(msg)

def visit_path(arg, dirpath, namelist):
    if ".git" not in dirpath:
        org_path = os.path.abspath(os.curdir)
        d_path = os.path.abspath(dirpath)
        os.chdir(d_path)
        
        print '-'*80
        print os.path.abspath(os.curdir)
        print '-'*80
        
        for name in namelist:
            proc_name(arg, dirpath, name)

        os.chdir(org_path)
            

if "__main__" == __name__:
    # read file
    found = ret.get_proj_id_list(ret.txt_fname)
    
    # sample git log example
    '''git log --format="%h, %ai" [path]/[file]'''
    
    '''
    project id loop : for all project id's
        go in
        get list
        if doesn't start with '.'
            if file, get log
                # commits
                # begin ~ end
                # average commit interval
    '''
    
    proj_id = found[4]

    # change directory to project repository    
    original_path = ret.cd_proj_repo(proj_id)
    
    # initialize student directory
    student_dict = {}

    os.path.walk(os.curdir, visit_path, student_dict)

    os.chdir(original_path)
    
    pprint.pprint (student_dict.keys())
    pprint.pprint (student_dict)

    print proc_msg('''commit fc8fb8e9b3a5174303d3733e1646d53a3dc5f638
Author: naverdev <naverdev@naver.com>
Date:   Tue Mar 4 06:58:15 2014 +0000

    initialized Git repository    ''')
