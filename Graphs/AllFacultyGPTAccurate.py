import matplotlib.pyplot as plt
import pandas as pd


def allFacultyGPTAccurate():
    df = pd.read_csv('data.csv')

    science_df = df[df['Which Faculty/Program are you in? '] == 'Science (Computer Science, Biology, Chemistry, Physics, Mathematics...)']
    x_science = science_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_science = x_science.value_counts(sort = False).reindex(range(1,6), fill_value = 0)
    
    engineering_df = df[df['Which Faculty/Program are you in? '] == 'Engineering/Architectural Science']
    x_engineering = engineering_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_engineering = x_engineering.value_counts(sort = False).reindex(range(1,6), fill_value = 0)

    business_df = df[df['Which Faculty/Program are you in? '] == 'Business/Commerce']
    x_business = business_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_business = x_business.value_counts(sort = False).reindex(range(1,6), fill_value = 0)

    medicine_df = df[df['Which Faculty/Program are you in? '] == 'Medicine/Health Science']
    x_medicine = medicine_df['On a scale of 1-5, how accurate is the information/answers provided by ChatGPT?']
    y_medicine = x_medicine.value_counts(sort = False).reindex(range(1,6), fill_value = 0)

    width = 0.15

    plt.bar(range(1,6), y_science.values, width = width, label = "Science")

    x_engineering_shift = [(x+0.1) + width for x in range(1, 6)]

    plt.bar(x_engineering_shift, y_engineering.values, width = width, label = "Engineering")

    x_business_shift = [(x+0.3) + width for x in range(1, 6)]

    plt.bar(x_business_shift, y_business.values, width = width, label = "Business")

    x_medicine_shift = [(x+0.5) + width for x in range(1, 6)]

    plt.bar(x_medicine_shift, y_medicine.values, width = width, label = "Medicine")

    for i, v in enumerate(y_science.values):
        plt.text(i + 0.92, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_engineering.values):
        plt.text(i + 1.17, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_business.values):
        plt.text(i + 1.38, v + 0.5, str(v), color='black', fontweight='bold')

    for i, v in enumerate(y_medicine.values):
        plt.text(i + 1.58, v + 0.5, str(v), color='black', fontweight='bold')


    plt.legend(title = "Faculty Key") 

    # The range of the rating is 1-6, so use xticks() to change the range of rating to 1-5
    plt.xticks(range(1,6))


    plt.xlabel('Rating')
    plt.ylabel('Number of Responses')
    plt.title('Accuracy of Information/Answers by ChatGPT (Science vs Engineering Faculty)')


    plt.show()
    


if __name__ == "__main__":
    allFacultyGPTAccurate()
