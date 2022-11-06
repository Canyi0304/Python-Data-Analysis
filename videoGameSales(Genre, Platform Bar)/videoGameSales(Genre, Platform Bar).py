from pyecharts import options as opts
import pandas as pd
from pyecharts.charts import Bar
import csv

#f = open('./vgsales.csv')
#data = csv.reader(f)

# for row in data:
#     print(row)

data  = pd.read_csv('vgsales.csv')
#print(data.head())
#print(data)

# data.info()

#데이터가 많아서 10줄만 먼저 확인
data.dropna(inplace= True)
data.reset_index (drop=True, inplace=True)
print(data.head(10))

# print(data.describe(include='object').T)


data['Year'] = data['Year'].astype(str)

x_first_5 = data[((data['Year'] == '2020.0')|(data['Year'] == '2019.0')|
            (data['Year']=='2018.0')|(data['Year']=='2017.0')|(data['Year']=='2016.0'))]
x_next_5 = data[((data['Year'] == '2015.0')|(data['Year'] == '2014.0')|
            (data['Year']=='2013.0')|(data['Year']=='2012.0')|(data['Year']=='2011.0'))]

bar1 = Bar(init_opts=opts.InitOpts(width='1450px', height='350px'))
bar1.add_xaxis(x_next_5['Genre'].value_counts().index.tolist())
bar1.add_yaxis("",x_next_5['Genre'].value_counts().tolist())
bar1.set_global_opts(title_opts=opts.TitleOpts(title="2011-2015년 사용자가 좋아하는 게임장르"),
                     visualmap_opts=opts.VisualMapOpts(max_=1500),
                    ) 

#bar1.render_notebook() 이방법은 Jupyter에서만 가능
bar1.render("2011-2015년 사용자가 좋아하는 게임장르.html")
# bar1.render_embed("2011-2015년 사용자가 좋아하는 게임장르.html")


bar2 = Bar(init_opts=opts.InitOpts(width='1450px', height='350px'))
bar2.add_xaxis(x_first_5['Genre'].value_counts().index.tolist())
bar2.add_yaxis("",x_first_5['Genre'].value_counts().tolist())
bar2.set_global_opts(title_opts=opts.TitleOpts(title="2016-2020년 사용자가 좋아하는 게임장르"),
                     visualmap_opts=opts.VisualMapOpts(max_=150,pos_left= "90%")
                    ) 
bar2.render("2016-2020년 사용자가 좋아하는 게임장르.html")

#최근 10년의 비디오 게임시장은 변화가 크지만 액션 장르는 역시 1위를 차지했고
#스포츠와 슈팅게임의 순위가 많이 올랐다.


bar3 = Bar(init_opts=opts.InitOpts(width='1450px', height='750px'))
bar3.add_xaxis(x_next_5['Platform'].value_counts().index.tolist())
bar3.add_yaxis("",x_next_5['Platform'].value_counts().tolist())
bar3.set_global_opts(title_opts=opts.TitleOpts(title="2011-2015년 인기많은 플랫폼 비교"),
                     visualmap_opts=opts.VisualMapOpts(max_=1000),
                    ) 
bar3.render("2011-2015년 인기많은 플랫폼 비교.html")


bar4 = Bar(init_opts=opts.InitOpts(width='1450px', height='750px'))
bar4.add_xaxis(x_first_5['Platform'].value_counts().index.tolist())
bar4.add_yaxis("",x_first_5['Platform'].value_counts().tolist())
bar4.set_global_opts(title_opts=opts.TitleOpts(title="2016-2020년 인기많은 플랫폼 비교") ,
                     visualmap_opts=opts.VisualMapOpts(max_=110),
                    ) 
bar4.render("2016-2020년 인기많은 플랫폼 비교.html")



