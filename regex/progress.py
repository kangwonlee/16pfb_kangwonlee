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

def proc_time_list(time_list):
    '''
    evaluate list of time stamps
    '''
    n = len(time_list)
    
    return n

def proc_name(arg, dirpath, name):
    if os.path.isfile(name) \
    and (name not in ("README"))\
    :
        proj_id = dirpath.split(os.sep)[1]
        key1 = proj_id
        key2 = name.lower()
        
        arg["fields"].add(key2)
        
        
        git_cmd_string = '''log %s''' % name
        #print git_cmd_string
        msg = ret.git(git_cmd_string, bVerbose=False)
        #print "len(msg) =", len(msg)
        #print msg
        
        time_list = proc_msg(msg)
        
        evaluation = proc_time_list(time_list)
        
        #print "key =", key
        if not arg.has_key(key1):
            arg[key1] = {key2: [evaluation]}
        else:
            if not arg[key1].has_key(key2):
                arg[key1][key2] = [evaluation]
            else:
                arg[key1][key2].append(evaluation)

def visit_path(arg, dirpath, namelist):
    if ".git" not in dirpath:
        org_path = os.path.abspath(os.curdir)
        d_path = os.path.abspath(dirpath)
        os.chdir(d_path)
        
        #print '-'*80
        #print os.path.abspath(os.curdir)
        #print '-'*80
        
        for name in namelist:
            proc_name(arg, dirpath, name)

        os.chdir(org_path)


def build_field_list(dict):
    field_list = list(dict['fields'])
    field_list.sort()
    return field_list

def build_table(dict):
    '''
    '''
    
    field_list = build_field_list(dict)
    
    del dict['fields']
    
    print field_list
    
    nFields = len(field_list)

    csv_fname = "progress.csv"
    
    f = open(csv_fname, 'w')

    separator = '\t'

    # column title row
    for field in field_list:
        f.write( "%c%s"%(separator,field) )
    f.write('\n')

    # proj_id row
    for proj_id in dict.iterkeys():
        # write ror
        # title column
        f.write("%s"%proj_id)
        for field in field_list:
            f.write(separator)
            if dict[proj_id].has_key(field):
                f.write(str(dict[proj_id][field]))
        f.write('\n')

    f.close()

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
    
    # initialize student directory
    student_dict = {"fields":set()}

    os.path.walk(ret.repository_local_path, visit_path, student_dict)

    pprint.pprint (student_dict)
    
    print build_table(student_dict)
