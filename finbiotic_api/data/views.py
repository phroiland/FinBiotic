from rest_pandas import PandasSimpleView
import pandas as pd
import os

CSV_DIR = os.environ.get('CSV_DIR', None)


class TimeSeriesView(PandasSimpleView):

    def get_data(self, request, *args, **kwargs):

        return pd.read_csv(os.path.join(CSV_DIR, '%s_%s.csv' % ('EUR_USD', 'Hourly')))
