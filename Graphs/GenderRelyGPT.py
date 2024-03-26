import matplotlib.pyplot as plt
import pandas as pd

def genRelyGPT():

    # Read the data from the csv file
    df = pd.read_csv('data.csv')

    # Get the number of responses from males
    male_df = df[(df['What is your gender?'] != 'Male')]
    x_male = male_df['On a scale of 1-5, how much do you rely on ChatGPT for work?']
    y_male = x_male.value_counts(sort = False).reindex(range(1,6), fill_value = 0)   # Fills in empty values from the csv files with 0 

    # Get the number of responses from females
    female_df = df[(df['What is your gender?'] == 'Female')]
    x_female = female_df['On a scale of 1-5, how much do you rely on ChatGPT for work?']
    y_female = x_female.value_counts(sort = False).reindex(range(1,6), fill_value = 0)   # Fills in empty values from the csv files with 0 

    # Get the number of responses from other genders
    other_df = df[(df['What is your gender?'] == 'Prefer not to say')]
    x_other = other_df['On a scale of 1-5, how much do you rely on ChatGPT for work?']
    y_other = x_other.value_counts(sort = False).reindex(range(1,6), fill_value = 0)   # Fills in empty values from the csv files with 0 

    #Set the width of the bars 
    width = 0.2

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses (1st bar)
    plt.bar(range(1,6), y_male.values, width = width, label='Male')

    # Shift the x values for the second set of bars
    x_male_shifted = [x + width for x in range(1, 6)]

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses (2nd bar)
    plt.bar(x_male_shifted, y_female.values, width = width, label='Female')

     # Shift the x values for the third set of bars
    x_female_shifted = [x + 0.2 + width for x in range(1, 6)]

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses (3rd bar)
    plt.bar(x_female_shifted, y_other.values, width = width, label='Other')

    # Display the exact number of responses per rating
    for i, v in enumerate(y_male.values):
        plt.text(i + 0.9, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_female.values):
        plt.text(i + 1.15, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_other.values):
        plt.text(i + 1.35, v + 0.5, str(v), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Relying on ChatGPT for Work (Genders)')

    # Show the graph
    plt.show()


if __name__ == "__main__":
    genRelyGPT()
