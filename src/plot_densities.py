import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt


def plot_densities(data):
    '''
    Plot features densities depending on the outcome values
    '''
    # change fig size to fit all subplots beautifully 
    rcParams['figure.figsize'] = 15, 30
    names = list(data.columns)
    # separate data based on outcome values 
    outcome_0 = data[data['Control'] == 0]
    outcome_1 = data[data['Control'] == 1]

    # init figure
    fig, axs = plt.subplots(10, 1)
    fig.suptitle('Features densities for different outcomes 0/1')
    plt.subplots_adjust(left = 0.25, right = 0.9, bottom = 0.1, top = 0.95,
                        wspace = 0.2, hspace = 0.9)

    # plot densities for outcomes
    i=0
    for column_name in names[10:20]: 
        ax = axs[i]
        #plt.subplot(4, 2, names.index(column_name) + 1)
        outcome_0[column_name].plot(kind='density', ax=ax, subplots=True, 
                                    sharex=False, color="red", legend=True,
                                    label=column_name + ' for Outcome = 0')
        outcome_1[column_name].plot(kind='density', ax=ax, subplots=True, 
                                     sharex=False, color="green", legend=True,
                                     label=column_name + ' for Outcome = 1')
        # ax.set_xlabel(column_name + ' values')
        # ax.set_title(column_name + ' density')
        ax.grid('on')
        ax.legend(loc='best')
        i+=1
    plt.show()
    fig.savefig('densities10-20.png')