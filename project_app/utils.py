import numpy as np
import pandas as pd
import pickle
import json
# import os
import config

class Bankcurupt():
    def __init__(self,ROAB_before_interest_and_depreciation_after_tax,Operating_Profit_Rate, Pre_tax_net_Interest_Rate,
                Non_industry_income_and_expenditure_per_revenue,Continuous_interest_rate_after_tax, Operating_Expense_Rate,
                Research_and_development_expense_rate, Cash_flow_rate,Interest_bearing_debt_interest_rate,
                Persistent_EPS_in_the_Last_Four_Seasons, Cash_Flow_Per_Share,Operating_Profit_Growth_Rate, After_tax_Net_Profit_Growth_Rate,
                Continuous_Net_Profit_Growth_Rate, Net_Value_Growth_Rate,Total_Asset_Return_Growth_Rate_Ratio, Quick_Ratio,
                Total_debt_per_Total_net_worth, Borrowing_dependency,Operating_profit_per_Paid_in_capital, Accounts_Receivable_Turnover,
                Fixed_Assets_Turnover_Frequency, Net_Worth_Turnover_Rate_times,Revenue_per_person, Operating_profit_per_person,
                Allocation_rate_per_person, Quick_Assets_per_Total_Assets,Cash_per_Total_Assets, Cash_per_Current_Liability,
                Retained_Earnings_to_Total_Assets, Quick_Asset_Turnover_Rate,Cash_Turnover_Rate, Cash_Flow_to_Sales,
                Current_Liability_to_Liability, Cash_Flow_to_Liability,Cash_Flow_to_Equity, Net_Income_to_Total_Assets,
                Liability_to_Equity,Interest_Coverage_Ratio_Interest_expense_to_EBIT):
        self.ROAB_before_interest_and_depreciation_after_tax=ROAB_before_interest_and_depreciation_after_tax
        self.Operating_Profit_Rate=Operating_Profit_Rate
        self.Pre_tax_net_Interest_Rate=Pre_tax_net_Interest_Rate
        self.Non_industry_income_and_expenditure_per_revenue=Non_industry_income_and_expenditure_per_revenue
        self.Continuous_interest_rate_after_tax=Continuous_interest_rate_after_tax
        self.Operating_Expense_Rate=Operating_Expense_Rate
        self.Research_and_development_expense_rate=Research_and_development_expense_rate
        self.Cash_flow_rate=Cash_flow_rate
        self.Interest_bearing_debt_interest_rate=Interest_bearing_debt_interest_rate
        self.Persistent_EPS_in_the_Last_Four_Seasons=Persistent_EPS_in_the_Last_Four_Seasons
        self.Cash_Flow_Per_Share=Cash_Flow_Per_Share
        self.Operating_Profit_Growth_Rate=Operating_Profit_Growth_Rate
        self.After_tax_Net_Profit_Growth_Rate=After_tax_Net_Profit_Growth_Rate
        self.Continuous_Net_Profit_Growth_Rate=Continuous_Net_Profit_Growth_Rate
        self.Net_Value_Growth_Rate=Net_Value_Growth_Rate
        self.Total_Asset_Return_Growth_Rate_Ratio=Total_Asset_Return_Growth_Rate_Ratio
        self.Quick_Ratio=Quick_Ratio
        self.Total_debt_per_Total_net_worth=Total_debt_per_Total_net_worth
        self.Borrowing_dependency=Borrowing_dependency
        self.Operating_profit_per_Paid_in_capital=Operating_profit_per_Paid_in_capital
        self.Accounts_Receivable_Turnover=Accounts_Receivable_Turnover
        self.Fixed_Assets_Turnover_Frequency=Fixed_Assets_Turnover_Frequency
        self.Net_Worth_Turnover_Rate_times=Net_Worth_Turnover_Rate_times
        self.Revenue_per_person=Revenue_per_person
        self.Operating_profit_per_person=Operating_profit_per_person
        self.Allocation_rate_per_person=Allocation_rate_per_person
        self.Quick_Assets_per_Total_Assets=Quick_Assets_per_Total_Assets
        self.Cash_per_Total_Assets=Cash_per_Total_Assets
        self.Cash_per_Current_Liability=Cash_per_Current_Liability
        self.Retained_Earnings_to_Total_Assets=Retained_Earnings_to_Total_Assets
        self.Quick_Asset_Turnover_Rate=Quick_Asset_Turnover_Rate
        self.Cash_Turnover_Rate=Cash_Turnover_Rate
        self.Cash_Flow_to_Sales=Cash_Flow_to_Sales
        self.Current_Liability_to_Liability=Current_Liability_to_Liability
        self.Cash_Flow_to_Liability=Cash_Flow_to_Liability
        self.Cash_Flow_to_Equity=Cash_Flow_to_Equity
        self.Net_Income_to_Total_Assets=Net_Income_to_Total_Assets
        self.Liability_to_Equity=Liability_to_Equity
        self.Interest_Coverage_Ratio_Interest_expense_to_EBIT=Interest_Coverage_Ratio_Interest_expense_to_EBIT

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.My_model=pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def predict_bankcurupcy(self):
        self.load_model()
        test_array=np.zeros(len(self.json_data["columns"])) 
        test_array[0]=self.ROAB_before_interest_and_depreciation_after_tax
        test_array[1]=self.Operating_Profit_Rate
        test_array[2]=self.Pre_tax_net_Interest_Rate
        test_array[3]=self.Non_industry_income_and_expenditure_per_revenue
        test_array[4]=self.Continuous_interest_rate_after_tax
        test_array[5]=self.Operating_Expense_Rate
        test_array[6]=self.Research_and_development_expense_rate
        test_array[7]=self.Cash_flow_rate
        test_array[8]=self.Interest_bearing_debt_interest_rate
        test_array[9]=self.Persistent_EPS_in_the_Last_Four_Seasons
        test_array[10]=self.Cash_Flow_Per_Share
        test_array[11]=self.Operating_Profit_Growth_Rate
        test_array[12]=self.After_tax_Net_Profit_Growth_Rate
        test_array[13]=self.Continuous_Net_Profit_Growth_Rate
        test_array[14]=self.Net_Value_Growth_Rate
        test_array[15]=self.Total_Asset_Return_Growth_Rate_Ratio
        test_array[16]=self.Quick_Ratio
        test_array[17]=self.Total_debt_per_Total_net_worth
        test_array[18]=self.Borrowing_dependency
        test_array[19]=self.Operating_profit_per_Paid_in_capital
        test_array[20]=self.Accounts_Receivable_Turnover
        test_array[21]=self.Fixed_Assets_Turnover_Frequency
        test_array[22]=self.Net_Worth_Turnover_Rate_times
        test_array[23]=self.Revenue_per_person
        test_array[24]=self.Operating_profit_per_person
        test_array[25]=self.Allocation_rate_per_person
        test_array[26]=self.Quick_Assets_per_Total_Assets
        test_array[27]=self.Cash_per_Total_Assets
        test_array[28]=self.Cash_per_Current_Liability
        test_array[29]=self.Retained_Earnings_to_Total_Assets
        test_array[30]=self.Quick_Asset_Turnover_Rate
        test_array[31]=self.Cash_Turnover_Rate
        test_array[32]=self.Cash_Flow_to_Sales
        test_array[33]=self.Current_Liability_to_Liability
        test_array[34]=self.Cash_Flow_to_Liability
        test_array[35]=self.Cash_Flow_to_Equity
        test_array[36]=self.Net_Income_to_Total_Assets
        test_array[37]=self.Liability_to_Equity
        test_array[38]=self.Interest_Coverage_Ratio_Interest_expense_to_EBIT
        # test_array = test_array.reshape(-1,1)
        print("test_array is: ",test_array)


        prediction=self.My_model.predict([test_array])[0]
        return prediction
if __name__=="__main__":
    ROAB_before_interest_and_depreciation_after_tax=0.40574977247176
    Operating_Profit_Rate=0.998969203197885
    Pre_tax_net_Interest_Rate=0.796887145860514
    Non_industry_income_and_expenditure_per_revenue=0.302646433889668
    Continuous_interest_rate_after_tax=0.780984850207341
    Operating_Expense_Rate=0.0001256968688759
    Research_and_development_expense_rate=0.0
    Cash_flow_rate=0.458143143520965
    Interest_bearing_debt_interest_rate=0.0007250725072507
    Persistent_EPS_in_the_Last_Four_Seasons=0.16914058806845
    Cash_Flow_Per_Share=0.311664426681757
    Operating_Profit_Growth_Rate=0.848194994526472
    After_tax_Net_Profit_Growth_Rate=0.688979462807371
    Continuous_Net_Profit_Growth_Rate=0.217535386199635
    Net_Value_Growth_Rate=0.000326977269203
    Total_Asset_Return_Growth_Rate_Ratio=0.263099983681843
    Quick_Ratio=0.0012077550852353
    Total_debt_per_Total_net_worth=0.0212659243655332
    Borrowing_dependency=0.390284354359258
    Operating_profit_per_Paid_in_capital=0.0958848339765825
    Accounts_Receivable_Turnover=0.0018138841264849
    Fixed_Assets_Turnover_Frequency=0.0001165006532358
    Net_Worth_Turnover_Rate_times=0.0329032258064516
    Revenue_per_person=0.0341641819543792
    Operating_profit_per_person=0.392912869451166
    Allocation_rate_per_person=0.0371353015800987
    Quick_Assets_per_Total_Assets=0.166672958825266
    Cash_per_Total_Assets=0.004094405952288
    Cash_per_Current_Liability=0.0001473360247605
    Retained_Earnings_to_Total_Assets=0.903224771166726
    Quick_Asset_Turnover_Rate=6550000000.0
    Cash_Turnover_Rate=458000000.0
    Cash_Flow_to_Sales=0.6715676535815
    Current_Liability_to_Liability=0.676269176153092
    Cash_Flow_to_Liability=0.458609147666847
    Cash_Flow_to_Equity=0.312904948119326
    Net_Income_to_Total_Assets=0.716845343217827
    Liability_to_Equity=0.29020189277926
    Interest_Coverage_Ratio_Interest_expense_to_EBIT=0.564050112276341


    obj=Bankcurupt(ROAB_before_interest_and_depreciation_after_tax,Operating_Profit_Rate, Pre_tax_net_Interest_Rate,
        Non_industry_income_and_expenditure_per_revenue,Continuous_interest_rate_after_tax, Operating_Expense_Rate,
        Research_and_development_expense_rate, Cash_flow_rate,Interest_bearing_debt_interest_rate,
        Persistent_EPS_in_the_Last_Four_Seasons, Cash_Flow_Per_Share,Operating_Profit_Growth_Rate, After_tax_Net_Profit_Growth_Rate,
        Continuous_Net_Profit_Growth_Rate, Net_Value_Growth_Rate,Total_Asset_Return_Growth_Rate_Ratio, Quick_Ratio,
        Total_debt_per_Total_net_worth, Borrowing_dependency,Operating_profit_per_Paid_in_capital, Accounts_Receivable_Turnover,
        Fixed_Assets_Turnover_Frequency, Net_Worth_Turnover_Rate_times,Revenue_per_person, Operating_profit_per_person,
        Allocation_rate_per_person, Quick_Assets_per_Total_Assets,Cash_per_Total_Assets, Cash_per_Current_Liability,
        Retained_Earnings_to_Total_Assets, Quick_Asset_Turnover_Rate,Cash_Turnover_Rate, Cash_Flow_to_Sales,
        Current_Liability_to_Liability, Cash_Flow_to_Liability,Cash_Flow_to_Equity, Net_Income_to_Total_Assets,
        Liability_to_Equity,Interest_Coverage_Ratio_Interest_expense_to_EBIT)
    obj.predict_bankcurupcy()
                 