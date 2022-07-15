import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

import  beautifulplots.beautifulplots as bp  

def lineplot(df, x, y, yaxisformat="1.2f", ycurrency=None,
             y2=None,y2axisformat="1.2f", y2currency=None, 
             ax=None, test_mode=False, estimator=None, estimator2=None, **kwargs):
    """Lineplot function designed for ease of use and aesthetics. Based on the
    Seaborn lineplot function with improvements, such as secondary axis, ease of use, and 
    improved default parameters. Refer to beautiful plot_defauts for full list of options.
 
    Args:
        df (Dataframe): The input DataFrame containing colums corresponding to x and y     
            
        x: Dataframe column corresponding to the lineplot x-axis
            aldfsd;lfj
        
        y: Dolumn or list of columns corresponding to the lineplot y-axis
            
        y2: Column or list of columns correspondng to the secondary axis, default = None 
        
        estimator: Specifies how to summarize data corresponding to y-axis. Defaults to plot all data points do not summarize.
        
        estimator2: Specifies how to summarize data corresponding to y2-axis. Defaults to plot all data points do not summarize.


    Returns:
        returns None if processing completes succesfully (without errors).
    """ 
    #***
 
    plot_options = bp.get_kwargs(**kwargs)
    hue = plot_options['hue']
    color = plot_options['color']
    ci2 = plot_options['ci2']
    alpha = plot_options['alpha']
    alpha2 = plot_options['alpha2']
    hue = plot_options['hue']
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
            g = sns.lineplot(data=df,x=x,y=_y, hue=hue, color=color,  ax=_ax,label=_y, 
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
            
    # yaxis format
            
      
    # y axis Parameters primary axis
    bp.set_axisparams(plot_options,_ax,g)  # axis parameters
    bp.set_yaxis_format(_ax,yaxisformat, ycurrency)
    
    # y2 axis parameters
    if y2 != None:

        bp.set_axisparams(plot_options,_ax2,g)  # axis 2 parameters
        
        # set ylims after set_axis ... set_axis lims defaults to primary y axis 
        if plot_options['ylims2'] != None:
            _ax2.set_ylim(plot_options['ylims2'])
        
        # axis 2 legend
        handles, labels = _ax2.get_legend_handles_labels()
        if y2 != None and handles:
            _ax2.legend( loc=plot_options['legend_loc2'], prop={'size': plot_options['legendfontsize']})

        bp.set_yaxis_format(_ax2,y2axisformat, y2currency)
        
    # plot show if easy lineplot created the figure
    if ax==None and test_mode==False: plt.show() # if simpl_plot created the figure then plt.show()
    
    return None