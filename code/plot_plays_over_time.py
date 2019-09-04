import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import pandas as pd

def team_run_percentage_by_conference(df,conference_divison):
    run_percentage = pd.pivot_table(df.replace('STL','LA').replace('SD','LAC').replace('JAC','JAX')[df[
        'posteam_conference_division'] == conference_divison] ,
                   values='effective_run',aggfunc=np.mean,index=['year'],columns=['posteam'])
    plt.figure(figsize=(20,5))
    for i in run_percentage.columns:
        sns.lineplot(x = run_percentage.reset_index()['year'], y = run_percentage.reset_index()[i])
    plt.title(f'{conference_divison} Run Percentages from {run_percentage.index.min()} to {run_percentage.index.max()}',fontsize=20)
    plt.ylabel('Run Percentage',fontsize=16)
    plt.xlabel('Year',fontsize=16)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    plt.legend(labels = run_percentage.columns)




def line_plot(df, play, title):

    tied_pass_tendencies = pd.DataFrame()
    tied_pass_tendencies[play] = df[df['posteam_status'] == 'Tied'].groupby(
        'minutes_elapsed')[play].mean()
    tied_pass_tendencies['status'] = 'Tied'

    winning_pass_tendencies = pd.DataFrame()
    winning_pass_tendencies[play] = df[df['posteam_status'] == 'Winning'].groupby(
        'minutes_elapsed')[play].mean()
    winning_pass_tendencies['status'] = 'Winning'

    losing_pass_tendencies = pd.DataFrame()
    losing_pass_tendencies[play] = df[df['posteam_status'] == 'Losing'].groupby(
        'minutes_elapsed')[play].mean()
    losing_pass_tendencies['status'] = 'Losing'

    pass_tendencies = pd.concat([tied_pass_tendencies,winning_pass_tendencies,losing_pass_tendencies])

    plt.figure(figsize=(15,5))
    sns.lineplot(y = pass_tendencies[play], x = pass_tendencies.index, hue = pass_tendencies['status'])
    plt.xlabel('Minutes Elapsed',fontsize=16)
    plt.ylabel(play,fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(fontsize=16)
    plt.title(title,fontsize=20);
    
    
    

def pie_chart_by_qtr(df):
    labels = ['Run', 'Pass']
    sizes1 = [df[df['qtr'] == 1]['effective_run'].value_counts(normalize=True)[0],
             df[df['qtr'] == 1]['effective_run'].value_counts(normalize=True)[1]]

    sizes2 = [df[df['qtr'] == 2]['effective_run'].value_counts(normalize=True)[0],
             df[df['qtr'] == 2]['effective_run'].value_counts(normalize=True)[1]]

    sizes3 = [df[df['qtr'] == 3]['effective_run'].value_counts(normalize=True)[0],
             df[df['qtr'] == 3]['effective_run'].value_counts(normalize=True)[1]]

    sizes4 = [df[df['qtr'] == 4]['effective_run'].value_counts(normalize=True)[0],
             df[df['qtr'] == 4]['effective_run'].value_counts(normalize=True)[1]]

    fig = plt.figure(figsize=(20,8))

    ax1 = fig.add_subplot(141)
    ax2 = fig.add_subplot(142)
    ax3 = fig.add_subplot(143)
    ax4 = fig.add_subplot(144)

    ax1.pie(sizes1, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                           'color':'white'})
    ax1.axis('equal')
    ax1.title.set_text('1st Qtr')
    ax1.title.set_size(28)

    ax2.pie(sizes2, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                            'color':'white'})
    ax2.axis('equal')
    ax2.title.set_text('2nd Qtr')
    ax2.title.set_size(28)

    ax3.pie(sizes3, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                            'color':'white'})
    ax3.axis('equal')
    ax3.title.set_text('3rd Qtr')
    ax3.title.set_size(28)

    ax4.pie(sizes4, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                           'color':'white'})
    ax4.axis('equal')
    ax4.title.set_text('4th Qtr')
    ax4.title.set_size(28)

    plt.legend(labels = ['Pass','Run'],fontsize=20)
    plt.show();

    
    
    
def pie_chart_by_down(df):

    labels = ['Run', 'Pass']
    sizes1 = [df[df['down'] == 1]['effective_run'].value_counts(normalize=True)[0],
             df[df['down'] == 1]['effective_run'].value_counts(normalize=True)[1]]

    sizes2 = [df[df['down'] == 2]['effective_run'].value_counts(normalize=True)[0],
             df[df['down'] == 2]['effective_run'].value_counts(normalize=True)[1]]

    sizes3 = [df[df['down'] == 3]['effective_run'].value_counts(normalize=True)[0],
             df[df['down'] == 3]['effective_run'].value_counts(normalize=True)[1]]

    sizes4 = [df[df['down'] == 4]['effective_run'].value_counts(normalize=True)[0],
             df[df['down'] == 4]['effective_run'].value_counts(normalize=True)[1]]

    fig = plt.figure(figsize=(20,8))

    ax1 = fig.add_subplot(141)
    ax2 = fig.add_subplot(142)
    ax3 = fig.add_subplot(143)
    ax4 = fig.add_subplot(144)

    ax1.pie(sizes1, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                           'color':'white'})
    ax1.axis('equal')
    ax1.title.set_text('1st Down')
    ax1.title.set_size(28)

    ax2.pie(sizes2, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                            'color':'white'})
    ax2.axis('equal')
    ax2.title.set_text('2nd Down')
    ax2.title.set_size(28)

    ax3.pie(sizes3, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                            'color':'white'})
    ax3.axis('equal')
    ax3.title.set_text('3rd Down')
    ax3.title.set_size(28)

    ax4.pie(sizes4, autopct='%1.1f%%', shadow=True, colors = ['navy','crimson'], textprops={'fontsize': 24,
                                                                                           'color':'white'})
    ax4.axis('equal')
    ax4.title.set_text('4th Down')
    ax4.title.set_size(28)

    plt.legend(labels = ['Pass','Run'],fontsize=20)
    plt.show();

    
    
    
def bar_chart_by_down(df):
    downs = df.groupby('down')[['effective_run']].sum()
    downs['effective_pass'] = df.groupby('down')[['effective_run']].count() - df.groupby('down')[['effective_run']].sum()

    fig = go.Figure(data=[
        go.Bar(name='Run', x=downs.index, y=downs['effective_run'],marker = {'color':'crimson'}),
        go.Bar(name='Pass', x=downs.index, y=downs['effective_pass'],marker = {'color':'navy'})
    ])
    # Change the bar mode
    fig.update_layout(barmode='group',xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Down")),
                     yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number of Plays")))
    fig.show()

    
    
    
def bar_chart_by_qtr(df):
    qtrs = df.groupby('qtr')[['effective_run']].sum()
    qtrs['effective_pass'] = df.groupby('qtr')[['effective_run']].count() - df.groupby('qtr')[['effective_run']].sum()

    fig = go.Figure(data=[
        go.Bar(name='Run', x=qtrs.index, y=qtrs['effective_run'],marker = {'color':'crimson'}),
        go.Bar(name='Pass', x=qtrs.index, y=qtrs['effective_pass'],marker = {'color':'navy'})
    ])
    # Change the bar mode
    fig.update_layout(barmode='group',xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Quarter")),
                     yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number of Plays")))
    fig.show()
    
    
    

if __name__ == '__main__':
    bar_chart_by_qtr(df)
    pie_chart_by_qtr(df)
    bar_chart_by_down(df)
    pie_chart_by_down(df)
