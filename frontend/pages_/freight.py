import time  # noqa: D100

import pandas as pd
import streamlit as st
from streamlit import rerun

if "tax_quantity" not in st.session_state:
    st.session_state["tax_quantity"] = None

if "freight_data" not in st.session_state:
    st.session_state["freight_data"] = {
        "house_bl": None,
        "master_bl": None,
        "freight": 0,
        "terminal_handling": 0,
        "documentation_fee": 0,
        "freight_currency": None,
        "terminal_handling_currency": None,
        "documentation_fee_currency": None,
    }


def freight_page():
    st.title("Cadastro de Frete 💰")
    with st.form("Cadastrar Frete"):
        col1, col2 = st.columns(2)

        with col1:
            hbl_freight = st.text_input(
                "House BL Frete",
                key="hbl_freight",
            )
            freight = st.number_input(
                "Informe o Frete",
                min_value=0.0,
                format="%.2f",
            )
            terminal_handling = st.number_input(
                "Capatazia",
                min_value=0.0,
                format="%.2f",
            )
            documentation_fee = st.number_input(
                "Doc Fee",
                min_value=0.0,
                format="%.2f",
            )
            escolha_de_taxa = st.number_input(
                "Escolha A Quantidade de Taxas",
                min_value=0,
                max_value=12,
                step=1,
                key="escolha_de_taxa",
            )

        with col2:
            mbl_freight = st.text_input(
                "Master_BL",
                key="mbl_freight",
            )
            freight_currency = st.selectbox(
                "Moeda do Frete",
                ["USD", "BRL"],
                index=0,
            )
            terminal_handling_currency = st.selectbox(
                "Moeda da Capatazia",
                ["USD", "BRL"],
                index=0,
            )
            documentation_fee_currency = st.selectbox(
                "Moeda do Doc Fee", ["USD", "BRL"], index=0
            )

        if st.form_submit_button("Abrir Quantidade de taxas"):

            st.session_state["tax_quantity"] = escolha_de_taxa
            st.warning(
                f"{escolha_de_taxa}"
            )

            if st.session_state["tax_quantity"] is None:
                st.warning(
                    "Por favor, escolha a quantidade de taxas.",
                )
            else:
                if "tax_values" not in st.session_state:
                    st.session_state["tax_values"] = []

                if "currency_values" not in st.session_state:
                    st.session_state["currency_values"] = []

                st.session_state["tax_values"].clear()  # Limpar caso o usuário reenvie
                st.session_state["currency_values"].clear()

                for i in range(st.session_state["tax_quantity"]):
                    col1, col2 = st.columns(2)

                    with col1:
                        hbl_fee = st.number_input(
                            f"{i + 4}ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                            key=f"hbl_fee_{i + 4}",
                        )
                    with col2:
                        currency_fee = st.selectbox(
                            f"Moeda da {i + 4}ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                            key=f"currency_fee_{i + 4}",
                        )
                    # Armazena os valores no session_state
                    st.session_state["tax_values"].append(hbl_fee)
                    st.session_state["currency_values"].append(currency_fee)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Enviar"):
            # Captura os valores mais recentes dos inputs no momento do clique
            st.session_state["freight_data"] = {
                "house_bl": hbl_freight,
                "master_bl": mbl_freight,
                "freight": freight,
                "terminal_handling": terminal_handling,
                "documentation_fee": documentation_fee,
                "freight_currency": freight_currency,
                "terminal_handling_currency": terminal_handling_currency,
                "documentation_fee_currency": documentation_fee_currency,
            }

            if st.session_state["tax_quantity"] > 0 and (
                len(st.session_state["tax_values"]) < st.session_state["tax_quantity"]
                or len(st.session_state["currency_values"])
                < st.session_state["tax_quantity"]  # noqa: E501
            ):
                st.error(
                    f"Você indicou {st.session_state['tax_quantity']} taxa(s), mas não preencheu todas elas.",  # noqa: E501
                )

            elif (
                hbl_freight is None
                or mbl_freight is None
                or freight == 0
                or terminal_handling == 0
                or documentation_fee == 0
                or freight_currency is None
                or terminal_handling_currency is None
                or documentation_fee_currency is None
            ):
                st.error("Preencha todos os campos")

            elif any(
                tax == 0 or tax is None for tax in st.session_state["tax_values"]
            ) or any(  # noqa: E501
                currency is None for currency in st.session_state["currency_values"]
            ):
                st.error(
                    "Preencha todos os valores e moedas para as taxas antes de enviar.",
                )
            else:
                json_data = {
                    "house_bl": hbl_freight,
                    "master_bl": mbl_freight,
                    "freight": freight,
                    "terminal_handling": terminal_handling,
                    "documentation_fee": documentation_fee,
                    "freight_currency": freight_currency,
                    "terminal_handling_currency": terminal_handling_currency,
                    "documentation_fee_currency": documentation_fee_currency,
                }

                if st.session_state["tax_quantity"] > 0:
                    for i, (tax, currency) in enumerate(
                        zip(
                            st.session_state["tax_values"],
                            st.session_state["currency_values"],
                        ),
                    ):
                        json_data[f"tax_{i + 1}"] = tax
                        json_data[f"currency_{i + 1}"] = currency

                df_json = pd.DataFrame([json_data])

                df_json = df_json[
                    [
                        "house_bl",
                        "master_bl",
                        "freight",
                        "terminal_handling",
                        "documentation_fee",
                    ]
                ]
                st.success("Valores de Frete Enviados com Sucesso!")
                st.write(df_json.to_html(index=False), unsafe_allow_html=True)
                time.sleep(4)
                rerun()

    with col2:
        if st.button("Sair", key="logout"):
            st.session_state.user_id = None
            st.session_state.page = "home"  # Volta para a página inicial
            rerun()
