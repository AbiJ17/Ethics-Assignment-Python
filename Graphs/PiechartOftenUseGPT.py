import matplotlib.pyplot as plt
import pandas as pd

def piechartOftenUseGPT():
    
    # Load data from CSV file
    df = pd.read_csv("data.csv")

    # Create two separate data frames for STEM and non-STEM departments
    stem_df = df[(df['Which Faculty/Program are you in? '] != 'Arts/Humanities')
                & (df['Which Faculty/Program are you in? '] != 'Business/Commerce')
                & (df['Which Faculty/Program are you in? '] != 'Communication & Design (Fashion, Journalism, Media...)')
                & (df['Which Faculty/Program are you in? '] != 'Law')]
    non_stem_df = df[(df['Which Faculty/Program are you in? '] == 'Arts/Humanities')
                     | (df['Which Faculty/Program are you in? '] == 'Business/Commerce')
                     | (df['Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)')
                     | (df['Which Faculty/Program are you in? '] == 'Law')]

    # Calculate the number of responses for each rating for STEM and non-STEM departments
    stem_counts = stem_df['How often do you use ChatGPT? '].value_counts().sort_index()
    non_stem_counts = non_stem_df['How often do you use ChatGPT? '].value_counts().sort_index()

    # Create a figure with two subplots for the two pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('How often do you use ChatGPT?')

    # Create the STEM pie chart
    ax1.pie(stem_counts, labels=stem_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('STEM Departments', y = 0.9)

    # Create the non-STEM pie chart
    ax2.pie(non_stem_counts, labels=non_stem_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title('Non-STEM Departments', y = 0.9)

    # Display the pie charts
    plt.show()

if __name__ == "__main__":
   piechartOftenUseGPT()