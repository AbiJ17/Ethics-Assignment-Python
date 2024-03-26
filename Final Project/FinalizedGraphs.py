"""
Description: Display relevant charts/graphs of collected data from the survey using the matplotlib library
to generate the figures and the pandas library to read the csv file
"""

import matplotlib.pyplot as plt     # Import the necessary library for creating the graphs
import pandas as pd                 # Import the pandas library for reading the csv file


def figure1():
    # Load data from CSV file
    df = pd.read_csv('Final Project/surveydata.csv')

    # Subset the DataFrame to include only the column with the question you want to plot
    question_df = df['Have you experimented with ChatGPT? ']

    # Count the frequency of each unique response in the column
    value_counts = question_df.value_counts()

    # Set colors for the wedges
    colors = ['#FFA500', '#1f77b4']

    # Create a pie chart of the frequency counts
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Have you experimented with ChatGPT? (General)')
    plt.show()


def figures2_and_3():
    # Load data from CSV file
    df = pd.read_csv('Final Project/surveydata.csv')

    # Create two separate data frames for STEM and non-STEM departments
    stem_df = df[(df['Which Faculty/Program are you in? '] != 'Arts/Humanities')
                 & (df['Which Faculty/Program are you in? '] != 'Business/Commerce')
                 & (df[
                        'Which Faculty/Program are you in? '] != 'Communication & Design (Fashion, Journalism, Media...)')
                 & (df['Which Faculty/Program are you in? '] != 'Law')]
    non_stem_df = df[(df['Which Faculty/Program are you in? '] == 'Arts/Humanities')
                     | (df['Which Faculty/Program are you in? '] == 'Business/Commerce')
                     | (df[
                            'Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)')
                     | (df['Which Faculty/Program are you in? '] == 'Law')]

    # Calculate the number of responses for each rating for STEM and non-STEM departments
    stem_counts = stem_df[
        'Have you experimented with ChatGPT? '].value_counts().sort_index()
    non_stem_counts = non_stem_df[
        'Have you experimented with ChatGPT? '].value_counts().sort_index()

    # Set colors for the wedges
    colors = ['#1f77b4', '#FFA500']

    # Create a figure with two subplots for the two pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Have you experimented with ChatGPT?')

    # Create the STEM pie chart
    ax1.pie(stem_counts, labels=stem_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('STEM Departments', y=0.8)

    # Create the non-STEM pie chart
    ax2.pie(non_stem_counts, labels=non_stem_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title('Non-STEM Departments', y=0.8)

    # Display the pie charts
    plt.show()


def figure4():
    # Load data from CSV file
    df = pd.read_csv("Final Project/surveydata.csv")

    # Subset the DataFrame to include only the column with the question to be plotted
    question_df = df['Do you think Post-Secondary schools should allow the use of ChatGPT?']

    # Count the frequency of each unique response in the column
    value_counts = question_df.value_counts()

    # Set colors for the wedges
    colors = ['#1f77b4', '#FFA500', '#00AA00']

    # Create a pie chart of the frequency counts
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Do you think Post-Secondary schools should allow the use of ChatGPT? (General)')
    plt.show()


def figures5_and_6():
    # Load data from CSV file
    df = pd.read_csv("Final Project/surveydata.csv")

    # Create two separate data frames for STEM and non-STEM departments
    stem_df = df[(df['Which Faculty/Program are you in? '] != 'Arts/Humanities')
                 & (df['Which Faculty/Program are you in? '] != 'Business/Commerce')
                 & (df[
                        'Which Faculty/Program are you in? '] != 'Communication & Design (Fashion, Journalism, Media...)')
                 & (df['Which Faculty/Program are you in? '] != 'Law')]
    non_stem_df = df[(df['Which Faculty/Program are you in? '] == 'Arts/Humanities')
                     | (df['Which Faculty/Program are you in? '] == 'Business/Commerce')
                     | (df[
                            'Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)')
                     | (df['Which Faculty/Program are you in? '] == 'Law')]

    # Calculate the number of responses for each rating for STEM and non-STEM departments
    stem_counts = stem_df[
        'Do you think Post-Secondary schools should allow the use of ChatGPT?'].value_counts().sort_index()
    non_stem_counts = non_stem_df[
        'Do you think Post-Secondary schools should allow the use of ChatGPT?'].value_counts().sort_index()

    # Set colors for the wedges
    colors = ['#FFA500', '#00AA00', '#1f77b4']

    # Create a figure with two subplots for the two pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Do you think Post-Secondary schools should allow the use of ChatGPT?')

    # Create the STEM pie chart
    ax1.pie(stem_counts, labels=stem_counts.index, autopct='%1.1f%%', startangle=190, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('STEM Departments', y=0.88)

    # Create the non-STEM pie chart
    ax2.pie(non_stem_counts, labels=non_stem_counts.index, autopct='%1.1f%%', startangle=190, colors=colors)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title('Non-STEM Departments', y=0.88)

    # Display the pie charts
    plt.show()


def figure7():
    # Load data from CSV file
    df = pd.read_csv('Final Project/surveydata.csv')

    # Subset the DataFrame to include only the column with the question to be plotted
    question_df = df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']

    # Count the frequency of each unique response in the column
    value_counts = question_df.value_counts().sort_index()

    # Set the width of each bar
    width = 0.35

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1, 6), value_counts.values, width=width)

    # Display the exact number of responses per rating
    for i, v in enumerate(value_counts.values):
        plt.text(i + 0.90, v + 0.5, str(int(v)), color='black', fontweight='bold')

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (General)')

    # Show the graph
    plt.show()


def figure8():
    # Load data from CSV file
    df = pd.read_csv("Final Project/surveydata.csv")

    # Create two separate data frames for STEM and non-STEM departments
    stem_df = df[(df['Which Faculty/Program are you in? '] != 'Arts/Humanities')
                 & (df['Which Faculty/Program are you in? '] != 'Business/Commerce')
                 & (df[
                        'Which Faculty/Program are you in? '] != 'Communication & Design (Fashion, Journalism, Media...)')
                 & (df['Which Faculty/Program are you in? '] != 'Law')]
    non_stem_df = df[(df['Which Faculty/Program are you in? '] == 'Arts/Humanities')
                     | (df['Which Faculty/Program are you in? '] == 'Business/Commerce')
                     | (df[
                            'Which Faculty/Program are you in? '] == 'Communication & Design (Fashion, Journalism, Media...)')
                     | (df['Which Faculty/Program are you in? '] == 'Law')]

    # Calculate the number of responses for each rating for STEM and non-STEM departments
    stem_counts = stem_df[
        'On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?'].value_counts().sort_index()
    non_stem_counts = non_stem_df[
        'On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?'].value_counts().sort_index()

    # Set the width of each bar
    width = 0.35

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1, 6), stem_counts.values, width=width, label='STEM')

    # Shift the x values for the second set of bars
    non_stem_shifted = [x + width for x in range(1, 6)]

    plt.bar(non_stem_shifted, non_stem_counts.values, width=width, label='non-STEM')

    # Display the exact number of responses per rating
    for i, v in enumerate(stem_counts.values):
        plt.text(i + 0.90, v + 0.5, str(int(v)), color='black', fontweight='bold')

    for i, v in enumerate(non_stem_counts.values):
        plt.text(i + 1.25, v + 0.5, str(int(v)), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (STEM vs non-STEM)')

    # Show the graph
    plt.show()


def figure9():
    # Load data from csv file
    df = pd.read_csv('Final Project/surveydata.csv')

    # Create two separate data frames for yes responses and no responses
    yes_df = df[df['Have you experimented with ChatGPT? '] == 'Yes']
    x_yes = yes_df[
        'On a scale of 1-5, are you concerned that the use of ChatGPT for academic purposes may promote academic dishonesty or cheating?']
    y_yes = x_yes.value_counts().sort_index().reindex(range(1, 6), fill_value=0)

    no_df = df[df['Have you experimented with ChatGPT? '] == 'No']
    x_no = no_df[
        'On a scale of 1-5, are you concerned that the use of ChatGPT for academic purposes may promote academic dishonesty or cheating?']
    y_no = x_no.value_counts().sort_index().reindex(range(1, 6), fill_value=0)

    # Set the width of each bar
    width = 0.3

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1, 6), y_yes.values, color='green', width=width, label="Have Used ChatGPT")

    # Shift the x values for the second set of bars
    x_no_shift = [x + width for x in range(1, 6)]

    plt.bar(x_no_shift, y_no.values, color='red', width=width, label="Have Not Used ChatGPT")

    # Display the exact number of responses per rating
    for i, v in enumerate(y_yes.values):
        plt.text(i + 0.88, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_no.values):
        plt.text(i + 1.2, v + 0.5, str(v), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # The range of the rating is 1-6, so use xticks() to change the range of rating to 1-5
    plt.xticks(range(1, 6))

    # Graph labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('ChatGPT Promoting Academic Dishonesty or Cheating')

    # Show the graph
    plt.show()


def figure10():
    # Load data from csv file
    df = pd.read_csv("Final Project/surveydata.csv")

    # Create two separate data frames for years 1/2 and year 3+
    young_df = df[(df['What is your year of study?'] == '1')
                  | (df['What is your year of study?'] == '2')]

    old_df = df[(df['What is your year of study?'] != '1')
                & (df['What is your year of study?'] != '2')]

    # Calculate the number of responses for each rating
    young_counts = young_df[
        'On a scale of 1-5, are you concerned that the use of ChatGPT for academic purposes may promote' \
        ' academic dishonesty or cheating?'].value_counts().sort_index().reindex(range(1, 6), fill_value=0)
    old_counts = old_df[
        'On a scale of 1-5, are you concerned that the use of ChatGPT for academic purposes may promote' \
        ' academic dishonesty or cheating?'].value_counts().sort_index().reindex(range(1, 6), fill_value=0)

    # Set the with of each bar
    width = 0.3

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1, 6), young_counts.values, color='green', width=width, label="First/Second Year")

    # Shift the x values for the second set of bars
    x_no_shift = [x + width for x in range(1, 6)]

    plt.bar(x_no_shift, old_counts.values, color='red', width=width, label="Third Year+")

    # Display the exact number of responses per rating
    for i, v in enumerate(young_counts.values):
        plt.text(i + 0.88, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(old_counts.values):
        plt.text(i + 1.2, v + 0.5, str(v), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # The range of the rating is 1-6, so use xticks() to change the range of rating to 1-5
    plt.xticks(range(1, 6))

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('ChatGPT Promoting Academic Dishonesty or Cheating depending on Year of Study')

    # Show the graph
    plt.show()


def figure11():
    # Load data from csv file
    df = pd.read_csv('Final Project/surveydata.csv')

    student_df = df[df['Are you currently employed?'] == 'No, just a student']
    x_student = student_df['On a scale of 1-5, how much do you rely on ChatGPT for work?']
    y_non_employed = x_student.value_counts().sort_index().reindex(range(1, 6), fill_value=0)

    # Create two separate data frames for employed and non-employed students
    employed_df = df[(df['Are you currently employed?'] == 'Yes, self-employed')
                     | (df['Are you currently employed?'] == 'Yes, employed part-time')
                     | (df['Are you currently employed?'] == 'Yes, employed full-time')]

    y_employed = employed_df[
        'On a scale of 1-5, how much do you rely on ChatGPT for work?'].value_counts().sort_index().reindex(range(1, 6),
                                                                                                            fill_value=0)

    # Set the width of each bar
    width = 0.35

    # Set the x values of the graphs to 1 - 5 and set the y values of the graphs to number of responses
    plt.bar(range(1, 6), y_non_employed.values, width=width, label='Non-Employed')

    # Shift the x values for the second set of bars
    x_employed_shifted = [x + width for x in range(1, 6)]

    plt.bar(x_employed_shifted, y_employed.values, width=width, label='Employed')

    # Display the exact number of responses per rating
    for i, v in enumerate(y_non_employed.values):
        plt.text(i + 0.90, v + 0.5, str(int(v)), color='black', fontweight='bold')

    for i, v in enumerate(y_employed.values):
        plt.text(i + 1.25, v + 0.5, str(int(v)), color='black', fontweight='bold')

    # Add a legend
    plt.legend()

    # Graph Labels
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Reliance of ChatGPT for work (Non-Employed vs Self-Employed)')

    # Show the graph
    plt.show()


# Main function
if __name__ == "__main__":

    # Initialize flag variable to be true for loop to function
    flag = True

    # Loop iterates when flag is True
    while flag:

        # Prompt user to choose which graph to display
        print("\nType the graph(s) you want to display (1-9) ")
        print("Figures 2 and 3 == 2")
        print("Figures 5 and 6 == 4")
        print("0 to quit")

        # Store user input
        choice = int(input())

        # Display certain graph(s) depending on user input
        if choice == 1:
            figure1()

        elif choice == 2:
            figures2_and_3()

        elif choice == 3:
            figure4()

        elif choice == 4:
            figures5_and_6()

        elif choice == 5:
            figure7()

        elif choice == 6:
            figure8()

        elif choice == 7:
            figure9()

        elif choice == 8:
            figure10()

        elif choice == 9:
            figure11()

        # Set flag to be false, breaking out of the loop, ultimately terminating the program
        elif choice == 0:
            flag = False

        # Prompt user for valid number if invalid input
        else:
            print("Please enter valid number!")