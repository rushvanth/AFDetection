"""This module loads the pre-processed data, extracts some metadata from it
and then returns the dataframe for classifying"""
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def gen_metadata():
    """
    Loads the data from the csv file, counts number of occurrences in each target class,
    visualizes the data in the form of a barplot, and then returns the dataframe for
    further classifications.
    """
    # Read file from data directory
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    file_path = 'data/Preprocessed_AFData.csv'
    relative_path = os.path.join(parent_dir, file_path)
    data = pd.read_csv(relative_path)
    # Print some metadata about the classes
    (unique,counts) = np.unique(data['Control'],return_counts=True)
    print("Metadata:\n" + "-"*50 + "\n")
    print(f"Classes: {str(unique)} \n")
    print("Class Labels: \n 0 - Non AF\n 1 - AF\n")
    print(f"Data in the 'Control' column: {dict(zip(unique,counts))} \n")
    print(f"Ratio of occurrences of each class: {dict(zip(unique,counts/len(data['Control'])))}\n")
    print("-"*50 + "\n")
    # display counts on a graph and save it
    target_variables = ['Non-AF','AF']
    sns.set_theme(style='whitegrid')
    sns.barplot(x=target_variables,y=counts)
    plt.title('Count of AF and Non-AF occurrences in the Preprocessed data')
    plt.ylabel('Count')
    for i,_ in enumerate(counts):
        plt.text(i-0.25, counts[i]+0.5, counts[i], color='black', fontweight='bold')
    img_file_path = 'images/general/count_of_AF_and_Non_AF_occurrences.png'
    plt.savefig(os.path.join(parent_dir, img_file_path))
    return data
    