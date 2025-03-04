import streamlit as st

def calculate_tax_with_rebate(income, is_salaried):
    """Tax calculation logic"""
    standard_deduction = 75000 if is_salaried else 0
    taxable_income = income - standard_deduction

    tax = 0
    if taxable_income > 400000:
        if taxable_income <= 800000:
            tax = (taxable_income - 400000) * 0.05
        elif taxable_income <= 1200000:
            tax = 20000 + (taxable_income - 800000) * 0.10
        elif taxable_income <= 1600000:
            tax = 60000 + (taxable_income - 1200000) * 0.15
        elif taxable_income <= 2000000:
            tax = 120000 + (taxable_income - 1600000) * 0.20
        else:
            tax = 200000 + (taxable_income - 2000000) * 0.30
            
    if taxable_income <= 1275000: 
        rebate = min(tax, 60000)  # Updated rebate limit
        tax -= rebate

    return max(tax, 0)

# Streamlit UI
st.title("💰 Income Tax Calculator (India - shashank)" , " By shashank ")

income = st.number_input("Enter your Annual Income (₹)", min_value=0.0, step=1000.0)
is_salaried = st.checkbox("Are you a salaried employee?")

if st.button("Calculate Tax"):
    tax = calculate_tax_with_rebate(income, is_salaried)
    st.success(f"Your tax payable is: ₹{tax:.2f}")
