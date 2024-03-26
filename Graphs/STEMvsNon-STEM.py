import matplotlib.pyplot as plt
import pandas as pd

def accurateGPT():
    df = pd.read_csv('data.csv')

    # Get the number of responses from the science department
    science_df = df[df['Which Faculty/Program are you in? '] == 'Science (Computer Science, Biology, Chemistry, Physics, Mathematics...)']
    x_science = science_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_science = x_science.value_counts().sort_index()

    # Get the number of responses from the medicine/health science department
    medicine_df = df[df['Which Faculty/Program are you in? '] == 'Medicine/Health Science']
    x_medicine = medicine_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_medicine = x_medicine.value_counts().sort_index()

    # Get the number of responses from the engineering department
    engineering_df = df[df['Which Faculty/Program are you in? '] == 'Engineering/Architectural Science']
    x_engineering = engineering_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_engineering = x_engineering.value_counts().sort_index()

    # Combine the value counts of all STEM departments
    y_stem = y_science.add(y_medicine, fill_value = 0).add(y_engineering, fill_value = 0)


    # Get the number of responses from the arts/humanities department
    arts_df = df[df['Which Faculty/Program are you in? '] == 'Arts/Humanities']
    x_arts = arts_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_arts = x_arts.value_counts().sort_index()

    # Get the number of responses from the Business/Commerce department
    business_df = df[df['Which Faculty/Program are you in? '] == 'Business/Commerce']
    x_business = business_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_business = x_business.value_counts().sort_index()

    # Get the number of responses from the communications & design department
    communications_df = df[df['Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)']
    x_communications = communications_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_communications = x_communications.value_counts().sort_index()

    # Get the number of responses from the law department
    law_df = df[df['Which Faculty/Program are you in? '] == 'Law']
    x_law = law_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_law = x_law.value_counts().sort_index()

    # Get the number of responses from the social sciences department
    social_df = df[df['Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)']
    x_social = social_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_social = x_social.value_counts().sort_index()

    # Combine the values of all non-STEM departments
    y_non_stem = y_arts.add(y_business, fill_value = 0).add(y_communications, fill_value = 0).add(y_law, fill_value = 0).add(y_social, fill_value = 0)

    #Set the width of the bars 
    width = 0.35

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1,6), y_stem.values, width = width, label='STEM')

    # Shift the x values for the second set of bars
    x_non_stem_shifted = [x + width for x in range(1, 6)]

    plt.bar(x_non_stem_shifted, y_non_stem.values, width = width, label='non-STEM')

    # Display the exact number of responses per rating
    for i, v in enumerate(y_stem.values):
        plt.text(i + 0.88, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_non_stem.values):
        plt.text(i + 1.2, v + 0.5, str(v), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (STEM vs non-STEM)')

    # Show the graph
    plt.show()


if __name__ == "__main__":
    accurateGPT()
