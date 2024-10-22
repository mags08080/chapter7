# -*- coding: utf-8 -*-
"""matplotlib

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15LyTmvA4gk9DL2CT7yMZxyLYu7nZxosp
"""

# create a program to plot list data with the matplotlib package
import matplotlib.pyplot as plt

#create a main method
def main():
  #create a list with the heights of each bar
  heights = [100,200,300,400,500]

  #left edges
  left_edges = [0,10,20,30,40]

  #create a variable for bar width
  bar_width = 5

  #build bar chart with different colors
  plt.bar(left_edges, heights, bar_width, color=('r','g','b','w','k'))

  #add title
  plt.title('Sales by Year')

  #add labels to the axes
  plt.xlabel('Year')
  plt.ylabel('Sales')

  #call the xticks() function to display custom tick mark labels for years along x axis
  plt.xticks([0,10,20,30,40],['2016', '2017', '2018', '2019', '2020'])
  #call the yticks() to display sales
  plt.yticks([0,100,200,300,400,500],['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

  #show bar chart
  plt.show()

#call main mehtod
if __name__ == '__main__':
  main()