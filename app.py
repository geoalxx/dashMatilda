from tools.helpers import pickle_to_dict
import pickle
from dash import Dash, dcc, html, Input, Output, callback
import os
import requests

# URL of the .pickle file
url = 'https://box.hu-berlin.de/f/76bd096c4be649be80db/?dl=1'

try:
    # # Download the file
    # response = requests.get(url)
    # response.raise_for_status()  # Ensure the request was successful
    #
    # # Load the pickle file content into a dictionary
    # data = pickle.loads(response.content)
    #
    # # Print or use the dictionary
    # k = list(data.keys())[0]

    state = 'a'

except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")
except pickle.UnpicklingError as e:
    print(f"Error unpickling the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# local_filename = 'matilda_scenarios.pickle'
#
# try:
#     matilda_scenarios = pickle_to_dict(f"matilda_scenarios.pickle")
#
#     state = 'a'
# except OSError as e:
#     print(e)
#
#     try:
#         state = 'b'
#         print('try downloading file...')
#
#         # Download the file
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#
#         # Save the file locally
#         with open(local_filename, 'wb') as f:
#             f.write(response.content)
#
#         print(f"File downloaded and saved as {local_filename}")
#
#         # matilda_scenarios = pickle_to_dict(f"C:\\Python\\matilda_edu\\output\\cmip6\\adjusted\\matilda_scenarios.pickle")
#         matilda_scenarios = pickle_to_dict(f"matilda_scenarios.pickle")
#
#         df = matilda_scenarios['SSP2']['MPI-ESM1-2-HR']['model_output']
#         print('DF length:', len(df))
#         state = 'c'
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error downloading the file: {e}")
#         state = 'd'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1(f'Hello World: {state}'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@callback(Output('display-value', 'children'), Input('dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run(debug=True)