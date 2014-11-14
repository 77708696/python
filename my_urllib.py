import urllib.request

url = 'http://www.w3cschool.cc/python/python-functions.html'
values = {'obs_year':'2011','obs_month':'March',
                             'obs_day':'8','start_year':'2011'
                             ,'start_month':'March','start_day':'8'
                             ,'start_hour':'All Hours','stop_year':'2011'
                             ,'stop_month':'March','stop_day':'8'
                             ,'stop_hour':'All Hours','xsize':'All'
                             ,'ysize':'All','wave':'all'
                             ,'filter':'all','object':'all'
                             ,'xbin':'all','ybin':'all'
                             ,'highc':'all'}

req = urllib.request.urlopen(url)

the_page = req.read()
print(the_page)