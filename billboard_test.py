import billboard
chart = billboard.ChartData('hot-100')

#Lists all charts which are avaibable:
#all_charts = billboard.charts()
#print(all_charts)


#print(chart[1])
#print(chart.entries)

#while chart.previousDate:
#    doSomething(chart)
#    chart = billboard.ChartData('hot-100', chart.previousDate)

greatest_100_singles = billboard.ChartData('greatest-hot-100-singles')
#greatest_100_artists = billboard.ChartData(''greatest-hot-100-artists')
print(f'{greatest_100_singles}')
while greatest_100_singles.previousDate:
    #greatest_100_singles(range(1, 10))
    greatest_100_singles_full = billboard.ChartData('Greatest_100_singles', chart.previousDate)

greatest_100_singles_full[]


#blues_albums = billboard.ChartData('blues-albums')
#top_10 = range(0, 10)
#for number in top_10:
#    print(f'{blues_albums[number]}')