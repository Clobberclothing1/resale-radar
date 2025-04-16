
import streamlit as st
from pricing import ebay_price_stats
from trend_scraper import vinted_trending
from brand_detect import detect_brand
import tracker

st.set_page_config(page_title="Resale Radar", layout="centered")
st.title("Resale Radar – Vinted Valuer")

st.header("📸 Item Valuer")
uploaded = st.file_uploader("Upload an item photo", type=["jpg", "jpeg", "png"])
if uploaded:
    brand_guess = detect_brand(uploaded)
    query = st.text_input("Brand / item keywords", value=brand_guess)
    if st.button("Get resale price"):
        if query:
            stats = ebay_price_stats(query)
            st.markdown(f"**eBay sold price range:** £{stats['low']} – £{stats['high']}  
Median: **£{stats['median']}**")
        else:
            st.warning("Enter a search query first.")

st.header("🔥 Trending on Vinted")
if st.button("Refresh trending list"):
    tags = vinted_trending()
    st.write(tags)

st.header("💰 Profit Tracker")
with st.form("log_form"):
    col1, col2 = st.columns(2)
    with col1:
        item = st.text_input("Item description")
        bought = st.number_input("Bought for (£)", min_value=0.0, step=0.10)
    with col2:
        sold = st.number_input("Sold for (£)", min_value=0.0, step=0.10)
        platform = st.selectbox("Platform", ["Vinted", "eBay", "Depop", "Other"])
    submitted = st.form_submit_button("Log sale")
    if submitted:
        tracker.log_sale(item, bought, sold, platform)
        st.success("Sale logged!")

st.subheader("📈 Profit history")
df = tracker.get_log()
st.dataframe(df)
