import xlwings as xw
import pandas as pd


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets["Python"]
    
    df = sheet.range('A1').expand().options(pd.DataFrame, index=False).value
    sheet.range("O:X").api.delete()
    
    sheet["O2"].options(pd.DataFrame, header=1, index=True, expand='table').value = df.describe()

    sheet["O21"].options(pd.DataFrame, header=1, index=True, expand='table').value = df.head()

if __name__ == "__main__":
    xw.Book("lab1_part3_alphabet_eshita_kavana.xlsm").set_mock_caller()
    main()
