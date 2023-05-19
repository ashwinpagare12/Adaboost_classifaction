from flask import Flask,jsonify,request,render_template
from project_app.utils import Bankcurupt
# from sklearn import neighbors
import config

app=Flask(__name__)
@app.route("/")
def home():
    print("This is Banking domain")
    return render_template("home.html")

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == "POST":
        data=request.form
        print(data) 
        # Glucose= eval(data["Glucose"])
        ROAB_before_interest_and_depreciation_after_tax= eval(data['ROAB_before_interest_and_depreciation_after_tax'])
        Operating_Profit_Rate= eval(data['Operating_Profit_Rate'])
        Pre_tax_net_Interest_Rate= eval(data['Pre_tax_net_Interest_Rate'])
        Non_industry_income_and_expenditure_per_revenue= eval(data['Non_industry_income_and_expenditure_per_revenue'])
        Continuous_interest_rate_after_tax= eval(data['Continuous_interest_rate_after_tax'])
        Operating_Expense_Rate= eval(data['Operating_Expense_Rate'])
        Research_and_development_expense_rate= eval(data['Research_and_development_expense_rate'])
        Cash_flow_rate= eval(data['Cash_flow_rate'])
        Interest_bearing_debt_interest_rate= eval(data['Interest_bearing_debt_interest_rate'])
        Persistent_EPS_in_the_Last_Four_Seasons= eval(data['Persistent_EPS_in_the_Last_Four_Seasons'])
        Cash_Flow_Per_Share= eval(data['Cash_Flow_Per_Share'])
        Operating_Profit_Growth_Rate= eval(data['Operating_Profit_Growth_Rate'])
        After_tax_Net_Profit_Growth_Rate= eval(data['After_tax_Net_Profit_Growth_Rate'])
        Continuous_Net_Profit_Growth_Rate= eval(data['Continuous_Net_Profit_Growth_Rate'])
        Net_Value_Growth_Rate= eval(data['Net_Value_Growth_Rate'])
        Total_Asset_Return_Growth_Rate_Ratio= eval(data['Total_Asset_Return_Growth_Rate_Ratio'])
        Quick_Ratio= eval(data['Quick_Ratio'])
        Total_debt_per_Total_net_worth= eval(data['Total_debt_per_Total_net_worth'])
        Borrowing_dependency= eval(data['Borrowing_dependency'])
        Operating_profit_per_Paid_in_capital= eval(data['Operating_profit_per_Paid_in_capital'])
        Accounts_Receivable_Turnover= eval(data['Accounts_Receivable_Turnover'])
        Fixed_Assets_Turnover_Frequency= eval(data['Fixed_Assets_Turnover_Frequency'])
        Net_Worth_Turnover_Rate_times= eval(data['Net_Worth_Turnover_Rate_times'])
        Revenue_per_person= eval(data['Revenue_per_person'])
        Operating_profit_per_person= eval(data['Operating_profit_per_person'])
        Allocation_rate_per_person= eval(data['Allocation_rate_per_person'])
        Quick_Assets_per_Total_Assets= eval(data['Quick_Assets_per_Total_Assets'])
        Cash_per_Total_Assets= eval(data['Cash_per_Total_Assets'])
        Cash_per_Current_Liability= eval(data['Cash_per_Current_Liability'])
        Retained_Earnings_to_Total_Assets= eval(data['Retained_Earnings_to_Total_Assets'])
        Quick_Asset_Turnover_Rate= eval(data['Quick_Asset_Turnover_Rate'])
        Cash_Turnover_Rate= eval(data['Cash_Turnover_Rate'])
        Cash_Flow_to_Sales= eval(data['Cash_Flow_to_Sales'])
        Current_Liability_to_Liability= eval(data['Current_Liability_to_Liability'])
        Cash_Flow_to_Liability= eval(data['Cash_Flow_to_Liability'])
        Cash_Flow_to_Equity= eval(data['Cash_Flow_to_Equity'])
        Net_Income_to_Total_Assets= eval(data['Net_Income_to_Total_Assets'])
        Liability_to_Equity= eval(data['Liability_to_Equity'])
        Interest_Coverage_Ratio_Interest_expense_to_EBIT= eval(data['Interest_Coverage_Ratio_Interest_expense_to_EBIT'])

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

        result=obj.predict_bankcurupcy()
        print("Result is: ",result)
        return render_template("after.html", data=result)
        # return render_template("after.html", data=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)
