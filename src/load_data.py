import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

def gen_metadata():
    """
    Loads the data from the csv file, derives some metadata and returns the dataframe
    """
    # Read file from data directory
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    file_path = 'data/Preprocessed_AFData.csv'
    relative_path = os.path.join(parent_dir, file_path)
    data = pd.read_csv(relative_path)

    # Print some metadata about the classes
    (unique,counts) = np.unique(data['Control'],return_counts=True)
    print("Data in the 'Control' column: {} \nRatio of occurrences of each class: {}\n".format(dict(zip(unique,counts)),dict(zip(unique,counts/len(data['Control'])))))

    # display counts on a graph and save it
    target_variables = ['Non-AF','AF']
    sns.set_theme(style='whitegrid')
    sns.barplot(x=target_variables,y=counts)
    plt.title('Count of AF and Non-AF occurrences in the Preprocessed data')
    plt.ylabel('Count')

    for i in range(len(counts)):
        plt.text(i-0.25, counts[i]+0.5, counts[i], color='black', fontweight='bold')
    img_file_path = 'images/count_of_AF_and_Non_AF_occurrences.png'
    plt.savefig(os.path.join(parent_dir, img_file_path))
    return data