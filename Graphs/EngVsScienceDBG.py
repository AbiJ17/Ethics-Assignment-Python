import matplotlib.pyplot as plt
import pandas as pd

def engVsSciGraph():
    df = pd.read_csv('data.csv')

    science_df = df[df['Which Faculty/Program are you in? '] == 'Science (Computer Science, Biology, Chemistry, Physics, Mathematics...)']
    x_science = science_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_science = x_science.value_counts().sort_index()
    
    engineering_df = df[df['Which Faculty/Program are you in? '] == 'Engineering/Architectural Science']
    x_engineering = engineering_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_engineering = x_engineering.value_counts().sort_index()

    width = 0.35

    plt.bar(range(1,6), y_science.values, width = width, label = "Science")

    x_engineering_shifted = []

    for i in range(1,6):
        x_engineering_shifted.append(i + width)

    plt.bar(x_engineering_shifted, y_engineering.values, width = width, label = "Engineering")

    for i, v in enumerate(y_science.values):
        plt.text(i + 0.88, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_engineering.values):
        plt.text(i + 1.2, v + 0.5, str(v), color='black', fontweight='bold')


    plt.legend(title = "Faculties Key") 

    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (Science vs Engineering Faculty)')


    plt.show()
    


if __name__ == "__main__":
    engVsSciGraph()
