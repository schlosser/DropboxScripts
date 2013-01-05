"""
File -- Flatten_Photo_Folders.py
Creator -- Dan Schlosser
Date -- 1/5/13
Description -- Empties all folders of format 'YYYY-MM' of support image/movie 
               files anddeletes the folders if empty.

"""

import os

def main():
    """Empties all folders of format 'YYYY-MM' of support image/movie files and
    deletes the folders if empty.
    
    """
    fileTypes = ['.jpg', '.jpeg', '.gif', '.png', '.mp4', '.avi', 
                          '.ppm', '.mov', '.bmp', '.tiff']
    home = os.getcwd()
    
    for dir in os.listdir(home):
        print dir
        if isPhotoFolder(dir):
            os.chdir(os.path.join(home, dir))
            for fn in os.listdir(os.getcwd()):
                if fileTypeIsSupported(fn, fileTypes):
                    print fn
                    target_path = os.path.join(home, os.path.basename(fn))
                    current_path = os.path.join(os.getcwd(), os.path.basename(fn))
                    print target_path
                    os.rename(current_path, target_path) # Move file.
            os.chdir(home)        
            if not os.listdir(os.path.join(home, dir)):
                os.rmdir(dir)  # Delete folder if empty.
                
def isPhotoFolder(dir):
    """Returns whether or not the dir of the format 'YYYY-MM'.
    
    Arguments:
    dir -- the directoy to be checked.
    
    Return:
    True if it is of the correct format, else False.
    
    """
    print "isPhotoFolder: ", dir
    if (os.path.isdir(dir) and len(dir)==7  and 
            int(dir[0:4])<=9999 and dir[4]=='-' and int(dir[5:7])<=12):
        return True
    return False

def fileTypeIsSupported(fn, fileTypes):
    """Returns whether or not the filename is of any of the file types in 
    fileTypes.
    
    Arguments: 
    fn -- File name to check against types
    fileTypes -- A list of fileTypes to check against fn
    
    Return:
    True if a match, else False
    
    """
    for fileType in fileTypes:
        if fn.endswith(fileType):
            return True
    return False
    
if __name__ == '__main__':
    main()

