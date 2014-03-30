# -*- coding: utf-8 -*-
import re
import os
import pprint
import tempfile # Martelli, Python in a Nutsell 2nd ed, p. 223, 2006.
import urllib
import urlparse
import zipfile  # Martelli, Python in a Nutsell 2nd ed, p. 235, 2006.

git_string = r'"D:\Program Files (x86)\Git\bin\git.exe"'

repository_local_path = "data"

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
            path_under_data = os.path.join(repository_local_path, proj_id)
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
    https://dev.naver.com/projects/[proj id]/download/[????]?filename=[file name]
    
    unzip under an appropriate path
    
    setup as remote repository
    
    merge with repository
    '''
    # make temporary path
    # Martelli, Python in a Nutsell 2nd ed, p. 223, 2006.
    dest_path = tempfile.mkdtemp()
    print "download_n_sync() : dest_path =", dest_path
    
    # download page url
    download_page_url = "http://dev.naver.com/projects/%s/download" % (proj_id)

    # url to zip file
    file_path = get_intermediate_url(download_page_url)
    print "download_n_sync() : file_path =", file_path
    num_zip_list = re.findall(r"download/(.*)\?filename=(.*)", file_path)
    
    number, zip_fname = num_zip_list[0] 
    
    print "download_n_sync() : num_zip_list =", num_zip_list
    print "download_n_sync() : numeric =", number
    print "download_n_sync() : zip_file_name =", zip_fname
    
    zip_url = "http://dev.naver.com/frs/download.php/%s/%s" % (number, zip_fname)

    dest_path_fname = os.path.join(dest_path, zip_fname)
    #download file
    print "download_n_sync() : retriving %s to %s" % (zip_url, dest_path_fname)
    urllib.urlretrieve(zip_url, dest_path_fname)

    # extract zip file content    
    # http://stackoverflow.com/questions/9431918/extracting-zip-file-contents-to-specific-directory-in-python-2-7
    z = zipfile.ZipFile(dest_path_fname, 'r')
    z.extractall(dest_path)
    z.close()
    # os.rmdir(dest_path)

def parse_table(html_txt):
    '''
    content of a 2D table -> tuple of tuple
    '''
    
    # initialize table
    table_list = []
    
    # find all rows
    table_rows = re.findall("<tr.*?>(.*?)</tr>", html_txt, re.S)
    
    for table_row in table_rows:
        row_columns = re.findall("<t[dh].*?>(.*?)</t[dh]>", table_row, re.S)
        table_list.append(tuple(row_columns))
        
    return tuple(table_list)

def get_intermediate_url(url):
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
    print "get_intermediate_url() : len(txt) =", len(txt)
    
    # find all tables
    items = re.findall("<table.*?>(.*?)</table>", txt, re.S)
    
    result = ""
    
    # tables loop
    for table_item in items:
        # if this table contains .zip string
        if ".zip" in table_item:
            # find all rows
            table_tuple = parse_table(table_item)
            
            latest_row = table_tuple[1]
            anchor_string = latest_row[1]
            path_fname_list = re.findall(r'''<a\s.*?href="(.+?)"''', anchor_string, re.S)
            zip_file_url = urlparse.urljoin(url, path_fname_list[0])
            
            if ".zip" in zip_file_url:
                result = zip_file_url
                break
            
    # sample table
    '''
    (('\xeb\xa6\xb4\xeb\xa6\xac\xec\xa6\x88 \xec\x9d\xb4\xeb\xa6\x84',
      '\xed\x8c\x8c\xec\x9d\xbc\xeb\xaa\x85',
      '\xed\x81\xac\xea\xb8\xb0',
      '\xeb\x8b\xa4\xec\x9a\xb4\xed\x9a\x8c\xec\x88\x98',
      '\xeb\x82\xa0\xec\xa7\x9c'),
     ('<a href="/projects/14cpfakangwon/download/note/5919" title="140325">140325</a>',
      '<a href="/projects/14cpfakangwon/download/9335?filename=140325PFA.zip" rel="nofollow" title="140325PFA.zip">140325PFA.zip</a>',
      '71 KB',
      '1',
      '2014-03-25'))
    '''

    return zip_file_url

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
    path = os.path.join(repository_local_path, proj_id)
    clone_naver_to(proj_id, path)

def paths_under_data():
    '''
    return all subfolders under data/ folder
    '''
    raw = os.listdir(repository_local_path)
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
    url_zip = download_n_sync(r"14cpfakangwon")
    print url_zip