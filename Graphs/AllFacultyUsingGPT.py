import matplotlib.pyplot as plt
import pandas as pd


def allFacultyUsingGPT():

    # Read the survey results CSV file
    df = pd.read_csv('data.csv')

    # Get the number of responses from faculty of science
    science_df = df[df['Which Faculty/Program are you in? '] == 'Science (Computer Science, Biology, Chemistry, Physics, Mathematics...)']
    x_science = science_df['Have you experimented with ChatGPT? ']
    y_science = x_science.value_counts().sort_index()
    
     # Get the number of responses from faculty of engineering
    engineering_df = df[df['Which Faculty/Program are you in? '] == 'Engineering/Architectural Science']
    x_engineering = engineering_df['Have you experimented with ChatGPT? ']
    y_engineering = x_engineering.value_counts().sort_index()

    # Get the number of responses from faculty of business
    business_df = df[df['Which Faculty/Program are you in? '] == 'Business/Commerce']
    x_business = business_df['Have you experimented with ChatGPT? ']
    y_business = x_business.value_counts().sort_index()

    # Get the number of responses from faculty of medicine
    medicine_df = df[df['Which Faculty/Program are you in? '] == 'Medicine/Health Science']
    x_medicine = medicine_df['Have you experimented with ChatGPT? ']
    y_medicine = x_medicine.value_counts().sort_index()

    width = 0.1

    plt.bar(range(1,3), y_science.values, width = width, label = "Science")

    x_engineering_shift = [(x+0.1) + width for x in range(1, 3)]

    plt.bar(x_engineering_shift, y_engineering.values, width = width, label = "Engineering")

    x_business_shift = [(i+0.3) + width for i in range(1, 3)]

    plt.bar(x_business_shift, y_business.values, width = width, label = "Business")

    x_medicine_shift = [(x+0.5) + width for x in range(1, 3)]

    plt.bar(x_medicine_shift, y_medicine.values, width = width, label = "Medicine")

    for i, v in enumerate(y_science.values):
        plt.text(i + 0.93, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_engineering.values):
        plt.text(i + 1.15, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_business.values):
        plt.text(i + 1.35, v + 0.5, str(v), color='black', fontweight='bold')
    
    for i, v in enumerate(y_medicine.values):
        plt.text(i + 1.56, v + 0.5, str(v), color='black', fontweight='bold')


    plt.legend(title = "Faculty Key") 

    # Not displaying "Yes" and "No" as x-axis labels
    x_axis = df.iloc[1, :2].tolist()
    
    plt.xticks(range(len(x_axis)), x_axis)

    plt.xlabel('Rating')
    plt.ylabel('Answers')
    plt.title('Experimenting with ChatGPT (All Faculties)')


    plt.show()
    

if __name__ == "__main__":
    allFacultyUsingGPT()