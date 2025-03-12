import pandas as pd  # noqa: D100
import streamlit as st

if "hbl_container" not in st.session_state:
    st.session_state["hbl_container"] = None

if "containers" not in st.session_state:
    st.session_state["containers"] = []

containers = []


def container_page():
    st.title("Cadastro de Container 📦")
    escolha_de_container = st.number_input(
        "Informe a Quantidade de Containers",
        min_value=1,
        step=1,
    )
    if st.button("Gerar Lista de Container"):
        with st.form("Cadastrar Container"):
            col1, col2 = st.columns(2)

            with col1:
                hbl_container = st.text_input(
                    "House BL Do Container",
                    key="hbl_container",
                )

            if st.form_submit_button("Gerar Lista"):
                st.session_state["containers"] = []

                for i in range(escolha_de_container):
                    container_data = {}

                    col1, col2, col3 = st.columns(3)

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
                        container_data["hbl_container"] = hbl_container
                        container_data["container"] = container
                        container_data["container_weight"] = container_weight

                    with col2:
                        container_tare = st.number_input(
                            f"Container Tare {i + 1}",
                            min_value=0.0,
                            format="%.3f",
                            key=f"container_tare_{i + 1}",
                        )
                        container_cbm = st.number_input(
                            f"Container CBM {i + 1}",
                            min_value=0.0,
                            format="%.3f",
                            key=f"container_cbm {i + 1}",
                        )
                        container_data["container_tare"] = container_tare
                        container_data["container_cbm"] = container_cbm

                    with col3:
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

                        container_data["hbl_container"] = hbl_container

                    st.markdown(
                        """
            <hr style="border: 2px solid #CD5C5C;">
            """,
                        unsafe_allow_html=True,
                    )

                    st.session_state["containers"].append(container_data)

    if st.button("Enviar Dados Container"):
        st.write(st.session_state["containers"])
        if len(st.session_state["containers"]) == []:
            st.error("Insira pelo menos um Container para enviar para o DataBase.")
        elif st.session_state["hbl_container"] is None:
            st.error("Informe o número do HBL.")
        else:
            # Exibe os dados dos contêineres cadastrados
            df_container = pd.DataFrame(st.session_state["containers"])

            st.success(
                "Container(s) enviado(s) com sucesso.",
            )

            df_container = pd.DataFrame(st.session_state["containers"])

            st.write(df_container[["hbl_container", "container", "container_type"]])
