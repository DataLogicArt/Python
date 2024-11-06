print("**********************************************"
      "\n Menu" +
      "\n1. Compare Stocks" +
      "\n2.Qiut")

num1 = input("Please enter your Selection: ")
while float(num1) < 2:
    num2 = input("Enter the first stock ")
    num3 = input("Enter the second stock ")
    num4 = input("Enter the total previous days for the analysis: ")
    print("Please wait a few seconds for this request to complete")

    import pandas_datareader as pdr
    import datetime
    import pandas as pd

    # Allow the full width of the data frame to show.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)


    def getStock(stk):
        # Set and show dates.
        dt = datetime.date.today()
        dtPast = dt + datetime.timedelta(days=-int(num4))
        # print(dt)
        print(dtPast)
        print("Statistics from " + str(dtPast) + " to " + str(dt))

        # Call Yahoo finance to get stock data for the stock provided.
        df = pdr.get_data_yahoo(stk,
                                start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                                end=datetime.datetime(dt.year, dt.month, dt.day))

        # Return a dataframe containing stock data to the calling instruction.
        return df


    dfApple = getStock(num2)
    dfDOW = getStock(num3)


    numRows = len(dfApple)

    Open = (dfApple.iloc[0]['Close'])
    Close = (dfApple.iloc[numRows - 1]['Close'])
    PerChange = (Close - Open) / Open * 100
    STD = dfApple['Close'].std()
    MeanPrice = dfApple['Close'].mean()

    Open2 = (dfDOW.iloc[0]['Close'])
    Close2 = (dfDOW.iloc[numRows - 1]['Close'])
    PerChange2 = (Close2 - Open2) / Open2 * 100
    STD2 = dfDOW['Close'].std()
    MeanPrice2 = dfDOW['Close'].mean()

    dfApple = pd.DataFrame(
        columns=["Stock Name", "Start Price", "End Price", "Mean Price", "ST. Deviation", "Percent Change"])
    fullNameDictionary1 = ({"Stock Name": str(num2), "Start Price": str(Open), "End Price": str(Close),'Mean Price': str(MeanPrice), "ST. Deviation": str(STD), "Percent Change": str(PerChange)})
    fullNameDictionary2 = ({"Stock Name": str(num3), "Start Price": str(Open2), "End Price": str(Close2),'Mean Price': str(MeanPrice2), "ST. Deviation": str(STD2),
                            "Percent Change": str(PerChange2)})
    dfApple = dfApple.append(fullNameDictionary1, ignore_index=True)
    dfApple = dfApple.append(fullNameDictionary2, ignore_index=True)

    print(dfApple)
    print("**********************************************"
          "\n Menu" +
          "\n1. Compare Stocks" +
          "\n2.Qiut")
    num1 = input("Please enter your Selection: ")
print("Thank you! Please come again :) ")