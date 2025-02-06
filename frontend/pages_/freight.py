import time  # noqa: D100

import pandas as pd
import streamlit as st
from streamlit import rerun


def freight_page():

    st.title("Cadastro de Frete 💰")
    with st.form("Cadastrar Frete"):
        col1, col2 = st.columns(2)

        with col1:
            hbl_freight = st.text_input(
                "House BL Frete",
                key="hbl_freight",
            )

        with col2:
            escolha_de_taxa = st.number_input(
                "Escolha A Quantidade de Taxas",
                min_value=1,
                step=1,
                key="escolha_de_taxa",
            )

        if st.form_submit_button("Abrir Quantidade de taxas"):
            if escolha_de_taxa is None:
                st.warning(
                    "Por favor, escolha a quantidade de taxas.",
                )
            else:
                col1, col2 = st.columns(2)

                with col1:
                    if escolha_de_taxa >= 3:
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
                    if escolha_de_taxa >= 5:
                        fourth_fee = st.number_input(
                            "4ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        fifth_fee = st.number_input(
                            "5ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                    if escolha_de_taxa >= 11:
                        sixth_fee = st.number_input(
                            "6ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        seventh_fee = st.number_input(
                            "7ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        eighth_fee = st.number_input(
                            "8ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        ninth_fee = st.number_input(
                            "9ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        tenth_fee = st.number_input(
                            "10ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        eleventh_fee = st.number_input(
                            "11ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                    if escolha_de_taxa >= 15:
                        twelfth_fee = st.number_input(
                            "12ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        thirtheenth_fee = st.number_input(
                            "13ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        fourteenth_fee = st.number_input(
                            "14ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                        fifteenth_fee = st.number_input(
                            "15ª Taxa",
                            min_value=0.0,
                            format="%.2f",
                        )
                with col2:
                    if escolha_de_taxa >= 3:
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
                    if escolha_de_taxa >= 5:
                        fourth_fee_currency = st.selectbox(
                            "Moeda da 4ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        fifth_fee_currency = st.selectbox(
                            "Moeda da 5ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                    if escolha_de_taxa >= 11:
                        sixth_fee_currency = st.selectbox(
                            "Moeda da 6ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        seventh_fee_currency = st.selectbox(
                            "Moeda da 7ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        eighth_fee_currency = st.selectbox(
                            "Moeda da 8ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        ninth_fee_currency = st.selectbox(
                            "Moeda da 9ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        tenth_fee_currency = st.selectbox(
                            "Moeda da 10ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        eleventh_fee_currency = st.selectbox(
                            "Moeda da 11ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                    if escolha_de_taxa >= 15:
                        twelfth_fee_currency = st.selectbox(
                            "Moeda da 12ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        thirtheenth_fee_currency = st.selectbox(
                            "Moeda da 13ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        fourteenth_fee_currency = st.selectbox(
                            "Moeda da 14ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )
                        fifteenth_fee_currency = st.selectbox(
                            "Moeda da 15ª Taxa",
                            ["USD", "BRL"],
                            index=0,
                        )