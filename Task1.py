import pandas as pd
import matplotlib.pyplot as plt


def lineChart():

    """This function creates a line chart for percentage of daily new users
        for the message_data.csv file"""

    # Loading the CSV file
    data = pd.read_csv('message_data.csv')

    # Grouping the date-time instaces into each dates
    data['message_time'] = pd.to_datetime(data['message_time']).dt.date

    # Grouping each date with respective author IDs
    total_author_ids = data.groupby(data['message_time'])['author_id'].apply(list)

    percentage_new_author_ids = {} # Initializing an empty hash to store date - % new users
    current_authors = set() #Initializing an empty set to store cummilative number of users

    # Iterating over total_author_ids to calculate % new users
    for date, author_ids in total_author_ids.items():
        
        newCount = 0 #Initializing new user messages to zero.

        #Counting new user messages
        for author in author_ids:
            if author not in current_authors:
                newCount += 1

        current_authors = current_authors | set(author_ids) #Updating cummilative number of users.
        percentage_new_author_ids[date] = newCount / len(author_ids) * 100 # % of messages by users on each date.

    # Converting the hashmap to a pandas series
    percentage_new_author_ids = pd.Series(percentage_new_author_ids)

    # Plotting the matlibplot chart
    plt.title('Percentage of daily messages sent by new users')
    plt.xlabel('Date')
    plt.ylabel('Percentage_New_Messages')
    plt.plot(percentage_new_author_ids.index, percentage_new_author_ids)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    """Driver function"""
    lineChart()