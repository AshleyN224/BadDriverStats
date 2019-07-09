# Standard Built-In Libraries
import csv
import sys 

# Third Party Libraries
import plotly # For analyzing data and creating graphs/charts
import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import pandas as pd
import pyfiglet # for greeting art

# Plotly Access
api_key = 'i8mSAWHnjJ1KlCcHxH7s' # personal API Key
plotly.tools.set_credentials_file(username='AshleyN224', api_key=api_key) # ploptly access
plotly.tools.set_config_file(world_readable=True, sharing='public') # Keeping data private (for paying customers only)
print('Data Stats Version: 1.0')
print('Plotly Version:', plotly.__version__) # Prints the working version of plotly

def usageOptions():
    '''Display usage options to user on invalid input or when -h is called.'''
    print('\nUsage Options\n'
        +'- Get fatal collsion statitics by state:\n'
        +'\t> python Plotting.py -stats\n'
        +'\t> python Plotting.py -stats [state]\n\n'
        +'- Get pie or bar chart illustrating statistics of a state:\n'
        +'\t> python Plotting.py -pie or -bar\n'
        +'\t> python geotweets.py -pie [state] or -bar [state]\n\n'
        +'- Enter command line interface of the program:\n'
        +'\t> python Plotting.py'
        +'\n\nNote: Locations that have more than one word should be put in quotes. Example:\n'
        +'\t> python Plotting.py -stats \'Los Angeles\''
        +'\n\nNote: States are case sensitive. Example:\n'
        +'\t> python Plotting.py -stats \'Florida\'')

# Stating the filename
csvfile = 'bad-drivers.csv' # name of existing csv file 

# Converting CSV to Dataframe
df = pd.read_csv(csvfile, index_col=0) # index_col=0 removes the numbering system of the original datafram

# Sections of df
index = df.index # States
columns = df.columns # Headers
values = df.values # Data

def state_stats(state):
    '''Pulls data from CSV file and list the data based on the the state entered in the program.'''
    df = pd.read_csv(csvfile, index_col=0)
    data = df.loc[state]
    print('-' * 50)
    print('Driving statistics for {}: '.format(state))
    print('-' * 50)
    print(data)


def state_pie(state):
    '''
    Displays a pie chart in a browser, displaying the data from the CSV file based on the state entered in the program.
    When the mouse is hovering over a section of the pie chart, information is displayed about the section.
    '''
    df = pd.read_csv(csvfile, index_col=0)
    df1 = df.loc[:, ['Speeding (%)', 'Alcohol-Impaired (%)', 'Drivers Not Distracted (%)', 'Not Involved In Any Previous Accidents (%)']]
    location = df1.loc[state]
    values= list(location)
    labels = list(df1.columns.values)
    trace = go.Pie(labels=labels, values=values)
    plot([trace], filename='basic_pie_chart.html')

def state_bar(state):
    '''
    Displays a basic bar chart in a browser, displaying the data from the CSV file based on the state entered into the program.
    When the mouse is hovering over a section of the bar chart, information is desplayed about the section.
    '''
    df = pd.read_csv(csvfile, index_col=0)
    df1 = df.loc[:, ['Speeding (%)', 'Alcohol-Impaired (%)', 'Drivers Not Distracted (%)', 'Not Involved In Any Previous Accidents (%)']]
    vals = list(df1.loc[state])
    cols = list(df1.columns.values)

    data = [go.Bar(
        x = cols,
        y = vals
    )]
    plot(data, filename = 'basic-bar.html')



## MAIN ##


# give greeting and prompt user for inputs 
if len(sys.argv) == 1:
    # ascii art greeting
    print('-' * 50)
    art = pyfiglet.figlet_format("Driver Stats") 
    print(art)
    print('-' * 50)

    # loop that prompts user what they would like to do
    while True:
        choice = input('\nWhat would you like to do?\n(1) Get stats\n(2) Get pie chart\n(3) Get bar chart\n(4) Exit program\n\nEnter number: ')
        
        if choice == '1':
            try:
                state_stats(str(input('Enter state: ')))
            except:
                print('\n! ERROR: There are no stats for that state, please check the spelling.')

        elif choice == '2':
            try: 
                state = state_pie(str(input('Enter state: ')))
            except:
                print('\n! ERROR: There are no stats for that state, please check the spelling.')
        
        elif choice == '3':
            try:
                state = state_bar(str(input('Enter state:')))
            except:
                print('\n! ERROR: There are no stats for that state, please check the spelling.')
                
        elif choice == '4':
            print('Exiting. Goodbye!')
            sys.exit()

# display usage options
elif sys.argv[1] == '-h':
    usageOptions()

# get stats
elif sys.argv[1] == '-stats':
    # when user provides location via CLI
    if len(sys.argv) == 3:
        stats = state_stats(sys.argv[2])
        try:
            state_stats(state)
        except:
            print('\n! ERROR: There is no data for that state or it does not exist.\n') 
    
    # when user does not provide location via CLI
    elif len(sys.argv) == 2:
        state = state_stats(str(input('Enter state: ')))
        try:
            state_stats(state)
        except:
            print('\n! ERROR: There is no data for that state or it does not exist.\n') 

    # when user inputs more than one word for the location
    else:
        print('\n! ERROR: Locations that have more than one word should be put in quotes\n'
        +'Example: > python geotweet.py -trends \'Los Angeles\'\n')

# get pie chart
elif sys.argv[1] == '-pie':
    #  when user provides location via CLI
    if len(sys.argv) == 3:
        pie = state_pie(sys.argv[2])

    #  when user does not provide location via CLI
    elif len(sys.argv) == 2:
        pie = state_pie(str(input('Enter state: ')))

# get bar chart
elif sys.argv[1] == '-bar':
    #  when user provides location via CLI
    if len(sys.argv) == 3:
        bar = state_bar(sys.argv[2])

    #  when user does not provide location via CLI
    elif len(sys.argv) == 2:
        bar = state_bar(str(input('Enter state: ')))

else:
    print('\n! ERROR: Input not recognized. use the -h flag for usage instructions.\n')