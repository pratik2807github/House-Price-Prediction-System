import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

model = pickle.load(open('house_price_model.pkl', 'rb'))

features = pickle.load(open('features.pkl', 'rb'))

st.set_page_config(page_title='House Price Prediction',
                  page_icon = "🏠",
                  layout='wide'
                  )

st.title('🏠 House Price Prediction System')

st.sidebar.title('Navigation')

st.sidebar.info(
    '''
    House Price Prediction System

    Model: Linear Regression

    Built with:
    -Python
    -Scikit-Learn
    -Streamlit
    '''
)

st.caption('Enter property details below to estimate the house price.')

st.header('Enter House Details')

st.subheader('🏡 Property Information')

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input('Bedrooms',min_value=0,value=3)

with col2:
    bathrooms = st.number_input('Bathrooms',min_value=0.0,value=2.0)

with col1:
    sqft_lot = st.number_input('Lot Area (sqft)',min_value=0,value=5000)

with col2:
    floors = st.number_input('Floors',min_value=1.0,value=1.0)

with col1:
    waterfront = st.number_input('Waterfront(0=No,1=Yes)',min_value=0,max_value=1,value=0)

with col2:
    view = st.number_input('View',min_value=0,max_value=4,value=0)

with col1:
    condition = st.number_input('Condition',min_value=1,max_value=5,value=3)

with col2:
    sqft_above = st.number_input('Sqft Above',min_value=0,value=1500)

with col1:
    sqft_basement = st.number_input('Sqft Basement',min_value=0,value=500)

with col2:
    yr_built = st.number_input('Year Built',min_value=1900,max_value=2025,value=2000)

with col1:
    yr_renovated = st.number_input('Year Renovated',min_value=0,max_value=2025,value=0)

base_features = ['bedrooms','bathrooms','sqft_lot','floors','waterfront','view','condition','sqft_above','sqft_basement','yr_built','yr_renovated']

st.subheader('📍 Location Information')

loc_col1, loc_col2 = st.columns(2)

city_options = [
    c for c in model.feature_names_in_
    if c not in base_features and not str(c).isdigit()
]

with loc_col1:
    city = st.selectbox('City', city_options)

zip_options = [
    c for c in model.feature_names_in_
    if str(c).isdigit()
]


with loc_col2:
    statezip = st.selectbox('ZIP Code', zip_options)

st.subheader('🎯 Price Prediction')

if st.button('🔄 Reset Inputs'):
    st.rerun()

if st.button('🔮 Predict House Price'):

    if sqft_above <= 0:
        st.error('Sqft Above must be greater than 0.')
        st.stop()

    st.subheader('📋 Input Summary')

    st.write(f'Bedrooms: {bedrooms}')
    st.write(f'Bathrooms: {bathrooms}')
    st.write(f'Lot_Area: {sqft_lot}')
    st.write(f'Floors: {floors}')
    st.write(f'City: {city}')
    st.write(f'ZIP Code: {statezip}')
    
    input_data = {
        bedrooms,
        bathrooms,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        }
    input_df = pd.DataFrame([input_data])

    input_df[city] = 1
    input_df[statezip] = 1

    input_df = input_df.reindex(
        columns=model.feature_names_in_,
        fill_value = 0
    )

    prediction = model.predict(input_df)

    predicted_price = prediction[0]

    st.divider()

    st.metric(
        label='🏠 Estimated House Price', 
        value=f'${predicted_price:,.2f}'
    )

    st.caption(f'🕒 Prediction generated on:{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}')

    if predicted_price < 300000:
        st.info('💰 Budget-Friendly Property')
    elif predicted_price < 700000:
        st.success('🏡 Mid-Range Property')
    else:
        st.warning('🏘️ Premium Property')

    st.subheader('🎯 Prediction Confidence')

    if predicted_price > 0:
        st.progress(58)

        st.caption('Model R2 Score: 58.14% | Prediction should be used as an estimate.')

    average_price = 540000
    difference = predicted_price - average_price
    
    if difference > 0:
        st.success(f'📈 ${difference:,.2f} above the average market price')
    elif difference < 0:
        st.info(f'📉 ${abs(difference):,.2f} below the average market price')
    else:
        st.warning('📊 Equal to the average market price')

    with st.expander('📊  View Prediction Summary'):
        
        st.markdown(f'''**🏠 Bedrooms:** {bedrooms}
        **🛁 Bathrooms:** {bathrooms}
        **🌆City:** {city}
        **📮 ZIP Code:** {statezip}''')
        
    st.write(f'''Based on the property details, the estimated market value of this property is **${predicted_price:,.2f}**.''')
    st.write('### Market Value Indicator')
    progress_value = max(0.0,min(predicted_price / 1000000,1.0))
    st.progress(progress_value)

    with st.expander('📈 Model Performance'):
        st.write('Model: Linear Regression')
        st.write('R2 Score: 58.14%')
        st.write('MAE: $156,419')
        st.write('RMSE: $245,119')

    with st.expander('ℹ️ About This Project'):
        st.write("""This House Price Prediction System uses a Linear Regression model trained on real estate data to estimate house prices based on property
        features such as bedrooms,bathrooms,lot size,location,condition,and construction details.
        The project includes:
        ✅ Data Cleaning
        ✅ Outlier Removal
        ✅ Feature Engineering
        ✅ Machine Learning Model Training
        ✅ Streamlit Web Application
        """)
        st.divider()

        st.caption('Developed by Pratik Gurav | House Price Prediction using Machine Learning & Streamlit')

st.write('This system predicts house prices using property features and Linear Regression model.')













