import plotly.figure_factory as ff

df = [dict(Task="UGC SP #1", Start='2022-01-25', Finish='2022-01-26', Resource='regular'),
      dict(Task="UGC SP #2", Start='2022-02-22', Finish='2022-02-23', Resource='regular'),
      dict(Task="UGC SP #3", Start='2022-03-29', Finish='2022-03-30', Resource='regular'),
      dict(Task="UGC SP #4", Start='2022-04-26', Finish='2022-04-27', Resource='regular'),
      dict(Task="Data collect for TRACDAT", Start='2022-03-01', Finish='2022-05-01', Resource='tasks'),

      dict(Task="Vote on PHYS pre-reqs", Start='2022-08-17', Finish='2022-08-24', Resource='tasks'),
      dict(Task="UGC FA #1", Start='2022-09-26', Finish='2022-09-27', Resource='regular'),
      dict(Task="UGC FA #2", Start='2022-10-31', Finish='2022-11-01', Resource='regular'),
      dict(Task="UGC FA #3", Start='2022-11-28', Finish='2022-11-29', Resource='regular'),
      dict(Task="UGC FA #4", Start='2022-12-12', Finish='2022-12-13', Resource='regular'),

      dict(Task="CUWiP", Start='2022-08-29', Finish='2022-10-10', Resource='awards'),
      dict(Task="WiP UNT Group Grant", Start='2022-10-08', Finish='2022-10-22', Resource='awards'),

      dict(Task="Ugrad Scholarship Noms.", Start='2023-01-25', Finish='2023-02-08', Resource='awards'),
      dict(Task="Honors Day Nominations", Start='2023-02-08', Finish='2023-02-22', Resource='awards')
     ]

colors = {'tasks': 'rgb(252,192,89)',
          'awards': 'rgb(232,72,127)',
          'regular': 'rgb(53,174,132)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)
fig.update_layout(xaxis = dict(showgrid=True, ticklabelmode="period", dtick='M1')  )
fig.update_layout(title="<b>UGC Gantt Chart 2022</b>", 
                font=dict(family="Arial",size=18),
                legend=dict(orientation="h")
                )

#fig.show()
fig.write_html('save.html')
