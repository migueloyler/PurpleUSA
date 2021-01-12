""" Miguel Oyler-Castrillo
CS1103 Project 4: Purple America
Main function
"""

import sys
import csv
import math
import glob
from region import Region
from plot import Plot



def mercator(lat):
    """project latitude 'lat' according to Mercator"""
    lat_rad = (lat * math.pi) / 180
    projection = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
    return (180 * projection) / math.pi


def main(results, boundaries, output, width, style):
    """
    Draws an image.
    This function creates an image object, constructs Region objects by reading
    in data from csv files, and draws polygons on the image based on those Regions

    Args:
        results (str): name of a csv file of election results
        boundaries (str): name of a csv file of geographic information
        output (str): name of a file to save the image
        width (int): width of the image
        style (str): either 'GRAD' or 'SOLID'
    """
    region_instance_list = []
    
    def get_coord_pairs(longitude_list, raw_latitude_list):
    
    
        def true_lat(raw_latitude_list):
            """converts list of lats into they're mercator value"""
            true_lat_list = []
            for i in raw_latitude_list:
                true_lat_list.append(mercator(i))
            return true_lat_list
  
    
        coord_pairs = []
        
        
        for long, lat in zip(longitude_list, true_lat(raw_latitude_list)):
            
            coord_pairs.append((long, lat))
            
        return coord_pairs    
    
    
    with open(results, 'r') as elc, open(boundaries, 'r') as bnd:
              
                    
        for (co,st,r,d,o), boundary in zip(csv.reader(elc),csv.reader(bnd)):
            
            long_list = []
            lat_list = []
             
            county,state, *coords = boundary
            
            for num, info in enumerate(coords):
                if num  % 2 == 0:
                    long_list.append(float(info))
                else:
                    lat_list.append(float(info))
                        
            
            region_instance = Region(get_coord_pairs(long_list, lat_list),r,d,o)
            region_instance_list.append(region_instance)
                
            
                                
    max_long_list = [region.max_long() for region in region_instance_list]
    min_long_list = [region.min_long() for region in region_instance_list]
    max_lat_list = [region.max_lat() for region in region_instance_list]
    min_lat_list = [region.min_lat() for region in region_instance_list]
    
    bounding_box = Plot(width, min(min_long_list),
                        min(min_lat_list), max(max_long_list),
                        max(max_lat_list))
    
    for region in region_instance_list:
        
    
        
        bounding_box.draw(region, style)
        
        
    bounding_box.save(output)



if __name__ == '__main__':
    results = sys.argv[1]
    boundaries = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    style = sys.argv[5]
    main(results, boundaries, output, width, style)
