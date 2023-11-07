import streamlit as st
import numpy as np
from itertools import product
import base64


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("coffee1.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover; /* This will cover the entire container without stretching */
    background-position: center center; /* Center the image horizontally and vertically */
    background-repeat: no-repeat; /* Prevent image from repeating */
    height: 100vh; /* Set the height to 100% of the viewport height (full height) */
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


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
transport = 0
fertilizing = 0
spraying = 0
harvesting = 0
rejuvenation = 0
weeding = 0
max_profit = 0
percent_othermarkets = 0
percent_bigcompaniesgcb = 0
percent_coopgcb = 0
percent_othermarketsgcb = 0
percent_traders = 0
percent_tradersgcb = 0
price_coopgcb = 0
price_bigcompaniesgcb = 0
price_othermarkets = 0
price_othermarketsgcb = 0
price_tradersgcb = 0
price_traders = 0
coop_gcb_profit = 0
trader_fc_profit = 0
traders_gcb_profit = 0
other_markets_fc_profit = 0
big_companies_gcb_profit = 0
other_markets_gcb_profit = 0

coffee_trees = st.number_input(label="How many coffee trees are there in your farm?", min_value=0.00, step=100.00)
coffee_variety = st.radio("Select the variety of your Coffee:",
                          ("Robusta", "Arabica", "Excelsa"))
coffee_type = st.radio("Select the type of Coffee you will sell:",
                       ("Fresh", "Green Coffee Beans", "Both"))
if coffee_type == "Green Coffee Beans":
    st.header("Selling Green Coffee Beans:")
    amount_fc = 0
    amount_gcb = st.number_input(label="Enter the amount of Green Coffee Beans you will sell (in kilos)", min_value=0.00, step=5.00)
    st.subheader("Big companies (e.g. Nestle)")
    sellto_bigcompaniesgcb = st.radio("Will you sell to Big Companies (e.g. Nestle)?",
                              ("Yes", "No"))
    if sellto_bigcompaniesgcb == "Yes":
        percent_bigcompaniesgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Big Companies in kilograms (kg)", min_value=0.00, max_value=100.00, step=10.00)
        price_bigcompaniesgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Big Companies in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_bigcompaniesgcb == "No":
        percent_bigcompaniesgcb = 0
        price_bigcompaniesgcb = 0
    
    st.subheader("Traders")
    sellto_tradersgcb = st.radio("Will you sell to Traders?",
                              ("Yes", "No"))
    if sellto_tradersgcb == "Yes":
        percent_tradersgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Traders in kilograms (kg)", min_value=0.00, max_value=100.00 - percent_bigcompaniesgcb, step=10.00)
        price_tradersgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Traders in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_tradersgcb == "No":
        percent_tradersgcb = 0
        price_tradersgcb = 0

    max_remaining_percentage = 100 - (percent_bigcompaniesgcb + percent_tradersgcb)

    st.subheader("Other Markets (e.g. Supermarkets, Coffee Shops, etc.)")
    sellto_othermarketsgcb = st.radio("Will you sell to Other Markets (e.g. Supermarkets, Coffee Shops, etc.)?",
                              ("Yes", "No"))
    if sellto_othermarketsgcb == "Yes":
        percent_othermarketsgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Other Markets in kilograms (kg)", min_value=0.00, max_value=max_remaining_percentage, step=10.00)
        price_othermarketsgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Other Markets in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_othermarketsgcb == "No":
        percent_othermarketsgcb = 0
        price_othermarketsgcb = 0

    max_remaining_percentage -= percent_othermarketsgcb

    st.subheader("Cooperatives")
    sellto_coopgcb = st.radio("Will you sell to a Cooperative?",
                              ("Yes", "No"))
    if sellto_coopgcb == "Yes":
        percent_coopgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to the Cooperative in kilograms (kg)", min_value=0.00, max_value=max_remaining_percentage, step=10.00)
        price_coopgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to the Cooperative in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_coopgcb == "No":
        percent_coopgcb = 0
        price_coopgcb = 0
    st.subheader("Type of Allocation")
    type_of_allocation = st.radio("Should all markets have an allocation?:",
                            ("No", "Yes"))
if coffee_type == "Both":
    amount_fc = st.number_input(label="Enter the total amount of fresh coffee cherries you will sell (in kilos)", min_value=0.00, step=0.5)
    amount_gcb = st.number_input(label="Enter the amount of Green Coffee Beans you will sell (in kilos)", min_value=0.00, step=0.5)
    st.header("Selling Fresh Cherries:")
    st.subheader("Traders")
    sellto_traders = st.radio("Will you sell fresh cherries to Traders?",
                              ("Yes", "No"))
    if sellto_traders == "Yes":
        percent_traders = st.number_input(label="Enter the percentage of Fresh Coffee Cherries to be allocated to Traders in kilograms (kg)", min_value=0.00, max_value=100.00, step=10.00)
        price_traders = st.number_input(label="Enter the price of Fresh Coffee Cherries when sold to Traders in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_traders == "No":
        percent_traders = 0
        price_traders = 0
    st.subheader("Other Markets (e.g. Supermarkets, Coffee Shops)")
    sellto_othermarkets = st.radio("Will you sell fresh cherries to Other Markets (e.g. Supermarkets, Coffee Shops) ?",
                              ("Yes", "No"))
    if sellto_othermarkets == "Yes":
        percent_othermarkets = st.number_input(label="Enter the percentage of Fresh Coffee Cherries to be allocated to Other Markets in kilograms (kg)", min_value=0.00, max_value=100.00-percent_traders, step=10.00)
        price_othermarkets = st.number_input(label="Enter the price of Fresh Coffee Cherries when sold to Other Markets in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_othermarkets == "No":
        percent_othermarkets = 0
        price_othermarkets = 0
    st.header("Selling Green Coffee Beans:")
    st.subheader("Big companies (e.g. Nestle, etc.)")
    sellto_bigcompaniesgcb = st.radio("Will you sell to Big Companies (e.g. Nestle, etc.)?",
                              ("Yes", "No"))
    if sellto_bigcompaniesgcb == "Yes":
        percent_bigcompaniesgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Big Companies in kilograms (kg)", min_value=0.00, max_value=100.00, step=10.00)
        price_bigcompaniesgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Big Companies in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_bigcompaniesgcb == "No":
        percent_bigcompaniesgcb = 0
        price_bigcompaniesgcb = 0
    st.subheader("Traders")
    sellto_tradersgcb = st.radio("Will you sell to Traders?",
                              ("Yes", "No"))
    if sellto_tradersgcb == "Yes":
        percent_tradersgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Traders in kilograms (kg)", min_value=0.00, max_value=100.00 - percent_bigcompaniesgcb, step=10.00)
        price_tradersgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Traders in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_tradersgcb == "No":
        percent_tradersgcb = 0
        price_tradersgcb = 0

    max_remaining_percentage = 100.00 - (percent_bigcompaniesgcb + percent_tradersgcb)
    st.subheader("Other Markets (e.g. Supermarkets, Coffee Shops, etc.)")
    sellto_othermarketsgcb = st.radio("Will you sell to Other Markets (e.g. Supermarkets, Coffee Shops, etc.)?",
                              ("Yes", "No"))
    if sellto_othermarketsgcb == "Yes":
        percent_othermarketsgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to Other Markets in kilograms (kg)", min_value=0.00, max_value=max_remaining_percentage, step=10.00)
        price_othermarketsgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to Other Markets in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_othermarketsgcb == "No":
        percent_othermarketsgcb = 0
        price_othermarketsgcb = 0

    max_remaining_percentage -= percent_othermarketsgcb
    st.subheader("Cooperative")
    sellto_coopgcb = st.radio("Will you sell to a Cooperative?",
                              ("Yes", "No"))
    if sellto_coopgcb == "Yes":
        percent_coopgcb = st.number_input(label="Enter the percentage of Green Coffee Beans to be allocated to the Cooperative in kilograms (kg)", min_value=0.00, max_value=max_remaining_percentage, step=10.00)
        price_coopgcb = st.number_input(label="Enter the price of Green Coffee Beans when sold to the Cooperative in pesos (php)", min_value=0.00, step=10.00)
    elif sellto_coopgcb == "No":
        percent_coopgcb = 0
        price_coopgcb = 0
    type_of_allocation =  "Yes"
if coffee_type == "Fresh":
    st.header("Selling Fresh Cherries:")
    amount_fc = st.number_input(label="Enter the total amount of fresh coffee cherries you will sell (in kilos)", min_value=0.00, step=0.5)
    amount_gcb = 0
    st.subheader("Traders")
    sellto_traders = st.radio("Will you sell to Traders?",
                              ("Yes", "No"))
    if sellto_traders == "Yes":
        percent_traders = st.number_input(label="Enter the percentage of Fresh Coffee Cherries to be allocated to Traders in kilograms (kg)", min_value=0.00, max_value=100.00, step=10.00)
        price_traders = st.number_input(label="Enter the price of Fresh Coffee Cherries when sold to Traders in pesos (php)", min_value=0.00, step=1.00)
    elif sellto_traders == "No":
        percent_traders = 0
        price_traders = 0
    st.subheader("Other Markets (e.g. Supermarkets, Coffee Shops, etc.)")
    sellto_othermarkets = st.radio("Will you sell to Other Markets (e.g. Supermarkets, Coffee Shops, etc.)?",
                              ("Yes", "No"))
    if sellto_othermarkets == "Yes":
        percent_othermarkets = st.number_input(label="Enter the percentage of Fresh Coffee Cherries to be allocated to Other Markets in kilograms (kg)", min_value=0.00, max_value=100.00-percent_traders, step=10.00)
        price_othermarkets = st.number_input(label="Enter the price of Fresh Coffee Cherries when sold to Other Markets in pesos (php)", min_value=0, step=1)
    elif sellto_othermarkets == "No":
        percent_othermarkets = 0
        price_othermarkets = 0
    st.subheader("Type of Allocation")
    type_of_allocation = st.radio("Should all markets have an allocation?:",
                            ("No", "Yes"))

amount_coffee = amount_gcb + amount_fc
total_percentfc = percent_traders + percent_othermarkets
total_percentgc = percent_bigcompaniesgcb + percent_tradersgcb + percent_othermarketsgcb + percent_coopgcb

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
st.subheader(f"Fertilizers")
fertilizer1 = st.number_input(label="Enter the cost of Fertilizer 1 per kilogram: ", min_value=0.00, step=0.5)
fertilizer1qty = st.number_input(label="Enter the number of kilos of Fertilizer 1 used: ", min_value=0.00, step=0.5)
fertilizer2 = st.number_input(label="Enter the cost of Fertilizer 2 per kilogram: ", min_value=0.00, step=0.5)
fertilizer2qty = st.number_input(label="Enter the number of kilos of Fertilizer 2 used: ", min_value=0.00, step=0.5)
organic_fertilizer = st.number_input(label="Enter the cost of Organic Fertilizer per kilogram: ", min_value=0.00, step=0.5)
organic_fertilizer_qty = st.number_input(label="Enter the number of kilos of Organic Fertilizer used: ", min_value=0.00, step=0.5)
st.subheader(f"Herbicide")
herbicide = st.number_input(label="Enter the cost of Herbicide per kilogram: ", min_value=0.00, step=0.5)
herbicide_qty = st.number_input(label="Enter the number of kilos of Herbicide used: ", min_value=0.00, step=0.5)
st.subheader(f"Pesticide")
pesticide = st.number_input(label="Enter the cost of Pesticide per kilogram: ", min_value=0.00, step=0.5)
pesticide_qty = st.number_input(label="Enter the number of kilos of Pesticide used: ", min_value=0.00, step=0.5)

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
    transport = st.radio("Did you incur any labor costs for Transportation?:", ("Yes", "No"))
    transport = 1 if transport == "Yes" else 0

st.header("Other Costs:")
other_cost = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)

if coffee_type == "Both":
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
    total_cost = (
            input_cost + m_labor_cost + m_postproduction_cost + other_cost + (m_transport * transport * amount_coffee)
        )
    total_percentfc = percent_traders + percent_othermarkets
    trader_fc_profit = (
            ((percent_traders/total_percentfc) * amount_fc) * price_traders
        )if total_percentfc and amount_fc > 0 else 0
    other_markets_fc_profit = (
            ((percent_othermarkets/total_percentfc) * amount_fc) * price_othermarkets
        )if total_percentfc and amount_fc > 0 else 0
    total_percentgc = percent_bigcompaniesgcb + percent_tradersgcb + percent_othermarketsgcb + percent_coopgcb
    big_companies_gcb_profit = (
            ((percent_bigcompaniesgcb/total_percentgc) * amount_gcb) * price_bigcompaniesgcb
    )if total_percentgc and amount_gcb > 0 else 0
    traders_gcb_profit = (
            ((percent_tradersgcb/total_percentgc) * amount_gcb) * price_tradersgcb
    )if total_percentgc and amount_gcb > 0 else 0
    other_markets_gcb_profit = (
            ((percent_othermarketsgcb/total_percentgc) * amount_gcb) * price_othermarketsgcb
    )if total_percentgc and amount_gcb > 0 else 0
    coop_gcb_profit = (
            ((percent_coopgcb/total_percentgc) * amount_gcb) * price_coopgcb
    )if total_percentgc and amount_gcb > 0 else 0
    total_profit = (
            (trader_fc_profit + other_markets_fc_profit + big_companies_gcb_profit + traders_gcb_profit + other_markets_gcb_profit + coop_gcb_profit) - (total_cost)
        )
    
if coffee_type == "Fresh":
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
    total_cost = (
            input_cost + m_labor_cost + other_cost + (m_transport * transport * amount_coffee)
        )
    trader_fc_profit = (
            (percent_traders / 100 * amount_fc) * price_traders
        )
    other_markets_fc_profit = (
            (percent_othermarkets / 100 * amount_fc) * price_othermarkets
        )
    total_profit = (
            (trader_fc_profit + other_markets_fc_profit ) - (total_cost)
        )
if coffee_type == "Green Coffee Beans":
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
    total_cost = (
            input_cost + m_labor_cost + m_postproduction_cost + other_cost + (m_transport * transport * amount_coffee)
        )
    big_companies_gcb_profit = (
            (percent_bigcompaniesgcb / 100 * amount_gcb) * price_bigcompaniesgcb
    )
    traders_gcb_profit = (
            (percent_tradersgcb / 100 * amount_gcb) * price_tradersgcb
    )
    other_markets_gcb_profit = (
            (percent_othermarketsgcb / 100 * amount_gcb) * price_othermarketsgcb
    )
    coop_gcb_profit = (
            (percent_coopgcb / 100 * amount_gcb) * price_coopgcb
    )
    total_profit = (
            (big_companies_gcb_profit + traders_gcb_profit + other_markets_gcb_profit + coop_gcb_profit) - (total_cost)
        )

def calculate_profit_both(percent_traders, percent_othermarkets, percent_bigcompaniesgcb, percent_coopgcb, percent_othermarketsgcb, percent_tradersgcb):
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
    total_cost = (
        input_cost + m_labor_cost + m_postproduction_cost + other_cost + (m_transport * transport * amount_coffee)
    )
    total_percentfc = percent_traders + percent_othermarkets
    total_percentgc = percent_tradersgcb + percent_othermarketsgcb + percent_coopgcb
    if total_percentfc > 0:
        trader_fc_profit = (
            ((percent_traders/total_percentfc) * amount_fc) * price_traders
        )
        other_markets_fc_profit = (
            ((percent_othermarkets/total_percentfc) * amount_fc) * price_othermarkets
        )
    if total_percentfc == 0:
        trader_fc_profit = 0
        other_markets_fc_profit = 0
    if total_percentgc > 0:
        big_companies_gcb_profit = (
            ((percent_bigcompaniesgcb/total_percentgc) * amount_gcb) * price_bigcompaniesgcb
        )
        traders_gcb_profit = (
            ((percent_tradersgcb/total_percentgc) * amount_gcb) * price_tradersgcb
        )
        other_markets_gcb_profit = (
            ((percent_othermarketsgcb/total_percentgc) * amount_gcb) * price_othermarketsgcb
        )
        coop_gcb_profit = (
            ((percent_coopgcb/total_percentgc) * amount_gcb) * price_coopgcb
        )
    if total_percentgc == 0:
        big_companies_gcb_profit = 0
        traders_gcb_profit = 0
        other_markets_gcb_profit = 0
        coop_gcb_profit = 0
    total_profit = (
        (trader_fc_profit + other_markets_fc_profit + big_companies_gcb_profit + traders_gcb_profit + other_markets_gcb_profit + coop_gcb_profit) - (total_cost)
    )
    return total_profit

def calculate_profit_fresh(percent_traders, percent_othermarkets):
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
    total_cost = (
        input_cost + m_labor_cost + other_cost + (m_transport * transport * amount_coffee)
    )
    trader_fc_profit = (
        (percent_traders * amount_fc) * price_traders
    )
    other_markets_fc_profit = (
        (percent_othermarkets * amount_fc) * price_othermarkets
    )
    total_profit = (
        (trader_fc_profit + other_markets_fc_profit) - (total_cost)
    )
    return total_profit

def calculate_profit_gcb(percent_bigcompaniesgcb, percent_coopgcb, percent_othermarketsgcb, percent_tradersgcb):
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
    total_cost = (
        input_cost + m_labor_cost + m_postproduction_cost + other_cost + (m_transport * transport * amount_coffee)
    )
    big_companies_gcb_profit = (
        (percent_bigcompaniesgcb * amount_gcb) * price_bigcompaniesgcb
    )
    traders_gcb_profit = (
        (percent_tradersgcb * amount_gcb) * price_tradersgcb
    )
    other_markets_gcb_profit = (
        (percent_othermarketsgcb * amount_gcb) * price_othermarketsgcb
    )
    coop_gcb_profit = (
        (percent_coopgcb * amount_gcb) * price_coopgcb
    )
    total_profit = (
        (big_companies_gcb_profit + traders_gcb_profit + other_markets_gcb_profit + coop_gcb_profit) - (total_cost)
    )
    return total_profit


def optimize_market_allocations():
    if coffee_type == "Fresh":
        variables = ['percent_traders', 'percent_othermarkets']
    if coffee_type == "Green Coffee Beans":
        variables = ['percent_bigcompaniesgcb', 'percent_coopgcb', 'percent_othermarketsgcb', 'percent_tradersgcb']
    if coffee_type == "Both":
        variables = ['percent_traders', 'percent_othermarkets', 'percent_bigcompaniesgcb', 'percent_coopgcb', 'percent_othermarketsgcb', 'percent_tradersgcb']
    values = np.linspace(0, 1, num=11)  # num=11 (0.1), num=101 (0.01), num=21 (0.05)

    # Define a generator function to generate possible combinations of market allocation with intervals
    def market_allocation_generator():
        # Generates all possible combinations of the elements in the values variable
        if type_of_allocation == "No":
            for combo in product(values, repeat=len(variables)):
                # Assign values to the markets by pairing the markets to the combination of values generated
                allocation = dict(zip(variables, combo))
                # Restriction to ensure market allocation is equal to 1
                if sum(allocation.values()) == 1:
                    yield allocation
        
        elif type_of_allocation == "Yes":
            for combo in product(values, repeat=len(variables)):
                # Assign values to the markets by pairing the markets to the combination of values generated
                allocation = dict(zip(variables, combo))
                # Check if all allocations have values
                if all(value > 0 for value in allocation.values()):
                    # Restriction to ensure market allocation is equal to 1
                    if sum(allocation.values()) == 1:
                        yield allocation

    # Create a list for the market allocations
    market_allocations = list(market_allocation_generator())
    num_allocations = len(market_allocations)
    profits = np.zeros(num_allocations)

    max_profit_case = market_allocations[0]  # Initialize with the first allocation
    if coffee_type == "Fresh":
        max_profit_value = calculate_profit_fresh(**max_profit_case)
    if coffee_type == "Green Coffee Beans":
        max_profit_value = calculate_profit_gcb(**max_profit_case)
    if coffee_type == "Both":
        max_profit_value = calculate_profit_both(**max_profit_case)

    # Calculate profits for each market allocation
    for i, case in enumerate(market_allocations):
        if coffee_type == "Fresh":
            profits[i] = calculate_profit_fresh(**case)
        if coffee_type == "Green Coffee Beans":
            profits[i] = calculate_profit_gcb(**case)
        if coffee_type == "Both":
            profits[i] = calculate_profit_both(**case)
        if profits[i] > max_profit_value:
            max_profit_value = profits[i]
            max_profit_case = case

    # Print overall maximum profit
    if coffee_type == "Both":
        if total_percentfc != 100 and total_percentgc != 100:
            st.warning("The allocation percentages for Fresh Cherries and Green Coffee Beans must each add up to 100%. Please adjust your allocations.")
        else:
            st.subheader(f"Optimized Market Allocation:")
            total_percentfc1 = max_profit_case['percent_traders'] * 100 + max_profit_case['percent_othermarkets'] * 100 if max_profit_case['percent_traders'] and max_profit_case['percent_othermarkets'] > 0 else 1
            st.subheader(f"Fresh Cherries Allocation:")
            st.write(f"Traders (Fresh):", round((((max_profit_case['percent_traders'] * 100) / total_percentfc1) * 100), 2), "%")
            st.write(f"Other Markets (Fresh):", round((((max_profit_case['percent_othermarkets'] * 100) / total_percentfc1) * 100), 2), "%")
            st.subheader(f"Green Coffee Beans Allocation:")
            if type_of_allocation == "Yes":
                total_percentgc1 = max_profit_case['percent_coopgcb'] * 100 + max_profit_case['percent_bigcompaniesgcb'] * 100 + max_profit_case['percent_tradersgcb'] * 100 + max_profit_case['percent_othermarketsgcb'] * 100 if max_profit_case['percent_traders'] and max_profit_case['percent_othermarkets'] > 0 else 1
                st.write(f"Cooperative (GCB): ", round(((max_profit_case['percent_coopgcb'] * 100 / total_percentgc1) * 100), 2), "%")
                st.write(f"Big Companies (GCB): ", round(((max_profit_case['percent_bigcompaniesgcb'] * 100 / total_percentgc1) * 100), 2), "%")
                st.write(f"Traders (GCB): ", round(((max_profit_case['percent_tradersgcb'] * 100 / total_percentgc1) * 100), 2), "%")
                st.write(f"Other Markets (GCB): ", round(((max_profit_case['percent_othermarketsgcb'] * 100 / total_percentgc1) * 100), 2), "%")
                st.markdown(f"<b>Maximum Profit: ₱{max_profit_value:.2f}</b>", unsafe_allow_html=True)
            elif type_of_allocation == "No":
                total_percentgc1 = max_profit_case['percent_coopgcb'] * 100 + max_profit_case['percent_bigcompaniesgcb'] * 100 + max_profit_case['percent_tradersgcb'] * 100 + max_profit_case['percent_othermarketsgcb'] * 100 if max_profit_case['percent_traders'] and max_profit_case['percent_othermarkets'] > 0 else 1
                st.write(f"Cooperative (GCB): ", round((max_profit_case['percent_coopgcb'] * 100 / total_percentgc1), 2), "%")
                st.write(f"Big Companies (GCB): ", round((max_profit_case['percent_bigcompaniesgcb'] * 100 / total_percentgc1), 2), "%")
                st.write(f"Traders (GCB): ", round((max_profit_case['percent_tradersgcb'] * 100 / total_percentgc1), 2), "%")
                st.write(f"Other Markets (GCB): ", round((max_profit_case['percent_othermarketsgcb'] * 100 / total_percentgc1), 2), "%")
                st.markdown(f"<b>Maximum Profit: ₱{max_profit_value:.2f}</b>", unsafe_allow_html=True)
    if coffee_type == "Fresh":
        if total_percentfc != 100:
            st.warning("The allocation percentages for Fresh Cherries must add up to 100%. Please adjust your allocations.")
        else:
            st.subheader(f"Optimized Market Allocation:")
            st.write(f"Traders (Fresh):", max_profit_case['percent_traders'] * 100, "%")
            st.write(f"Other Markets (Fresh):", max_profit_case['percent_othermarkets'] * 100, "%")
            st.markdown(f"<b>Maximum Profit: ₱{max_profit_value:.2f}</b>", unsafe_allow_html=True)
    if coffee_type == "Green Coffee Beans":
        if total_percentgc != 100:
            st.warning("The allocation percentages for Green Coffee Beans must add up to 100%. Please adjust your allocations.")
        else:
            st.subheader(f"Optimized Market Allocation:")
            st.write(f"Cooperative (GCB): ", max_profit_case['percent_coopgcb'] * 100, "%")
            st.write(f"Big Companies (GCB): ", max_profit_case['percent_bigcompaniesgcb'] * 100, "%")
            st.write(f"Traders (GCB): ", max_profit_case['percent_tradersgcb'] * 100, "%")
            st.write(f"Other Markets (GCB): ", max_profit_case['percent_othermarketsgcb'] * 100, "%")
            st.markdown(f"<b>Maximum Profit: ₱{max_profit_value:.2f}</b>", unsafe_allow_html=True)

if st.button("Optimize"):
    if coffee_type == "Both":
        if total_percentfc != 100 and total_percentgc != 100:
            st.markdown(f"<b>Error:</b>", unsafe_allow_html=True)
        else:
            st.subheader(f"Desired allocation:")
            st.subheader(f"Fresh Cherries Allocation:")
            st.write(f"Traders (Fresh): ", (percent_traders/total_percentfc)*100, "%")
            st.write(f"Other Marketsc (Fresh): ", (percent_othermarkets/total_percentfc)*100, "%")
            st.subheader(f"Green Coffee Beans Allocation:")
            st.write(f"Cooperative (GCB): ", (percent_coopgcb/total_percentgc)*100, "%")
            st.write(f"Big Companies (GCB): ", (percent_bigcompaniesgcb/total_percentgc)*100, "%")
            st.write(f"Traders (GCB): ", (percent_tradersgcb/total_percentgc)*100, "%")
            st.write(f"Other Markets (GCB): ", (percent_othermarketsgcb/total_percentgc)*100, "%")
            st.markdown(f"<b>Estimated Total Profit: ₱{total_profit:.2f}</b>", unsafe_allow_html=True)
            st.write(f"\n")
            st.write(f"\n")
    if coffee_type == "Fresh":
        if total_percentfc != 100:
            st.markdown(f"<b>Error:</b>", unsafe_allow_html=True)
        else:
            st.subheader(f"Desired allocation:")
            st.write(f"Traders (Fresh): ", percent_traders, "%")
            st.write(f"Other Marketsc (Fresh): ", percent_othermarkets, "%")
            st.markdown(f"<b>Estimated Total Profit: ₱{total_profit:.2f}</b>", unsafe_allow_html=True)
            st.write(f"\n")
            st.write(f"\n")
    if coffee_type == "Green Coffee Beans":
        if total_percentgc != 100:
            st.markdown(f"<b>Error:</b>", unsafe_allow_html=True)
        else:
            st.subheader(f"Desired allocation:")
            st.write(f"Cooperative (GCB): ", percent_coopgcb, "%")
            st.write(f"Big Companies (GCB): ", percent_bigcompaniesgcb, "%")
            st.write(f"Traders (GCB): ", percent_tradersgcb, "%")
            st.write(f"Other Markets (GCB): ", percent_othermarketsgcb, "%")
            st.markdown(f"<b>Estimated Total Profit: ₱{total_profit:.2f}</b>", unsafe_allow_html=True)
            st.write(f"\n")
            st.write(f"\n")
    optimize_market_allocations()
