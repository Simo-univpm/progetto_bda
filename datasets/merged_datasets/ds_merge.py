import pandas as pd
from os.path import dirname, abspath

PATH = dirname(dirname(abspath(__file__)))
PATH = PATH + f'/datasets/'
PATH = PATH.replace("\\", "/")


def mergeBookingDataSets():

    availability_df = pd.read_excel(PATH + "availability_dataset_2022-09-17_2022-09-24_booking.xlsx", index_col=0)
    review_df = pd.read_excel(PATH + "review_dataset_booking.xlsx", index_col=0)
    general_df = pd.read_excel(PATH + "general_data_dataset_booking.xlsx", index_col=0)

    df = pd.merge(review_df, general_df, on = 'id', how='left')
    #df = pd.merge(availability_df, general_df, on = 'id', how='left')
    


    return df

def main():

    

    booking_complete_dataset = mergeBookingDataSets()
    booking_complete_dataset.to_excel(PATH + "sas_left.xlsx", header = True)

main()


reviews_booking_ds = reviews_booking_ds.apply(getIdFromUrl(reviews_booking_ds["url"]), axis=0, raw=False, result_type='broadcast')



reviews_booking_ds = reviews_booking_ds.apply(lambda x: )

df['x'] = df['x'].apply(lambda x: x * 2)

id = url.partition(".it.html")[0] # prende tutto quello prima di .it.html dall'url
id = id.partition("it/")[2] # prende tutto quello dopo di it/ dall'url