import beautifulplots as bp
import pandas as pd


def test_plot_defaults():
    """Test plot defaults."""

    
    plot_defaults_expected={'pltstyle': 'seaborn','figsize': None,'legend_loc': 'best',
    'legend_loc2': 'best','wspace': 0.2,'hspace': 0.2,'sharex': False,'title': None,
    'ylims': None, 'xlims': None, 'ylims2': None,
    'xlabelfontsize': 16,   'xticklabelsize': 16, 'xtickfontsize': 16,
    'xtickrotation': 0, 'ylabelfontsize': 16, 'ytickfontsize': 16, 'ytickrotation': 0,
    'titlefontsize': 18, 'legendsize': 16, 'legend': False, 'xlabel': '', 'ylabel': '',
    'color': None, 'color2': None, 'palette': None, 'palette2': None, 'hue': None,
    'ci': None, 'ci2': None, 'marker': None, 'marker2': None, 'yaxis_currency': False,
    'ytick_format': None, 'legend_labels': None, 'alpha': None, 'alpha2': 0.5, 
    'estimator': sum, 'estimator2': sum}
    
    plot_defaults_actual = bp.plot_defaults()
    assert plot_defaults_actual == plot_defaults_expected, "plot_defaults incorrect"
    
    
def test_barplot():
    
    # data 
    print('Data:Product Category Sales by Store')
    barplot_data = { 'category':['groceries','groceries','groceries', 'hardware','hardware','hardware','hobbies','hobbies','hobbies'] ,
                'sales':[ 90, 60,50, 50,30,20,40,40,20], 'store':['A','B','C','A','B','C','A','B','C'] }

    df = pd.DataFrame(barplot_data)
    # create unit sales by category ... assume some average sale price per category
    def unit_sales(row):
        units = 0
        if row['category'] == 'groceries': units = row['sales']/5
        elif row['category'] == 'hardware': units = row['sales']/10
        elif row['category'] == 'hobbies': units = row['sales']/20
        return units
    df['units']= df.apply(lambda row: unit_sales(row),axis=1)
    
    
    # test that barplot completes normally and returns None
    plot_return = bp.barplot(df,'category','sales',hue='store', palette='tab20', 
                   title='1e. easy barplot, Product Category Sales by Store, horizontal bars', figsize=(12,8), 
                   bardatalabels=True, bardataformat=".2f", barcurrency=True, bar_orientation='h',
                   xlims = (0.1,100), legend=True, legendloc="lower right", test_mode=True)
    assert plot_return == None, "barplot error: did not complete normally"
    
    # do not set bardataformat ... ensure it has useful default
    plot_return = bp.barplot(df,'category','sales',hue='store', palette='tab20', 
                   title='1e. easy barplot, Product Category Sales by Store, horizontal bars', figsize=(12,8), 
                   bardatalabels=True, barcurrency=True, bar_orientation='h',
                   xlims = (0.1,100), legend=True, legendloc="lower right", test_mode=True)
    
    assert plot_return == None, "barplot error: did not complete normally"
    
    # do not set bardataformat ... use color
    plot_return = bp.barplot(df,'category','sales',hue='store', color='blue', 
                   title='1e. easy barplot, Product Category Sales by Store, horizontal bars', figsize=(12,8), 
                   bardatalabels=True, barcurrency=True, bar_orientation='h',
                   xlims = (0.1,100), legend=True, legendloc="lower right", test_mode=True)
    assert plot_return == None, "barplot error: did not complete normally"
    
    # no color or palette, vertical bars
    # do not set bardataformat ... no color or palette
    plot_return = bp.barplot(df,'category','sales',hue='store', 
                   title='1e. easy barplot, Product Category Sales by Store, horizontal bars', figsize=(12,8), 
                   bardatalabels=True, bar_orientation='v',
                   xlims = (0.1,100), legend=True, legendloc="lower right", test_mode=True)
    assert plot_return == None, "barplot error: did not complete normally"
    
    
    bp.barplot(df,'category','sales', palette='tab20', 
                   title='1a. Beautifulplots barplot, Sales All Stores by Product Category, secondary y-axis', figsize=(12,4),
                   bardatalabels=True, bardataformat=".2f", barcurrency=True, ylims = (0.1,220), 
                   y2='units',ylims2=(0,45), color2='black',marker2="o", test_mode=True)
    assert plot_return == None, "barplot error: did not complete normally"
    
def test_lineplot():
    
    # data
    sp500_file =  './data/GSPC_1950-1-3_to_2022-6-8.csv'
    df_sp500 = pd.read_csv(sp500_file,index_col=0,parse_dates=True)
    # reset index ...  Seaborn requires x-axis to be a column 
    df = df_sp500.reset_index() 

    
    plot_return=bp.lineplot(df,x='Date' , y=['Close','Open'], y2='Volume', 
             ylims=(0,4000), ylims2=(0,10*1e9), legend_loc2 = "lower left", color2='red', alpha2=0.5,
             figsize=[12,4],yaxis_currency=True, legend=True,
             ytick_format=".0f", title="S&P 500, easy lineplot", test_mode=True)
    
    assert plot_return == None, "lineplot error: did not complete normally"
    
    # palette 
    plot_return=bp.lineplot(df,x='Date' , y=['Close','Open'], y2='Volume', palette='tab20',
             ylims=(0,4000), ylims2=(0,10*1e9), legend_loc2 = "lower left", color2='red', alpha2=0.5,
             figsize=[12,4],yaxis_currency=True, legend=True,
             ytick_format=".0f", title="S&P 500, easy lineplot", test_mode=True)
    
    assert plot_return == None, "lineplot error: did not complete normally"
    
    
    plot_return=bp.lineplot(df,x='Date' , y=['Close','Open'], y2='Volume', color='red',
             ylims=(0,4000), ylims2=(0,10*1e9), legend_loc2 = "lower left", color2='red', alpha2=0.5,
             figsize=[12,4],yaxis_currency=True, legend=True,
             ytick_format=".0f", title="S&P 500, easy lineplot", test_mode=True)
    
    assert plot_return == None, "lineplot error: did not complete normally"