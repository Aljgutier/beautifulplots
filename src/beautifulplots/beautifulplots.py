import gc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from matplotlib.colors import Normalize
import logging
from matplotlib.cbook import boxplot_stats
import matplotlib as mpl



def plot_defaults():
    """Dictionary of plot parameters. Each parameter coresponds and corresponding value. 
    See also get_plot_options for extracting plot options from **kwargs. 

    **Axis - x, y, and plot area parameters**
    
    Args:
        df (DataFrame): The input DataFrame containing colums corresponding to bar values and columns.
 
        title (String): corresponds to the axis title. default = ''
            
        titlefontsize: font size of the axis title, default = 18
            
        legend_loc(String): Matplotlib legend location, for example, upper right , default = "best".
        
        legend_loc2 (String): Secondary axis legend location, for example, upper right , default = best.
         
        xlims: (xmin, xmax), minimum and maximum x-values of the axis. default = None, in which case the min and max are set automatically by matplotlib.
        
        ylims: (ymin,ymax), minimum and maximum y-values of the axis. default = None, in which case the min and max are set automatically by matplotlib.
        
        ylims2: (ymin,ymax), minimum and maximum y-values of the secondary axis. default = None, in which case the min and max are set automatically by matplotlib.
        
        xlabelfontsize: default = 16
        
        xticklabelsize: default = 16
        
        xtickfontsize: default = 16
        
        xtickrotation: default = 0
        
        ylabelfontsize: ylabel font size, default = 16
            
        ytickfontsize: xtick label font size, default = 16
        
        ytickrotation:  Rotation of the xtick label, default = 0
        
        legendsize: legend font size, default = 16
        
        legend (Boolean):  Place a legend on the axis, default = False
            
        xlabel (String): xlabel title, default = ''
            
        ylabel (String):  ylable title, default = ''
        
    **Bar, Line, Scatter Plots**
    
    Args:
        
        marker: Matplotlib line markers. default = None (Matplotlib default).
            
        marker2: Secondary axis, Matplotlib line marker. default = None (Matplotlib default).
            
        yaxis_currency (Boolean): Boolean default = False.
            
        ytick_format (String): String default = None (Matplotlib default).
            
        alpha (fraction): Trasnparancy (opacity), default = None (not transparent)
            
        alpha2 (fraction): Secondary axis, default = 0.5, 50% opacity
        
        bar_orientation: "v" (vertical) or "h" (horizontal), default = "v" 
        
        bardatalabels (Boolean): Add data labels to bargraph, default = False
            
        bardataformat(String): Bardata format number format, default = ":.2f"
            
        bardatafontsize: default = 14 
            
        barcurrency (Boolean): Bar data labels represent currency (dollar), defuault = False
            
        legend_labels (list): Overide default legend labels. default = None (do not override)
        
        estimator: seaborn barplot summary estimator, default = sum
            
        estimator2: secondary axis, seaborn barplot summary estimator, default = sum
            
        color: default = None, indicateing Matplolib default (Matplotlib default)
            
        color2: secondary axis line, bar or color. defualt = None (Matplotlib default)
            
        palette: colormap, default = None
            
        palette2: colormap, default = None, secondary y axis.
            
        hue: dimension value for corresponding Seaborn graphs, default = None.
        
        ci: Seaborn confidence interval parameter: float, sd, or None
            
        ci2: Seaborn confidence interval parameter second y axis: float, sd, or None
     
    **Plots and subplots**
    
    Parameters corresponding to the plot or subplot characteristics. They are used when matplot_helpers
    functions create the plot figure and axis, otherewise, these parameters do not affect the plot.
    
    Args:
    
        plotstyle (String): matplotlib plotstyle
            
        figsize: total size (height, width) in inches of the figure, including total plotting area of all subplots and spacing
        
        wspace: width space (horizontal) between subplots, default wspace = 0.2
        
        hspace: height space (vertical) between subplots, default hspace = 0.2
            
        legendloc: default=best
   
    **Returns**
    
        Dictionary: {parameter1:value1, parameter2:value2, ... }. 
        Pairs of plat parameters and corresponding values.
    """    

    plot_defaults = {
    # plot and subplot
    'pltstyle': 'seaborn',
    'figsize' :  None,
    'legend_loc':'best',
    'legend_loc2':'best',
    'wspace': 0.2,
    'hspace': 0.2,
    'sharex':False,
    
    # Axis ( corx and y plot)
    'title' :None,               #  list ot titles, 1 per axis  #  list of x,y tuples
    'ylims' :None,               # list of two-tuples ylims (lower, upper)
    'xlims' :None,
    'ylims2':None,
    'xlabelfontsize':16,
    'xticklabelsize':16,
    'xtickfontsize': 16,
    'xtickrotation':0,
    'ylabelfontsize':16,
    'ytickfontsize':16,
    'ytickrotation':0,
    'titlefontsize':18,
    'legendsize':16,
    'legend':False,
    'xlabel': '',
    'ylabel': '',
    'color':None,   # color designation for the corresponding graph
    'color2':None,   # color secondary y axis
    'palette':None,  
    'palette2':None,  # palette secondary y axis
    'hue':None,   # dimensional value for corresponding Seaborn graphs
    'ci':None, # confidence parameter for pimary axis
    'ci2': None, # confidence parameter for secondary axis


    # Bars, Lines and Scatter
    'marker':None,  # Boolean, list, dictionary
    'marker2':None,  # Boolean, list, or dictionary
    'yaxis_currency':False,
    'ytick_format': None,
    'legend_labels':None,
    'alpha': None,
    'alpha2': 0.5,
    'bar_orientation':'v',
    'bardatalabels':False,
    'bardataformat':".2f",
    'bardatafontsize':14,
    'estimator':sum,
    'estimator2':sum,
    'barcurrency':False #dollar, comma, default (None)

    }

    return plot_defaults

def set_axisparams(options_dict,ax,g):
    """Receives as input a dictionary of plot options and applies the options to the maxtplotlib axis and graph.

    Args:
        options_dict (dictionary): Dictionary where each key, value pair corresponds to plot parameter
        ax (axis): matplotlib axis to apply the plot options
        g (graph): matplotlib graph to apply the plot options

    Returns:
        None: returns None if the function completes without errors.
    """ 

    title=options_dict['title']
    titlefontsize=options_dict['titlefontsize']
    legendloc=options_dict['legend_loc']
    legendsize=options_dict['legendsize']
    xlabel=options_dict['xlabel']
    xlabelfontsize=options_dict['xlabelfontsize']
    xlims=options_dict['xlims']
    xtickfontsize=options_dict['xtickfontsize']
    xtickrotation=options_dict['xtickrotation']
    ylabel=options_dict['ylabel']
    ylabelfontsize=options_dict['ylabelfontsize']
    ytickfontsize=options_dict['ytickfontsize']
    ytickrotation=options_dict['ytickrotation']
    ylims=options_dict['ylims']
    
    
    bardatalabels=options_dict['bardatalabels']
    bardataformat=options_dict['bardataformat']

    ax.set_xlabel(xlabel,fontsize=xlabelfontsize)
    ax.set_ylabel(ylabel,fontsize=ylabelfontsize)

    for x_tick in ax.get_xticklabels():
        x_tick.set_fontsize(xtickfontsize)
        x_tick.set_rotation(xtickrotation)

    for y_tick in ax.get_yticklabels():
        y_tick.set_fontsize(ytickfontsize)
        y_tick.set_rotation(ytickrotation)


    ax.set_title(title, fontsize=titlefontsize)

    if ylims != None:
        ax.set_ylim(ylims[0],ylims[1])

    if xlims != None:
        ax.set_xlim(xlims[0],xlims[1])

    if options_dict['legend'] == True:
        ax.legend( loc=legendloc, prop={'size': legendsize})     
        

    return True

def get_kwargs(**kwargs):   
    """process **kwargs options corresponding to the plot_defaults dictionary (see above)
    If a beautifulplots plot_option dictionary key is 
    contained in the **kwargs then the plot_defautls[key] value is replaced 
    with that found in **kwargs. 

    Returns:
        Dictionary: {parameter1:value1, parameter2:value2, ...} dictionary corresponding to plot options 
    """   
       
    plot_options = plot_defaults() # returns a dictionary of defaut matplotlib parameters

    # interate through the parameters in the plot_options dictionary
    # find the key in the kwargs, otherwise the paremeer = default
    # if the kwargs parameter != default then update plot_options
    for key in plot_options:
        default = plot_options[key]
        kwarg_value = kwargs.get(key, default) # parameter = kwarg  or default
        if kwarg_value != default: plot_options[key] = kwarg_value # update plot_option 
        
    return plot_options

 
def barplot(df, bar_columns, bar_values, y2=None, ax=None, test_mode=False, **kwargs):
    """Bar plot function designed for ease of use and aesthetics. 
    The underlying barplot is ased on the Seaborn with additions, such as secondary axis, data labels,
    and improved default parameters. Refer to beautifulplots plot_defaults for a complete list of options.
    
    Args:
        df (DataFrame): The input DataFrame containing colums corresponding to bar_plot values ("bar_values") and column names (see examples in documentation)
            
        bar_columns: Datafrae columns corresponding to bar column names
            
        bar_values: Dataframe column corresponding to bar column values
            
        ax (axis): matplotlib axis (optional), default = None. If axis is None, then create a matplolib figure, axis to host the barplot
            
        color: Matplotlib compatabile color name as text or RGB values, for example,  color = [51/235,125/235,183/235].
            
        palette: Matplotlib compatible color palette name, for example, "tab20"
            
        hue: Name of hue dimension variable (i.e., DataFrame column name)
            
        ci: Seaborn confidence interval parameter: float, sd, or None, default = None
            
        bar_orientation: default = v (vertical), or h (horizontal)
            
        bar_currency: default = False (bar values do not represent currency). True (bar values represent currency, append $ to the value)
            
        bar_datalabels (Boolean): default = False (data labels not included)
        
        additional options:  see kale.plot_defaults for additional input variables.
            

    Returns:
        returns True if processing completes succesfully (without errors).
    """
        
    plot_options = get_kwargs(**kwargs)
    
    estimator = plot_options['estimator'] 
    estimator2 = plot_options['estimator'] 
    ci = plot_options['ci']
    ci2 = plot_options['ci2']
    alpha = plot_options['alpha']
    alpha2 = plot_options['alpha2']
    hue = plot_options['hue']
    bar_orientation= plot_options['bar_orientation']
    palette = plot_options['palette']
    palette2 = plot_options['palette2']
    marker2 = plot_options['marker2']
    color = plot_options['color']
    color2 = plot_options['color2']
    bardataformat =plot_options['bardataformat']

    # if no hue then only one color
    # if hue == None and color==None : color = [51/235,125/235,183/235] if plot_options['color'] == None else plot_options['color']

    if bar_orientation == 'v': x,y = bar_columns, bar_values
    else: x,y = bar_values, bar_columns
    

    if ax == None: 
        mpl.rcParams.update(mpl.rcParamsDefault) # reset plot/figure parameters
        plt.style.use(plot_options['pltstyle'])
        fig,_ax = plt.subplots(nrows=1, ncols=1, figsize=plot_options['figsize']) 
    else: _ax = ax
        
    g=sns.barplot(x=x, y=y, hue=hue, color = color, palette=palette, data=df, ax = _ax,
                  orient=bar_orientation, ci=ci, estimator=estimator, alpha=alpha)
    
    # Bar labels ... iterate with hue
    # Matplotlib
      # https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py
    # Geeks for Geeks
      # https://www.geeksforgeeks.org/how-to-show-values-on-seaborn-barplot/
    if plot_options['bardatalabels']== True and hue == None:
        f = "%"+bardataformat+""
        if plot_options["barcurrency"] == True: f = "$"+f # dollar
        g.bar_label(g.containers[0],  fontsize=plot_options['bardatafontsize'], fmt=f)

    # Geeks for Geeks
      # https://www.geeksforgeeks.org/how-to-show-values-on-seaborn-barplot/
    if  plot_options['bardatalabels']== True and hue !=None:
        f = "%"+bardataformat+""
        if plot_options["barcurrency"] == True: f = "$"+f # dollar
        for i in g.containers:
            g.bar_label(i,fontsize=plot_options['bardatafontsize'], fmt=f )
   
    # yaxis tick label format
    # https://matplotlib.org/stable/gallery/pyplots/dollar_ticks.html
    if plot_options["barcurrency"] == True:
        #y_ticks = _ax.get_yticks()
        if plot_options["bar_orientation"]=='v':
            _ax.yaxis.set_major_formatter('${x:1.2f}')
        if plot_options["bar_orientation"]=='h':
            _ax.xaxis.set_major_formatter('${x:1.2f}')
 
   
   # secondary y-axis
    if y2 != None:
       
        if isinstance(y2,list):
            y2_list = y2
        else:
            y2_list = [y2]

        _ax2 = _ax.twinx()
        
        
        for _y2 in y2_list:
            if plot_options['palette2'] !=None:
                g = sns.lineplot(data=df,x=x, y =_y2, hue=hue, palette=palette2,  ax=_ax2, label=_y2, 
                                 alpha = alpha2,ci = ci2, marker=marker2, estimator=estimator2)
            elif plot_options['color2'] !=None:
                g = sns.lineplot(data=df,x=x, y=_y2, hue=hue, color=color2,  ax=_ax2,label=_y2, 
                                 alpha=alpha2, ci=ci2, marker=marker2, estimator=estimator2)
            else:
                g = sns.lineplot(data=df,x=x, y=_y2, hue=hue, ax=_ax2, label=_y2, 
                                 alpha=alpha2, ci=ci2, marker=marker2, estimator=estimator2) 
                
        _ax2.grid(b=None)  
    
    # set axis params
    set_axisparams(plot_options,_ax,g)  # axis parameters from the plot_options dictionary
    
    if y2 != None:
        set_axisparams(plot_options,_ax2,g)  # axis parameters
    
        # set ylims 2 after general axis parameters 
        if plot_options['ylims2'] != None:
            _ax2.set_ylim(plot_options['ylims2'])
        
        # axis 2 legend
        if y2 != None and plot_options['legend']==True:
            _ax2.legend( loc=plot_options['legend_loc2'], prop={'size': plot_options['legendsize']})
    

    if ax==None and test_mode==False: plt.show() # if barplot created the figure then plt.show()
    
    return None


def lineplot(df, x, y, y2=None, ax=None, test_mode=False,  **kwargs):
    """Lineplot function designed for ease of use and aesthetics. Based on the
    Seaborn lineplot function with improvements, such as secondary axis, ease of use, and 
    improved default parameters. Refer to beautiful plot_defauts for full list of options.
 
    Args:
        df (Dataframe): The input DataFrame containing colums corresponding to x and y     
            
        x: Dataframe column corresponding to the lineplot x-axis
            aldfsd;lfj
        
        y: Dataframe column corresponding to the lineplot y-axis
            
        y2: Column name correspondng to the secondary axis, default = None 

    Returns:
        returns None if processing completes succesfully (without errors).
    """ 
    plot_options = get_kwargs(**kwargs)
    estimator = plot_options['estimator']
    estimator2 = plot_options['estimator2']
    hue = plot_options['hue']
    color = plot_options['color']
    ci2 = plot_options['ci2']
    alpha = plot_options['alpha']
    alpha2 = plot_options['alpha2']
    hue = plot_options['hue']
    bar_orientation= plot_options['bar_orientation']
    palette = plot_options['palette']
    palette2 = plot_options['palette2']
    marker = plot_options['marker']
    marker2 = plot_options['marker2']
    color = plot_options['color']
    color2 = plot_options['color2']
    
    # get back to the default plot options
    if ax == None: 
        mpl.rcParams.update(mpl.rcParamsDefault) # reset plot/figure parameters
        plt.style.use(plot_options['pltstyle'])
        fig,_ax = plt.subplots(nrows=1, ncols=1, figsize=plot_options['figsize']) 
    else: _ax = ax
    

    # Primary Y ... loop over each element
    if isinstance(y,list):
        y_list = y
    else:
        y_list =[y]
    for _y in y_list:
        if plot_options['palette'] !=None:
            g = sns.lineplot(data=df,x=x, y=_y, hue=hue, palette=palette,  ax=_ax, label=_y, 
                             alpha = alpha, ci=ci2, marker=marker, estimator=estimator)
        elif plot_options['color'] !=None:
            g = sns.lineplot(data=df,x=x,y=_y, hue=hue, color=None,  ax=_ax,label=_y, 
                             alpha = alpha, markers=marker, estimator=estimator)
        else:
            g = sns.lineplot(data=df,x=x,y=_y, hue=hue, ax=_ax, label=_y,
                             alpha= alpha, markers=marker, estimator=estimator  )
            
            
    # second y_axis ... plot this first so that primary y is plotted over secondary
    if y2 != None:
        if isinstance(y2,list):
            y2_list = y2
        else:
            y2_list = [y2]
    
        _ax2 = _ax.twinx()
        
        for _y2 in y2_list:
            if plot_options['palette2'] !=None:
                g = sns.lineplot(data=df,x=x, y =_y2, hue=hue, palette=palette2,  ci=ci2,
                                 ax=_ax2, label=_y2, alpha = alpha2, markers=marker2,
                                 estimator=estimator2)
            elif plot_options['color2'] !=None:
                g = sns.lineplot(data=df,x=x, y=_y2, hue=hue, color=color2,  ci=ci2,
                                 ax=_ax2,label=_y2, alpha=alpha2, marker=marker2,
                                 estimator=estimator2)
            else:
                g = sns.lineplot(data=df,x=x, y=_y2, hue=hue, ax=_ax2, label=_y2, ci=ci2,
                                 alpha=alpha2, marker=marker2,
                                 estimator=estimator2) 
                
        _ax2.grid(b=None)        
            
    # yaxis currency
    if plot_options["yaxis_currency"] == True:
        if plot_options['ytick_format'] !=None:
            f="${x:"+plot_options["ytick_format"]+"}"
            _ax.yaxis.set_major_formatter(f)
        else:
            _ax.yaxis.set_major_formatter('${x:.2f}')
           
    # legend
    if plot_options['legend_labels']!=None:
        _ax.legend(labels=plot_options['legend_labels'])
    
    if plot_options['legend']==True:
        _ax.legend( loc=plot_options['legend_loc'], prop={'size': plot_options['legendsize']})  
    
    # Set Axis Parameters
    set_axisparams(plot_options,_ax,g)  # axis parameters
    if y2 != None:
        set_axisparams(plot_options,_ax2,g)  # axis 2 parameters
        
        # set ylims after set_axis ... set_axis lims defaults to primary y axis 
        if plot_options['ylims2'] != None:
            _ax2.set_ylim(plot_options['ylims2'])
        
        # axis 2 legend
        if y2 != None and plot_options['legend']==True:
            _ax2.legend( loc=plot_options['legend_loc2'], prop={'size': plot_options['legendsize']})
        
    # plot show if easy lineplot created the figure
    if ax==None and test_mode==False: plt.show() # if simpl_plot created the figure then plt.show()
    
    return None