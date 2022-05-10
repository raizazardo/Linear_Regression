import streamlit as st
import pandas as pd
import joblib

model_path = "/Users/raiza/Documents/Python/Linear_Regression/linear_model.sav"
model = joblib.load(model_path)


def predict(attributes):
    prediction = model.predict(attributes)
    return prediction


# page config
st.set_page_config(page_title="Acidez total no vinho tinto ",
                   page_icon="🍷",
                   layout="centered")

# page settings
st.title(f"Predição da acidez total no vinho tinto")
st.subheader(
    "Modelo de Regressão Linear\n" "Desenvolvido por: Alysson Oliveira e Raiza Zardo")

with st.form("Formulário de predição"):
    st.header("Especificações do vinho:")
    # imput elements
    acido_citrico = st.slider(label="Ácido cítrico: ",
                              min_value=0.0, max_value=1.0, step=0.01)
    sulfatos = st.slider(label="Sulfatos: ", min_value=0.0,
                         max_value=2.0, step=0.01)
    qualidade = st.slider(label="Qualidade: ",
                          min_value=0.0, max_value=8.0, step=0.01)
    acucar_residual = st.slider(
        label="Açucar Residual: ", min_value=0.0, max_value=15.50, step=0.01)

# submit values
    submit_values = st.form_submit_button(label="Submit")
    if submit_values:
        # create input dictionary
        input_dic = {
            "acido_citrico": acido_citrico,
            "sulfatos": sulfatos,
            "qualidade": qualidade,
            "acucar_residual": acucar_residual
        }
    # create input dataframe
        input_dataframe = pd.DataFrame(input_dic, index=[1])
    # make preditions
        prediction = predict(input_dataframe)

    st.header(f"O resultado é: {prediction}")
    # output results
    st.success(f"A acidez total do vinho é igual a: {prediction}")
