"""
Miguel Oyler-Castrillo
CS1103 Project 4: Purple America
Plot Class
"""
from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb

class Plot:

    """
    Provides the ability to map, draw and color regions in a long/lat
    bounding box onto a proportionally scaled image.
    """
    @staticmethod
    def interpolate(x_1, x_2, x_3, newlength):
        """
        linearly interpolates x_2 <= x_1 <= x_3 into newlength
        x_2 and x_3 define a line segment, and x1 falls somewhere between them
        scale the width of the line segment to newlength, and return where
        x_1 falls on the scaled line.
        """
        line_segment = x_3 - x_2
        scale_value = newlength / line_segment
        return (x_1 - x_2) * scale_value
        
    @staticmethod
    def proportional_height(new_width, width, height):
        """
        return a height for new_width that is
        proportional to height with respect to width
        Yields:
            int: a new height
        """
        new_height = (new_width * height) / width
        return ((new_width * height) / width)

    @staticmethod
    def fill(region, style):
        """return the fill color for region according to the given 'style'"""
        if style == "GRAD":
            return Plot.gradient(region)
        else:
            return Plot.solid(region)

    @staticmethod
    def solid(region):
        """
        a solid color based on a region's plurality of votes
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        if region.plurality() == 'REPUBLICAN':
            return getrgb("RED")
        elif region.plurality() == 'DEMOCRAT':
            return getrgb("BLUE")
        else:
            return getrb('GREEN')
        


    @staticmethod
    def gradient(region):
        """
        a gradient color based on percentages of votes in a region
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        return (int(255 * region.republican_percentage()),
                int(255 * region.other_percentage()),
                int(255 * region.democrat_percentage()))
    #255 is for the color, didn't really seem logical to make a constant for the
    #highest RGB value
    

    def __init__(self, width, min_long, min_lat, max_long, max_lat):
        """
        Create a width x height image where height is proportional to width
        with respect to the long/lat coordinates.
        """
        self.width = width
        self.min_long = min_long
        self.min_lat = min_lat
        self.max_long = max_long
        self.max_lat = max_lat
        im_height = Plot.proportional_height(self.width,
                                        (self.max_long - self.min_long),
                                       (self.max_lat - self.min_lat))
        self.im_height = im_height
        
        im = Image.new("RGB", (int(self.width), int(im_height)), (255,255,255)) 
        self.im = im


    def save(self, filename):
        """save the current image to 'filename'"""
        self.im.save(filename, "PNG")

    def draw(self, region, style):
        """
        Draws 'region' in the given 'style' at the correct position on the
        current image
        Args:
            region (Region): a Region object with a set of coordinates
            style (str): 'GRAD' or 'SOLID' to determine the polygon's fill
        """
        
        
        def trans_long(region):
            """takes a region object and interpolates all longitudinal coords
            with respect the to image's width"""
            interpolated_longs = []
            for i in region.longs():
                interpolated_longs.append(Plot.interpolate(i, self.min_long,
                                                           self.max_long,
                                                           self.width))
            return interpolated_longs
        
        def trans_lat(region):
            """takes a region object and interpolates all latitudinal coords
            with respect to the images height, uses proportional_height to find
            image's height with respect to its width.
            substracts latitudinal coords from im_height in order to properly
            place points in the image"""
            interpolated_lats = []
            for i in region.lats():
                interpolated_lats.append(Plot.interpolate(i, self.min_lat, 
                                                          self.max_lat, 
                                                          self.im_height))
                
            return [self.im_height - k for k in interpolated_lats]        
        
        interpolated_coords = []
        
        for long, lat in zip(trans_long(region), trans_lat(region)):
            interpolated_coords.append((float(long), float(lat)))
        
        print(interpolated_coords)
            
        ImageDraw.Draw(self.im).polygon(interpolated_coords, Plot.fill(region,
                                                                       style))

