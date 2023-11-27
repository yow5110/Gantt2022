import plotly.figure_factory as ff
import pandas as pd

def csv2dict(inp):
    return dict(Task=inp['name'], Start=inp['startdate'].strip(), Finish=inp['enddate'].strip(), Resource=inp['type'].strip(), Comments=inp['comments'] )

df = pd.read_csv ('data.csv', names=['name','startdate','enddate','type','comments'], comment='#')
df = [ csv2dict(df.loc[i]) for i in range(len(df))    ]



colors = {'tasks': 'rgb(252,192,89)',
          'awards': 'rgb(232,72,127)',
          'regular': 'rgb(53,174,132)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)

#for i in range(len(fig['data'])):
#    fig['data'][i].update( hoverinfo='name')

fig.update_layout(
    xaxis = dict(showgrid=True, ticklabelmode="period", dtick='M1', tickformat="%b\n%Y",
                rangeselector=dict(x=.1,y=1.01)
                 ),
    yaxis = dict(showgrid=True, automargin=True, ticklen=10))
# more tick control see https://stackoverflow.com/questions/68475195/dticks-and-plotly-how-to-control-what-is-shown-on-x-axes

fig.update_layout(
    title="<b>UGC Gantt Chart </b>", 
    title_xanchor='center', title_x=0.5,
    font=dict(family="Arial",size=20),
    legend=dict(orientation="h"        ,yanchor="bottom"        ,xanchor="right"        ,y=1.0        ,x=1)
    )

#add vline for today's date
from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')
fig.add_vline(today)

#fig.show()
fig.write_html('save.html')
