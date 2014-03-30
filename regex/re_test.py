# -*- coding: cp949 -*-
import re
import os

git_string = r'"D:\Program Files (x86)\Git\bin\git.exe"'
def proc_proj_list(found):
    '''
    process project list
    if duplicate, don't do anything
    if path does not exist, clone
    if path exists, pull
    '''
    while found:
        proj_id = found.pop()
        # check if project duplicated
        duplicate = proj_id in found
        # indicate whether project duplicated
        print get_git_naver_anon(proj_id).ljust(8 * 8)
        print "[ duplicate =", duplicate, ']'
        # if duplicated, move to the next project id
        if (not duplicate):
            # get project path
            path_under_data = os.path.join("data", proj_id)
            # if project path already exists
            if (not os.path.exists(path_under_data)):
                clone_naver_under_data(proj_id)
            else:
                pull_path(path_under_data)

# https://dev.naver.com/projects/14cpfakangwon/download/9335?filename=140325PFA.zip

def git(cmd):
    '''
    execute git command & print
    >>> git("status") # == git status
    '''
    f = os.popen(git_string + ' ' + cmd)
    print f.read()
    f.close()
    del f
    
def get_git_naver_anon(proj_id):
    '''
    argument : proj_id : project id
    return : git repository address using the project id
    
    >>> get_git_naver_anon("aaa")
    https://nobody:nobody@dev.naver.com/git/aaa.git
    '''
    return "https://nobody:nobody@dev.naver.com/git/%s.git" % proj_id

def read_txt(fname):
    f = open(fname, 'r')
    txt = f.read()
    f.close()
    del f
    return txt

def clone_naver_to(proj_id, path = ""):
    '''
    git clone project (to a path if given)
    >>> clone_naver_to ("aaa", 'a')
    '''
    full_anon_path_naver = get_git_naver_anon(proj_id)
    cmd = "clone %s %s" % (full_anon_path_naver, path)
    git(cmd)
    
def clone_naver_under_data(proj_id):
    '''
    git clone given project under data/[project id] 
    '''
    path = os.path.join("data", proj_id)
    clone_naver_to(proj_id, path)

def paths_under_data():
    '''
    return all subfolders under data/ folder
    '''
    raw = os.listdir("data")
    result_list = filter(lambda path_item: os.path.isdir(path_item), raw)
    del raw
    return result_list

def pull_path(repository_path):
    '''
    cd to repository_path
    git pull
    return to original path
    '''
    curdir_full_path = os.path.abspath(os.curdir)
    
    os.chdir(repository_path)
    git("pull --all")
    os.chdir(curdir_full_path)
    del curdir_full_path
    

if "__main__" == __name__:
    # read file
    txt = read_txt("140318PFA.txt")
    
    # regular expression 을 이용하여 관심 문자열을 찾음
    found = re.findall("https://.+[/,](.+).git", txt)
    print "len(found) =", len(found)
    proc_proj_list(found)
