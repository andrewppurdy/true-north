import duckdb
from pipelines.util import *

URL = 'https://github.com/economic-analytics/edd/raw/main/data/parquet/RGVA_LAD.parquet'

if __name__ == "__main__":
    con = duckdb.connect()

    # @TODO write a generalised function of below
    # @TODO figure out why MAX('date') won't work
    data = con.execute(f"SELECT \"dates.date\" AS date, \"variable.name\", \"geography.code\", \"industry.name\", value FROM '{URL}' WHERE \"industry.name\"=='All industries' and \"variable.name\"=='GVA Current Prices £m' and date='2022-01-01';").fetchdf()

    # possible to rewrite below in the query, 
    # which may be quicker, but not sure if it's
    # worth it given its easier for me to do in pandas.
    data = data.pivot(columns='variable.name', values='value', index='geography.code')
    data.rename(columns={'GVA Current Prices £m': 'gva_current_prices'}, inplace=True)
    data.to_csv(os.path.join(SRC_DIR, 'themes/sustainable-growth/_data/gva_lad.csv'))