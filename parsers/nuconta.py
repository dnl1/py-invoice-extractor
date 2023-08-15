from datetime import datetime
import pandas as pd
import os

class NuContaParser:

    def run(self):
        outputs_folder = 'outputs'
        filename = os.path.join('inputs', 'nuconta.csv')

        df = pd.read_csv(filename, delimiter=',')

        df['Data'] = df['Data'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))

        column_mapping = {
            'Data': 'Date',
            'Descrição': 'Description',
            'Valor': 'Value'
        }

        df.rename(columns=column_mapping, inplace=True)

        columns_to_remove = ['Identificador']

        df.drop(columns=columns_to_remove, inplace=True)

        df['Amount'] = 1
        df['Value'] = df['Value'] * -1 # To import as transaction we had to invert the logic

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create the outputs folder if it doesn't exist
        os.makedirs(outputs_folder, exist_ok=True)

        # Create the output CSV file path with the timestamp
        output_csv_path = os.path.join(outputs_folder, f'nuconta_{timestamp}.csv')

        df.to_csv(output_csv_path, index=False)
