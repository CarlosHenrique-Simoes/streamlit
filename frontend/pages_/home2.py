import time  # noqa: D100

import pandas as pd
import streamlit as st
from streamlit import rerun

if "tax_quantity" not in st.session_state:
    st.session_state["tax_quantity"] = 0

if "containers" not in st.session_state:
    st.session_state["containers"] = []

if "containers_quantity" not in st.session_state:
    st.session_state["containers_quantity"] = 0

containers = []

def linha_azul():
    st.markdown(
        """
        <hr style="border: 2px solid #1E7FE4;">
        """,
        unsafe_allow_html=True,
    )


def linha_azul_escuro():
    st.markdown(
        """
        <hr style="border: 2px solid #4682B4;">
        """,
        unsafe_allow_html=True,
    )


def salva_sessao():
    st.session_state["house_bl"] = st.session_state["house_bl"]
    st.session_state["vessel_origin"] = st.session_state["vessel_origin"]

def home_page():
    """Página principal do sistema de cadastro de embarques marítimos.

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
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Embarque")
            # Campo de texto
            house_bl = st.text_input(
                "House BL",
                key="house_bl",
                value=st.session_state.get("house_bl", ""),
            )
        with col2:
            st.markdown("### 📋")
            master_bl = st.text_input(
                "Master BL",
                key="master_bl",
            )

        linha_azul()

        co1, co2 = st.columns(2)
        with co1:
            escolha_de_taxa = st.number_input(
                "Escolha A Quantidade de Taxas",
                min_value=3,
                max_value=15,
                step=1,
                key="escolha_de_taxa",
            )
        with co2:
            escolha_de_container = st.number_input(
                "Informe a Quantidade de Containers",
                min_value=1,
                step=1,
            )
        if st.form_submit_button("Gerar Lista de Dados"):
            if st.session_state["house_bl"] == "":
                st.error("House BL deve ser preenchido.")

            else:
                st.warning(f"{st.session_state['house_bl']}")

                st.session_state["tax_quantity"] = escolha_de_taxa
                st.session_state["containers_quantity"] = escolha_de_container

                with col1:
                    shipper = st.text_area(
                        label="Shipper",
                        height=123,
                        key="shipper",
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
                    vessel_origin = st.text_input(
                        "Navio de Origem",
                        key="vessel_origin",
                        value=st.session_state.get("vessel_origin", ""),
                    )

                with col2:
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
                    onboard_date = st.date_input(
                        "Onboard date",
                        key="onboard_date",
                    )
                    issue_date = st.date_input(
                        "Issue date",
                        key="issue_date",
                    )

                with col1:
                    linha_azul()
                    st.markdown("### Frete")
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
                with col2:
                    linha_azul()
                    st.markdown("### 💰")
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

                if st.session_state["tax_quantity"] > 3:
                    st.session_state["tax_quantity"] -= 3
                    for i in range(st.session_state["tax_quantity"]):
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

                if st.session_state["containers_quantity"] > 0:
                    with col1:
                        linha_azul()
                        st.markdown("### Dados dos Containers")
                    with col2:
                        linha_azul()
                        st.markdown("### 📦")
                    for i in range(escolha_de_container):
                        container_data = {}
                        with col1:
                            container = st.text_input(
                                f"Container {i + 1}",
                                key=f"container_{i + 1}",
                            ).upper()
                            container_weight = st.number_input(
                                f"Gross Weight {i + 1}",
                                min_value=0.0,
                                format="%.3f",
                                key=f"container_weight_{i + 1}",
                            )
                            container_tare = st.number_input(
                                f"Container Tare {i + 1}",
                                min_value=0.0,
                                format="%.3f",
                                key=f"container_tare_{i + 1}",
                            )
                            container_data["container"] = container
                            container_data["container_weight"] = container_weight
                            linha_azul_escuro()

                        with col2:
                            container_cbm = st.number_input(
                                f"Container CBM {i + 1}",
                                min_value=0.0,
                                format="%.3f",
                                key=f"container_cbm {i + 1}",
                            )
                            container_type = st.selectbox(
                                f"Container Type {i + 1}",
                                ["22GP", "45GP"],
                                index=None,
                                key=f"container_type_{i + 1}",
                            )
                            ncm = st.multiselect(
                                f"NCMs {i + 1}",
                                ["8151"],
                                default=None,
                                key=f"ncm_{i + 1}",
                            )
                            container_data["container_type"] = container_type
                            container_data["ncm"] = ncm
                            container_data["container_tare"] = container_tare
                            container_data["container_cbm"] = container_cbm
                            linha_azul_escuro()

                        with col1:
                            if st.form_submit_button("Salvar Container"):
                                st.session_state["vessel_origin"] = vessel_origin

    if st.button("Enviar Embarque", key="enviar_embarque", on_click=salva_sessao):

        st.warning(f"{st.session_state['house_bl']}")
        st.warning(f"{st.session_state['vessel_origin']}")
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
            # st.rerun()

        # Botão para sair
    if st.button("Sair", key="logout"):
        st.session_state.user_id = None
        st.session_state.page = "login"  # Volta para a página inicial
        rerun()
