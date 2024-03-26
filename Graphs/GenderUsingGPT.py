import matplotlib.pyplot as plt
import pandas as pd

def GenderUsingGPT():
    
    # Load data from CSV file
    df = pd.read_csv("data.csv")

    # Create two separate data frames for STEM and non-STEM departments
    male_df = df[(df['What is your gender?'] != 'Male')]
    female_df = df[(df['What is your gender?'] == 'Female')]
    other_df = df[(df['What is your gender?'] == 'Prefer not to say')]

    # Calculate the number of responses for each rating for Male, Female and Other departments
    male_counts = male_df['Have you experimented with ChatGPT? '].value_counts().sort_index()
    female_counts = female_df['Have you experimented with ChatGPT? '].value_counts().sort_index()
    other_counts = other_df['Have you experimented with ChatGPT? '].value_counts().sort_index()


    # Create a figure with two subplots for the three pie charts
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('Have you experimented with ChatGPT? (Genders)')

    # Create the Male pie chart
    ax1.pie(male_counts, labels=male_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Male', y = 0.9)

    # Create the Female pie chart
    ax2.pie(female_counts, labels=female_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title('Female', y = 0.9)

    # Create the other genders pie chart
    ax3.pie(other_counts, labels=other_counts.index, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax3.set_title('Other', y = 0.9)

    # Display the pie charts
    plt.show()

if __name__ == "__main__":
   GenderUsingGPT()