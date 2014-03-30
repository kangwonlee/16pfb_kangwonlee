# -*- coding: utf-8 -*-
import re
import os
import urllib
import urlparse

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
def download_n_sync(proj_id):
    '''
    read project download page
    http://dev.naver.com/projects/[proj id]/download
    
    find file name (using re)
    
    download zip file to a specified path
    https://dev.naver.com/projects/[proj id]/download/9335?filename=[file name]
    
    unzip under an appropriate path
    
    setup as remote repository
    
    merge with repository
    '''
    
    download_page_url = "http://dev.naver.com/projects/%s/download" % (proj_id)

    filename = get_filename(download_page_url)
    
    file_path = "https://dev.naver.com/projects/%s/download/9335?filename=%s" %(proj_id, filename)
    
def get_filename(url):
    '''
    get .zip filename from the download page of the project
    '''
    # download page string sample
    '''
    <table>
        <td></td>
        <td><a [path to file]> filename </a></td>
    </table>
    '''
    f = urllib.urlopen(url)
    txt = f.read()
    f.close()
    del f
    print "get_filename() : len(txt) =", len(txt)
    
    # find all tables
    items = re.findall("<table.*?>(.*?)</table>", txt, re.S)
    
    # tables loop
    for table_item in items:
        # if this table contains .zip string
        if ".zip" in table_item:
            # find all rows
            table_rows = re.findall("<tr.*?>(.*?)</tr>", table_item, re.S)
            for table_row in table_rows:
                print "get_filename() : table_row = %s" % (table_row)

    print "get_filename() : len(items) =", len(items)
    print ".zip" in items[0]
    return "not done yet"

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
    
    # regular expression �� �̿��Ͽ� ��� ���ڿ��� ã��
    found = re.findall("https://.+[/,](.+).git", txt)
    print "len(found) =", len(found)
    #proc_proj_list(found)
    url_zip = get_filename(r"http://dev.naver.com/projects/14cpfakangwon/download")
    print url_zip