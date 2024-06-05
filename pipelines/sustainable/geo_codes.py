from pipelines.util import *
import pandas as pd

'''
Adding geo codes to data city data.
'''

def get_relative_paths(dir):
    f_paths = []
    names = []
    for root, _, files in os.walk(dir):
        for file in files:
            f_paths.append(os.path.join(root, file))
            names.append(file.split("-")[1])
    return f_paths, names

if __name__ == '__main__':
    
    paths, names = get_relative_paths('working/datacity/netzero')
    # outs = [os.path.join('src/themes/sustainable-growth/netzero/_data/', f'{name}.csv') for name in ['business_counts', 'employee_counts', 'turnover']]

    codes = pd.read_csv('metadata/LADC_lookup_2022.csv', usecols=['LAD22NM', 'LAD22CD'])

    for path, name in zip(paths, names):
        data = pd.read_csv(f'{path}')
        data.rename(columns={'Local authority': 'LAD22NM'}, inplace=True)
        merged = data.merge(codes, how='inner', on='LAD22NM') 
        merged.to_csv(os.path.join('src/themes/sustainable-growth/netzero/_data/',f'{name}'))