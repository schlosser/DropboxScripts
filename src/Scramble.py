""" 
File -- Scramble.py
Creator -- Dan Schlosser
Date -- 1/9/13
Description -- **TODO**

"""

import os
import zipfile

def main():
    """Copies all .jpg files to folders with 'YYYY-MM' labels.
    
    """
    choice = input('Enter value (1 or 2):')
    
    if choice == 1:
        package(os.getcwd())
        print "Scrambling successful."
    else:
        unpackage(os.getcwd())
        print "Unscrambling successful."

# ||-------------------------------------------------------------------------||
# ||-Packaging---------------------------------------------------------------||
# ||-------------------------------------------------------------------------||

def package(p):
    """Appropriately scrambles and zips all files, folders, and subfolders
    recursively.
    
    Arguments:
    p -- The pathname to be packaged
    
    """
    os.chdir(p)
    print "cwd:", os.getcwd()
    if not cwdIsValid(True): return     
    
    dontZipTypes = ['py', 'db'] # Not to be included in zip archives
    zipName = sScramble(os.getcwd().rsplit('\\', 1)[1].lstrip('rec_'))+'.db'
    zip = zipfile.ZipFile(zipName,'w')
    zipIsEmpty = True
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(path):
            package(path)  # Recursive call to subfolders
            os.chdir(os.path.realpath(p))
            print "cwd:", os.getcwd()
            newPath = scrDirName(path)
            print 'Making:', newPath, 'from',path
            os.rename(path, newPath)
        elif not validExtension(path, dontZipTypes):
            zipIsEmpty = False
            newPath = scrFileName(path)
            os.rename(path, newPath)
            print "Writing:", newPath
            zip.write(newPath)
            print "Deleting:", newPath
            os.remove(newPath)
    zip.close()
    if zipIsEmpty:
        print "Removing:", zipName
        os.remove(zipName)

def unpackage(p):
    """Appropriately unzips '.db' files, and unscrambles afiles, folders, and 
    subfolders recursively.
    
    Arguments:
    p -- The pathname to be unpackaged
    
    """
    fileTypes = ['py', 'jpg', 'exe', 'html', 'ico', 'png', 'ini', 'txt', 'nsh',
                 'dll', 'chm'] # Supported for scrambling.
    
    os.chdir(p)
    print "cwd:", os.getcwd()
    if not cwdIsValid(False): return
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(path):
            newPath = unscrDirName(path)
            print 'Making:', newPath, 'from',path
            os.rename(path, newPath)
            unpackage(newPath)  # Recursive call to subfolders
            os.chdir(p)
            print "cwd:", os.getcwd()
        elif validExtension(path, ['.db']):
            newPath = unscrFileName(path.rstrip('.db'))+'.zip'
            os.rename(path, newPath)
            print "Extracting:", newPath
            zip = zipfile.ZipFile(newPath)
            zip.extractall()
            zip.close()
            print "Deleting:", newPath
            os.remove(newPath)
    for path in os.listdir(os.getcwd()):
        if os.path.isfile(path) and validExtension(sUnscramble(path), fileTypes):
            newPath = unscrFileName(path)
            os.rename(path, newPath)
            
            
# ||-------------------------------------------------------------------------||
# ||-Checking----------------------------------------------------------------||
# ||-------------------------------------------------------------------------||

def cwdIsValid(scrambling):
    """Indicates whether or not the current working directory (cwd) contains
    only 'rec_' folders, and files of acceptable types

    Arguments:
    scrambling -- Boolean indicator as to whether trying to scramble (True) or
                  unscramble (False).

    Return:
    False if cwd is  invalid, else True.
    
    """
    fileTypes = ['py', 'jpg', 'exe', 'html', 'ico', 'png', 'ini', 'txt', 'nsh',
                 'dll', 'chm'] # Supported for scrambling.
    if not scrambling:
        fileTypes = ['py', 'db'] # Supported for unscrambling
    for path in os.listdir(os.getcwd()):
        if os.path.isfile(path) and not validExtension(path, fileTypes):
            print 'cwdIsValid:', path, '-> False'
            return False  # Invalid File
    print 'cwdIsValid:', path, '-> True'
    return True

def validExtension(p, types):
    """Indicates whether or not p is of any of the types.
    
    Arguments:
    p -- The pathname of the file to be evaluated
    types -- The file types ('.txt', '.zip', etc)
    
    Return:
    True if p is of one of the types, else False.
    
    """
    for type in types:
        if os.path.basename(p).endswith(type):
            return True
    return False


# ||-------------------------------------------------------------------------||
# ||-Scrambling--------------------------------------------------------------||
# ||-------------------------------------------------------------------------||

def scrDirName(d):
    """Returns the scrambled path of the given directory
    
    Arguments:
    d -- String of the directory to be scrambled
    
    Return:
    String of the scrambled directory
    
    """
    if os.path.basename(d).startswith('rec_'):
        return os.path.join(os.path.dirname(d), 'rec_' + 
                            sScramble(os.path.basename(d.lstrip('rec_'))))
    return os.path.join(os.path.dirname(d), sScramble(os.path.basename(d)))

def scrFileName(f):
    """Returns the scrambled path of the given file
    
    Arguments:
    d -- String of the file to be scrambled
    
    Return:
    String of the scrambled file
    
    """
    return os.path.join(os.path.dirname(f), sScramble(os.path.basename(f)))

def unscrDirName(d):
    """Returns the unscrambled path of the given directory
    
    Arguments:
    d -- String of the directory to be unscrambled
    
    Return:
    String of the unscrambled directory
    
    """
    if os.path.basename(d).startswith('rec_'):
        return os.path.join(os.path.dirname(d), 'rec_' + 
                            sUnscramble(os.path.basename(d.lstrip('rec_'))))
    return os.path.join(os.path.dirname(d), sUnscramble(os.path.basename(d)))

def unscrFileName(f):
    """Returns the unscrambled path of the given file
    
    Arguments:
    d -- String of the file to be unscrambled
    
    Return:
    String of the unscrambled file
    
    """
    return os.path.join(os.path.dirname(f), sUnscramble(os.path.basename(f)))

def sScramble(string):
    """Perform ASCII shift on a string.
    
    Arguments:
    string -- The string to be scrambled.
    
    Return:
    The scrambled string.
    
    """
    return ''.join(map(cScramble, string)) 

def cScramble(c):
    """Perform ASCII shift on a character.
    
    Arguments:
    c -- The character to be scrambled.
    
    Return:
    The scrambled character.
    
    """     
    specialChars = ['\\', '/', ':', '*', '?', '"', '<', '>', ]
    
    c = ' ' if c=='~' else chr(ord(c)+1)
    while(c in specialChars):
        c = chr(ord(c)+1)
    return c

def sUnscramble(string):
    """Perform reverse ASCII shift on a string.
    
    Arguments:
    string -- The string to be unscrambled.
    
    Return:
    The unscrambled string.
    
    """
    return ''.join(map(cUnscramble, string)) 

def cUnscramble(c):
    """Perform reverse ASCII shift on a character.
    
    Arguments:
    c -- The character to be unscrambled.
    
    Return:
    The unscrambled character.
    
    """     
    specialChars = ['\\', '/', ':', '*', '?', '"', '<', '>']
    
    c = '~' if c==' ' else chr(ord(c)-1)
    while(c in specialChars):
        c = chr(ord(c)-1)
    return c

if __name__ == '__main__':
    main()
