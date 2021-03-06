import streamlit as st
import pickle
import  numpy as np
rand_for_model = pickle.load(open('rand_for_model','rb')) 

def predict_price(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
    input = np.array([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])#.astype(np.float64)
    price=rand_for_model.predict(input)
    return float(price)


def main():
    #front end elements of web page     
    html_temp = """
    <div style="background-color:; padding:10px">
    <h1 style="color:black;text-align:center;">Real Estate Price Predictor</h1>

    """
    st.markdown(html_temp,unsafe_allow_html=True)
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://www.onthemarket.com/content/wp-content/uploads/2018/01/Housepricepredictions2018lead.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


    CRIM = st.text_input("CRIM - per capita crime rate by town","")
    ZN = st.text_input("ZN - proportion of residential land zoned for lots over  25,000 sq.ft.","")
    INDUS = st.text_input("INDUS - proportion of non-retail business acres per town","")
    CHAS = st.text_input("CHAS - Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)","")
    NOX = st.text_input("NOX -  nitric oxides concentration (parts per 10 million)","")
    RM = st.text_input("RM - average number of rooms per dwelling","")
    AGE = st.text_input("AGE - proportion of owner-occupied units built prior to 1940","")
    DIS = st.text_input("DIS - weighted distances to five Boston employment centres","")
    RAD = st.text_input("RAD - index of accessibility to radial highways","")
    TAX = st.text_input("TAX - full-value property-tax rate per $10,000","")
    PTRATIO = st.text_input("PTRATIO - pupil-teacher ratio by town","")
    B = st.text_input("B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town","")
    LSTAT = st.text_input("LSTAT - % lower status of the population","")
    

    if st.button("Predict"):
        output = predict_price(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
        st.success('The price of your house is (in Lacs) {}'.format(output))

if __name__=='__main__':
    main()

