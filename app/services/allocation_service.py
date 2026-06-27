def calculate_allocation_percentage(holding_value:float,total_portfolio_value:float):

    if total_portfolio_value==0:
        return 0
    
    return round(
        (holding_value/total_portfolio_value) *100,2
    )


def find_top_holding(holdings:float):

    if not holdings:
        return None

    return max(
        holdings,
        key=lambda x : x["current_value"]  #holdings = [{"stock": "TCS","current_value": 50000},...]
    )