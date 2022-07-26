# Merge dei datasets

from numpy import broadcast
import pandas as pd
from os.path import dirname, abspath

PATH = dirname(dirname(abspath(__file__)))
PATH = PATH + f'/Merge_datasets_output/'
PATH = PATH.replace("\\", "/")

def mergeGeneralDataSets():
    general_booking_df = pd.read_excel(PATH + "general_data_dataset_booking.xlsx", index_col=0)
    general_tripadvisor_df = pd.read_excel(PATH + "general_data_dataset_tripadvisor.xlsx", index_col=0)
    
    general_df = pd.merge(general_booking_df, general_tripadvisor_df, on = 'name', how='outer')
    
    return general_df

def ReviewsBookingDataSets():
    
    reviews_booking_ds = pd.read_excel(PATH + "review_dataset_booking.xlsx", index_col=0)
    
#   reviews_booking_ds = reviews_booking_ds.drop(columns=["room_type"]) # rimuove la colonna room_type
    reviews_booking_ds["url"] = reviews_booking_ds["url"].apply(lambda x: (x.partition("hotel/")[2]) )
    reviews_booking_ds["url"] = reviews_booking_ds["url"].apply(lambda x: ((x.partition(".it.html")[0])) )
    reviews_booking_ds["url"] = reviews_booking_ds["url"].apply(lambda x: (x.replace("-", " ")))

    
    print(reviews_booking_ds.head())
    
#    reviews_ds = pd.merge(reviews_booking_ds, reviews_tripadvisor_ds, on = 'url', how='outer')
    return reviews_booking_ds

def ReviewsTripadvisorDatasets():
    reviews_tripadvisor_ds = pd.read_excel(PATH + "review_dataset_tripadvisor.xlsx", index_col=0)
    reviews_tripadvisor_ds["url"] = reviews_tripadvisor_ds["url"].apply(lambda x: (x.join([i for i in x if not i.isdigit()]))) 
#    reviews_tripadvisor_ds["url"] = reviews_tripadvisor_ds["url"].apply(lambda x: (x.partition("Reviews-or-")[2]) )
#    reviews_tripadvisor_ds["url"] = reviews_tripadvisor_ds["url"].apply(lambda x: ((x.partition("-")[0])) )
#    reviews_tripadvisor_ds["url"] = reviews_tripadvisor_ds["url"].apply(lambda x: (x.replace("_", " ")))

    print(reviews_tripadvisor_ds.head())

    return reviews_tripadvisor_ds


def main():

    camping_general_dataset = mergeGeneralDataSets()
    camping_general_dataset.to_excel(PATH + "General_data_merged.xlsx", header = True)

    camping_booking_reviews_dataset = ReviewsBookingDataSets()
    camping_tripadvisor_reviews_dataset = ReviewsTripadvisorDatasets()
    reviews_merged_df = pd.merge(camping_booking_reviews_dataset, camping_tripadvisor_reviews_dataset, on = 'url', how='outer')
    reviews_merged_df.to_excel(PATH + "Reviews_data_merged.xlsx", header = True)

main()