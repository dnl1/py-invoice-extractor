from datetime import datetime
import pandas as pd
import os

class XpParser:

    def run(self):
        outputs_folder = 'outputs'
        filename = os.path.join('inputs', 'xp.csv')

        df = pd.read_csv(filename, delimiter=';')

        df['Valor'] = df['Valor'].str.replace('R\$', '')  # Remove "R$"
        df['Valor'] = df['Valor'].str.replace(',', '.')  # Replace commas with dots
        df['Valor'] = df['Valor'].str.replace('.', '')  # Replace commas with dots
        df['Data'] = df['Data'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))

        column_mapping = {
            'Data': 'Date',
            'Estabelecimento': 'Description',
            'Valor': 'Value'
        }

        df.rename(columns=column_mapping, inplace=True)

        columns_to_remove = ['Portador', 'Parcela']

        df.drop(columns=columns_to_remove, inplace=True)
        
        df['Amount'] = 1

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create the outputs folder if it doesn't exist
        os.makedirs(outputs_folder, exist_ok=True)

        # Create the output CSV file path with the timestamp
        output_csv_path = os.path.join(outputs_folder, f'xp_{timestamp}.csv')

        df.to_csv(output_csv_path, index=False)
