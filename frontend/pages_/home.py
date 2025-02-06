import time  # noqa: D100

import pandas as pd
import streamlit as st
from streamlit import rerun


def home_page():
    """
    Página principal do sistema de cadastro de embarques marítimos.

    Ela contém um formulário com vários campos para coletar informações
    sobre o embarque, como House BL, Master BL, Shipper, Consignee,
    Notify, Porto de Origem, Porto de Destino, Navio de Origem,
    Número da Viagem, Tipo de Embalagem, Quantidade de Embalagem,
    Peso Bruto e Cubagem do House.

    Os dados coletados são enviados para uma API via POST e, em seguida,
    são exibidos na tela.

    Se todos os campos forem preenchidos corretamente, a página será
    recarregada.
    """
    st.title("Cadastro de Embarque Marítimo ⚓")

    # Criando o formulário com vários tipos de entradas
    with st.form("dados_do_importador"):  # Dados do Importador

        col1, col2, col3 = st.columns(3)

        with col1:
            # Campo de texto
            house_bl = st.text_input(
                "House BL",
                key="house_bl",
            )
            master_bl = st.text_input(
                "Master BL",
                key="master_bl",
            )
            consignee = st.selectbox(
                "Consignee",
                ["SEDA", "SDS"],
                index=0,
                key="consignee",
            )
            notify = st.selectbox(
                "Notify",
                ["SEDA", "SDS"],
                index=0,
                key="notify",
            )
            port_of_loading = st.selectbox(
                "Porto de Origem",
                ["BRMAO", "BRSSZ", "BRRIO"],
                index=0,
                key="port_of_loading",
            )
            port_of_discharge = st.selectbox(
                "Porto de Destino",
                ["BRMAO", "BRSSZ", "BRRIO"],
                index=0,
                key="port_of_discharge",
            )

        with col2:
            vessel_origin = st.text_input(
                "Navio de Origem",
                key="vessel_origin",
            )
            vessel_voyage = st.text_input(
                "Número da Viagem",
                key="vessel_voyage",
            )
            package_type = st.text_input(
                "Tipo de Embalagem",
                max_chars=3,
                key="package_type",
            )

            package_quantity = st.number_input(
                "Quantidade de Embalagem",
                min_value=0.0,
                format="%.1f",
                key="package_quantity",
            )
            gross_weight = st.number_input(
                "Informe o Peso Bruto",
                min_value=0.0,
                format="%.3f",
                key="gross_weight",
            )
            cbm = st.number_input(
                "Informe a Cubagem do House",
                min_value=0.0,
                format="%.3f",
                key="cbm",
            )

        with col3:
            shipper = st.text_area(
                label="Shipper",
                height=123,
                key="shipper",
            )
            onboard_date = st.date_input(
                "Onboard date",
                key="onboard_date",
            )
            issue_date = st.date_input(
                "Issue date",
                key="issue_date",
            )


        if st.form_submit_button("Enviar"):

            if (
                house_bl == ""
                or master_bl == ""
                or shipper == ""
                or consignee == ""
                or notify == ""
                or port_of_loading == ""
                or port_of_discharge == ""
                or onboard_date is None
                or issue_date is None
                or vessel_origin == ""
                or vessel_voyage == ""
                or package_quantity == 0
                or package_type == ""
                or gross_weight == 0
                or cbm == 0
            ):
                st.error("Por favor, preencha todos os campos!")
            else:
                st.success(f"Dados enviados com sucesso.")

                if notify == "SEDA":
                    notify = "Samsung Electronics"
                elif notify == "SDS":
                    notify = "Samsung SDS"

                if consignee == "SEDA":
                    consignee = "Samsung Electronics"
                elif consignee == "SDS":
                    consignee = "Samsung SDS"

                json_data = {
                    "house_bl": house_bl,
                    "master_bl": master_bl,
                    "shipper": shipper,
                    "consignee": consignee,
                    "notify": notify,
                    "port_of_loading": port_of_loading,
                    "place_of_receipt": port_of_loading,
                    "port_of_discharge": port_of_discharge,
                    "vessel_origin": vessel_origin,
                    "vessel_voayge": vessel_voyage,
                    "package_quantity": package_quantity,
                    "package_type": package_type,
                    "gross_weight": gross_weight,
                    "cbm": cbm,
                    "onboard_date": onboard_date,
                    "issue_date": issue_date,
                }

                df_json = pd.DataFrame([json_data])

                df_json = df_json[
                    [
                        "house_bl",
                        "master_bl",
                        "shipper",
                        "port_of_loading",
                    ]
                ]

                st.write(df_json.to_html(index=False), unsafe_allow_html=True)
                time.sleep(4)
                st.rerun()

        # if submit_button:

        # Botão para sair
    if st.button("Sair", key="logout"):
        st.session_state.user_id = None
        st.session_state.page = "login"  # Volta para a página inicial
        rerun()
