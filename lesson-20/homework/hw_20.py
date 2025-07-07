import pandas as pd
from sqlalchemy import create_engine,inspect
engine = create_engine('sqlite:///chinook.db')
inspector = inspect(engine)
print(inspector.get_table_names())
#Homework1
df_invoice = pd.read_sql("SELECT * FROM Invoice", con=engine)
df_customers = pd.read_sql("SELECT * FROM Customer", con=engine)
df_total = df_invoice.groupby('CustomerId')[['Total']].sum().merge(df_customers,on=['CustomerId'],how='inner')[['CustomerId','FirstName','LastName','Total']]
df_total_top5 = df_total.sort_values(by='Total',ascending=False).head(5)
print(df_total_top5)
#Homework2
df_invoice_line  = pd.read_sql('select * from InvoiceLine',con=engine)
df_track  = pd.read_sql('select * from Track',con=engine)
df_album  = pd.read_sql('select * from Album',con=engine)
invoice_with_album = df_invoice_line.merge(df_track[['TrackId','AlbumId']],on='TrackId',how='left').merge(df_invoice[['InvoiceId','CustomerId']], on = 'InvoiceId',how='left')
album_track_counts = df_track.groupby('AlbumId').size().reset_index(name='TotalTracks')
customer_album_purchases = invoice_with_album.groupby(['CustomerId','AlbumId'])['TrackId'].nunique().reset_index()
customer_album_purchases.rename(columns={'TrackId': 'TracksPurchased'}, inplace=True)
customer_album_purchases = customer_album_purchases.merge(album_track_counts, on='AlbumId')
customer_album_purchases['FullAlbumPurchased'] = customer_album_purchases['TracksPurchased'] == customer_album_purchases['TotalTracks']
customer_album_summary =customer_album_purchases.groupby('CustomerId')['FullAlbumPurchased'].any().reset_index()
customer_album_summary['PurchaseType'] = customer_album_summary['FullAlbumPurchased'].apply(lambda x:'Full Album' if x else 'Individual Tracks')
summary = round(customer_album_summary['PurchaseType'].value_counts(normalize=True)*100,2).reset_index(name='Percentage')
print(summary)
