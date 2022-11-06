from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd

data  = pd.read_csv('vgsales.csv')
data['Year'] = data['Year'].astype(str)

x_first_5 = data[((data['Year'] == '2020.0')|(data['Year'] == '2019.0')
                |(data['Year']=='2018.0')|(data['Year']=='2017.0')|(data['Year']=='2016.0'))]
x_next_5 = data[((data['Year'] == '2015.0')|(data['Year'] == '2014.0')
                |(data['Year']=='2013.0')|(data['Year']=='2012.0')|(data['Year']=='2011.0'))]

pie1 = Pie(init_opts=opts.InitOpts(width='1250px', height='600px',))
pie1.add('', [list(z) for z in zip(x_next_5['Publisher'].value_counts().head(10).index.tolist(), 
            x_next_5['Publisher'].value_counts().head(10).tolist())], radius=['30%', '70%'])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='2011 - 2015 비디오게임 제작사 Top10'),
                     legend_opts=opts.LegendOpts(orient='vertical',pos_top='15%',pos_left='90%'))
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
pie1.render(path="2011-2015년 비디오게임 제작사 Top10 .html")

pie2 = Pie(init_opts=opts.InitOpts(width='1250px', height='600px',))
pie2.add('', [list(z) for z in zip(x_first_5['Publisher'].value_counts().head(10).index.tolist(), 
            x_first_5['Publisher'].value_counts().head(10).tolist())], radius=['30%', '70%'])
pie2.set_global_opts(title_opts=opts.TitleOpts(title='2016 - 2020 비디오게임 제작사 Top10'),
                     legend_opts=opts.LegendOpts(orient='vertical',pos_top='15%',pos_left='90%'))
pie2.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
pie2.render("2016-2020년 비디오게임 제작사 Top10 .html")

