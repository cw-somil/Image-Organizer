# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:26:27 2020

@author: Somil
"""

import PIL 
import os
import shutil
import datetime



class ImageOrganizer:
    def __init__(self,dirname=''):
        self.images = os.listdir(dirname)
        self.dirname = dirname
        
    def preprocess_exif(self,data):
        data = data.strip()
        data = data.strip('\x00')
        
        return data

    def sort_by_device(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            manuf = self.preprocess_exif(exif[271])
            device = self.preprocess_exif(exif[272])
            merged = manuf + ' ' + device
            
            if not os.path.isdir(merged):
                os.mkdir(merged)
        
            shutil.move(os.path.join(self.dirname,fname),os.path.join(merged,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(merged,fname)))
            
            
    def sort_by_year(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
                     
            if not os.path.isdir(year):
                os.mkdir(year)
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(year,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(year,fname)))
            

    def sort_by_yr_month(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
            month = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%b')
                     
            if not os.path.isdir(year):
                os.mkdir(year)
            
            if not os.path.isdir(os.path.join(year,month)):
                os.mkdir(os.path.join(year,month))
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(year,month,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(year,month,fname)))
            
        
    def sort_by_device_yr_month(self):
        for fname in self.images:
            with PIL.Image.open(os.path.join(self.dirname,fname)) as img:
                exif = img._getexif() 
            
            ts = self.preprocess_exif(exif[306])
            date = ts.split(' ')[0]
            manuf = self.preprocess_exif(exif[271])
            device = self.preprocess_exif(exif[272])
            merged = manuf + ' ' + device
            year = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%Y')
            month = datetime.datetime.strptime(date, '%Y:%m:%d').strftime('%b')
            
            if not os.path.isdir(merged):
                os.mkdir(merged)
                
            if not os.path.isdir(os.path.join(merged,year)):
                os.mkdir(os.path.join(merged,year))
            
            if not os.path.isdir(os.path.join(merged,year,month)):
                os.mkdir(os.path.join(merged,year,month))
        
            shutil.copy(os.path.join(self.dirname,fname),os.path.join(merged,year,month,fname))
            print("Image {} moved from {} to {} successfully\n".format(fname,os.path.join(self.dirname,fname),os.path.join(merged,year,month,fname)))
        
