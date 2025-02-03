import streamlit as st

def calculate_tax_with_rebate(income, is_salaried):
    """Tax calculation logic"""
    standard_deduction = 50000 if is_salaried else 0
    taxable_income = income - standard_deduction

    tax = 0
    if taxable_income > 300000:
        if taxable_income <= 700000:
            tax = (taxable_income - 300000) * 0.05
        elif taxable_income <= 1000000:
            tax = 20000 + (taxable_income - 700000) * 0.10
        elif taxable_income <= 1200000:
            tax = 50000 + (taxable_income - 1000000) * 0.15
        elif taxable_income <= 1500000:
            tax = 80000 + (taxable_income - 1200000) * 0.20
        else:
            tax = 140000 + (taxable_income - 1500000) * 0.30

    if taxable_income <= 1275000:
        rebate = min(tax, 60000)
        tax -= rebate

    return max(tax, 0)

# Streamlit UI
st.title("💰 Income Tax Calculator (India - 2025)")
income = st.number_input("Enter your Annual Income (₹)", min_value=0.0, step=1000.0)
is_salaried = st.checkbox("Are you a salaried employee?")

if st.button("Calculate Tax"):
    tax = calculate_tax_with_rebate(income, is_salaried)
    st.success(f"Your tax payable is: ₹{tax:.2f}")
