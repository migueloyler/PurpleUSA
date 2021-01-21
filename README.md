# PurpleUSA

This project explores visualizing election data by county and by state through the use of color and gradient. The data is logically split by election results and by county and state regions. A primary goal of this lab is to naturally organize the data uses classes and clear, well defined programming interfaces.


A modern, popular visualization technique for geographic difference is to color counties in the United States according to some statistic. You see it everywhere.
In recent presidential elections we have heard a lot about “red” states and “blue” states. But a more nuanced view, espoused by Robert Verderbei, shows that the USA is actually filled with purple states (though a few like Utah and Vermont truly are more one color than the other).


To run your code from the command line use (assuming the data is in a folder called “election- data” in the same directory your code is in):
$ python election.py election-data/results/US2016.csv election-data/boundaries/US.csv output.png 1024 GRAD
