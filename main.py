import streamlit as st
import numpy as np
from itertools import product

st.title("Under Construction!")
st.title("Coffee Market Optimizer")
st.write("---")

#initialize values
amount_gcb = 0
amount_fc = 0
hauling = 0
floating = 0
depulping = 0
drying = 0
dehulling = 0
sorting = 0
storage = 0
pruning = 0
fertilizing = 0
spraying = 0
harvesting = 0
rejuvenation = 0
weeding = 0

coffee_trees = st.number_input(label="How many coffee trees are there in your farm?", min_value=1, step=1)
coffee_variety = st.radio("Select the variety of your Coffee:",
                          ("Robusta", "Arabica", "Excelsa"))
coffee_type = st.radio("Select the type of Coffee you will sell:",
                       ("Fresh", "Green Coffee Beans", "Both"))
amount_fc = st.number_input(label="Enter the total amount of fresh coffee cherries you have harvested (in kilos)", min_value=0.00, step=0.05)
if coffee_type == "Green Coffee Beans" or coffee_type == "Both":
    amount_gcb = st.number_input(label="Enter the amount of coffee cherries you have successfully converted to Green Coffee Beans (in kilos)", min_value=0.00, step=0.05)

if coffee_variety == "Robusta":
    m_hauling = 2.5
    m_floating = 0.4167
    m_depulping = 4.8
    m_drying = 3.125
    m_dehulling = 2.7
    m_sorting = 2
    m_storage = 0

    m_pruning = 1.25
    m_fertilizing = 0.75
    m_spraying = 0.6
    m_weeding = 2
    m_harvesting = 2
    m_rejuvenation = 0.225

    m_transport = 1 

elif coffee_variety == "Arabica":
    m_hauling = 1.5
    m_floating = 0
    m_depulping = 2.1667
    m_drying = 4.3016
    m_dehulling = 2.5
    m_sorting = 2.7083
    m_storage = 0

    m_pruning = 1.5
    m_fertilizing = 0.7143
    m_spraying = 0.8356
    m_weeding = 1.6667
    m_harvesting = 3.4857
    m_rejuvenation = 0.55

    m_transport = 1.5

elif coffee_variety == "Excelsa":

    m_hauling = 1.6
    m_floating = 0
    m_depulping = 3.2078
    m_drying = 4.1833
    m_dehulling = 4
    m_sorting = 3.3333
    m_storage = 0

    m_pruning = 1.3423
    m_fertilizing = 2.52
    m_spraying = 1.5
    m_weeding = 3
    m_harvesting = 7.05
    m_rejuvenation = 0.75

    m_transport = 1.8182 

st.header("Input Costs:")
fertilizer1 = st.number_input(label="Enter the cost of Fertilizer 1 per kilogram: ", min_value=0.00, step=0.05)
fertilizer1qty = st.number_input(label="Enter the number of kilos of Fertilizer 1 used: ", min_value=0.00, step=0.05)
fertilizer2 = st.number_input(label="Enter the cost of Fertilizer 2 per kilogram: ", min_value=0.00, step=0.05)
fertilizer2qty = st.number_input(label="Enter the number of kilos of Fertilizer 2 used: ", min_value=0.00, step=0.05)
organic_fertilizer = st.number_input(label="Enter the cost of Organic Fertilizer per kilogram: ", min_value=0.00, step=0.05)
organic_fertilizer_qty = st.number_input(label="Enter the number of kilos of Organic Fertilizer used: ", min_value=0.00, step=0.05)
herbicide = st.number_input(label="Enter the cost of Herbicide per kilogram: ", min_value=0.00, step=0.05)
herbicide_qty = st.number_input(label="Enter the number of kilos of Herbicide used: ", min_value=0.00, step=0.05)
pesticide = st.number_input(label="Enter the cost of Pesticide per kilogram: ", min_value=0.00, step=0.05)
pesticide_qty = st.number_input(label="Enter the number of kilos of Pesticide used: ", min_value=0.00, step=0.05)

st.header("Labor Costs:")
pruning = st.radio("Did you incur any labor costs for Pruning?:", ("Yes", "No"))
pruning = 1 if pruning == "Yes" else 0
fertilizing = st.radio("Did you incur any labor costs for Fertilizing?:", ("Yes", "No"))
fertilizing = 1 if fertilizing == "Yes" else 0
spraying = st.radio("Did you incur any labor costs for Spraying?:", ("Yes", "No"))
spraying = 1 if spraying == "Yes" else 0
harvesting = st.radio("Did you incur any labor costs for Harvesting?:", ("Yes", "No"))
harvesting = 1 if harvesting == "Yes" else 0
rejuvenation = st.radio("Did you incur any labor costs for Rejuvenation?:", ("Yes", "No"))
rejuvenation = 1 if rejuvenation == "Yes" else 0
weeding = st.radio("Did you incur any labor costs for Weeding?:", ("Yes", "No"))
weeding = 1 if weeding == "Yes" else 0

if coffee_type == "Green Coffee Beans" or coffee_type == "Both":
    st.header("Post Production Cost:")
    hauling = st.radio("Did you incur any labor costs for Hauling?:", ("Yes", "No"))
    hauling = 1 if hauling == "Yes" else 0
    floating = st.radio("Did you incur any labor costs for Floating?:", ("Yes", "No"))
    floating = 1 if floating == "Yes" else 0
    depulping = st.radio("Did you incur any labor costs for Deulping?:", ("Yes", "No"))
    depulping = 1 if depulping == "Yes" else 0
    drying = st.radio("Did you incur any labor costs for Drying?:", ("Yes", "No"))
    drying = 1 if drying == "Yes" else 0
    dehulling = st.radio("Did you incur any labor costs for Dehulling?:", ("Yes", "No"))
    dehulling = 1 if dehulling == "Yes" else 0
    sorting = st.radio("Did you incur any labor costs for Sorting?:", ("Yes", "No"))
    sorting = 1 if sorting == "Yes" else 0
    storage = st.radio("Did you incur any labor costs for Storage?:", ("Yes", "No"))
    storage = 1 if storage == "Yes" else 0

st.header("Other Costs:")
transport = st.radio("Did you incur any labor costs for Transportation?:", ("Yes", "No"))
transport = 1 if transport == "Yes" else 0
other_cost = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)


def calculate():
    input_cost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organic_fertilizer * organic_fertilizer_qty +
        herbicide * herbicide_qty +
        pesticide * pesticide_qty
    )
    m_labor_cost = (
        (m_pruning * pruning + m_fertilizing * fertilizing +
         m_spraying * spraying + m_weeding * weeding +
         m_harvesting * harvesting + m_rejuvenation * rejuvenation) * coffee_trees
    )
    m_postproduction_cost = (
        (m_hauling * hauling + m_floating * floating +
         m_depulping * depulping + m_drying * drying +
         m_dehulling * dehulling + m_sorting * sorting +
         m_storage * storage) * amount_gcb
    )
    total_m_bound_cost = (
        input_cost + m_labor_cost + m_labor_cost + other_cost + (m_transport * transport * amount_fc)
    )
    trader_fc_profit = (
        (traders_allocation / 100 * amount_fresh) * trader_fc_price
    )
    other_markets_fc_profit = (
        (other_markets_allocation / 100 * amount_fresh) * other_markets_fc_price
    )
    total_profit = (
        (trader_fc_profit + other_markets_fc_profit) - (total_cost)
    )
    return input_cost, m_labor_cost, m_postproduction_cost, total_m_bound_cost


def calculate_profit(traders_allocation, other_markets_allocation):
    total_input_cost = (
        fertilizer1_cost * fertilizer1_kilo + fertilizer2_cost * fertilizer2_kilo +
        organic_cost * organic_kilo + herbicides_cost * herbicides_kilo +
        pesticide_cost * pesticide_kilo
    )
    total_labor_cost = (
        (m_pruning * pruning_cost + m_fertilizing * fertilizing_cost +
         m_spraying * spraying_cost + m_weeding * weeding_cost +
         m_harvesting * harvesting_cost + m_rejuvenation * rejuvenation_cost) * number_of_trees
    )
    total_cost = total_input_cost + total_labor_cost + other_cost

    # Calculate profits from selling fresh coffee cherries to local traders and other markets
    trader_fc_profit = (traders_allocation * amount_fresh) * trader_fc_price
    other_markets_fc_profit = (other_markets_allocation * amount_fresh) * other_markets_fc_price

    # Calculate total profit
    total_profit = (trader_fc_profit + other_markets_fc_profit) - (total_cost)

    return total_profit


def optimize_market_allocations():
    variables = ['traders_allocation', 'other_markets_allocation']
    values = np.linspace(0, 1, num=21)  # num=11 (0.1), num=101 (0.01), num=21 (0.05)

    # Define a generator function to generate possible combinations of market allocation with intervals
    def market_allocation_generator():
        # Generates all possible combinations of the elements in the values variable
        for combo in product(values, repeat=len(variables)):
            # Assign values to the markets by pairing the markets to the combination of values generated
            allocation = dict(zip(variables, combo))
            # Restriction to ensure market allocation is equal to 1
            if sum(allocation.values()) == 1:
                yield allocation

    # Create a list for the market allocations
    market_allocations = list(market_allocation_generator())
    num_allocations = len(market_allocations)
    profits = np.zeros(num_allocations)

    max_profit = 0  # Initialize maximum profit
    max_profit_case = market_allocations[0]  # Initialize with the first allocation
    max_profit_value = calculate_profit(**max_profit_case)

    # Calculate profits for each market allocation
    for i, case in enumerate(market_allocations):
        profits[i] = calculate_profit(**case)
        if profits[i] > max_profit_value:
            max_profit_value = profits[i]
            max_profit_case = case

    # Print overall maximum profit
    print("\nOverall Maximum Profit:")
    print(f"Market Allocation: {max_profit_case}")
    print(f"Maximum Profit: {max_profit_value}")


if st.button("Optimize"):
    optimize_market_allocations()


