import pandas as pd
from os.path import dirname, abspath

PATH = dirname(dirname(abspath(__file__)))
PATH = PATH + f'/datasets/test_merge/'
PATH = PATH.replace("\\", "/")


def mergeBookingDataSets():

    availability_df = pd.read_excel(PATH + "availability_dataset_2022-09-17_2022-09-24_booking.xlsx", index_col=0)
    review_df = pd.read_excel(PATH + "review_dataset_booking.xlsx", index_col=0)
    general_df = pd.read_excel(PATH + "general_data_dataset_booking.xlsx", index_col=0)

    #df = pd.merge(review_df, general_df, on = 'id', how='left') # questo left join è ok, perdiamo qualche dato generale ma diciamo che è beh come dire... ridondante...
    df = pd.merge(availability_df, general_df, on = 'id', how='left') # anche questo è ok.
    
    # ma come vanno unite le recensioni ?


    return df

def main():

    booking_complete_dataset = mergeBookingDataSets()
    booking_complete_dataset.to_excel(PATH + "sas.xlsx", header = True)

main()