import csv
import utilities
import os

csv.writer(open(os.path.join(utilities.dataset_path, 'eu_procurements.csv'), 'w+'),
           delimiter=' ').writerows(csv.reader(open(os.path.join(utilities.dataset_path, 'eu_procurements_c.csv')), delimiter='\t'))
