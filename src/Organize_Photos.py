"""
File -- Organize_Photos.py
Creator -- Dan Schlosser
Date -- 1/5/12
Description -- Copies all .jpg files to folders with 'YYYY-MM' labels.

"""

import pyexiv2
import os
import datetime

def main():
    """Copies all .jpg files to folders with 'YYYY-MM' labels.
    
    """
    fileTypes = ['.jpg', '.jpeg', '.gif', '.png', '.mp4', '.avi', 
                          '.ppm', '.mov', '.bmp', '.tiff']
    for fn in os.listdir(os.getcwd()): #filename
        if not os.path.isdir(fn) and fileTypeIsSupported(fn, fileTypes):
            try:
                timeStamp = getEXIF(fn, '')['Exif.Image.DateTime']
            except:
                timeStamp = datetime.datetime.fromtimestamp(os.path.getctime(fn))
                
            target_folder = dateToString(timeStamp)
            
            if not os.path.exists(target_folder): #Make target folder as needed 
                os.mkdir(target_folder) 
                
            target_dir = os.path.join(target_folder, os.path.basename(fn))
            os.rename(os.path.join(os.getcwd(),fn), target_dir) # move file
                
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
    
            
def dateToString(date):
    """Converts the given date to a string of form 'YYYY-MM'.
    
    Arguments:
    date -- Date to be converted to string
    
    Return:
    String representation of date of form 'YYYY-MM'.
    
    """
    return (date.strftime('%Y-%m'))
    
def getEXIF(fn, PHOTOS_DIR):
    """Returns the EXIF data dictionary for the photo of the given filename.
    
    Arguments:
    fn -- The filename of the photo.
    PHOTOS_DIR -- Directory where photos are stored.
        
    Return:
    ret -- A dictionary containing EXIF metadata.
    
    """
    dic = {}
    metadata = pyexiv2.ImageMetadata(PHOTOS_DIR + fn)
    metadata.read()
    for tag in metadata.exif_keys:
        dic[tag] = metadata[tag].value
    return dic
    
if __name__ == '__main__':
    main()

