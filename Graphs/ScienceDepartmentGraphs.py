import matplotlib.pyplot as plt
import pandas as pd

def sheetsGraphs():
    df = pd.read_csv('data.csv')

    science_df = df[df['Which Faculty/Program are you in? '] == 'Science (Computer Science, Biology, Chemistry, Physics, Mathematics...)']
    x_science = science_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_science = x_science.value_counts().sort_index()

    plt.bar(range(1,6), y_science.values)
    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (Science Faculty)')
    plt.show()


if __name__ == "__main__":
    sheetsGraphs()
