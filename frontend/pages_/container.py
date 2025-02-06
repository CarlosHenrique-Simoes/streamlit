import streamlit as st

if "hbl_container" not in st.session_state:
    st.session_state["hbl_container"] = None

if "containers" not in st.session_state:
    st.session_state["containers"] = []

def container_page():
    with st.form("Cadastrar Container"):
        col1, col2 = st.columns(2)

        with col2:
            hbl_container = st.text_input(
                "House BL Do Container",
            )

        with col1:
            escolha_de_container = st.number_input(
                "Informe a Quantidade de Containers",
                min_value=1,
                step=1,
            )
        if st.form_submit_button("Gerar Lista"):
            st.session_state["containers"] = escolha_de_container

            if st.session_state["containers"] < 1:
                st.error(
                    "Por favor, escolha a quantidade de containers.",
                )
                st.session_state["containers"] = None
            else:
                st.success(
                    f"Quantidade de containers: {st.session_state['containers']}",
                )
                col1, col2, col3 = st.columns(3)

                with col1:
                    container = st.text_input(
                        "Container",
                    ).upper()
                    container_weight = st.number_input(
                        "Gross Weight",
                        min_value=0.0,
                        format="%.3f",
                    )

                with col2:
                    container_tare = st.number_input(
                        "Container Tare",
                        min_value=0.0,
                        format="%.3f",
                    )
                    container_cbm = st.number_input(
                        "Container CBM",
                        min_value=0.0,
                        format="%.3f",
                    )

                with col3:
                    container_type = st.selectbox(
                        "Container Type",
                        ["22GP", "45GP"],
                        index=None,
                    )
                    ncm = st.multiselect(
                        "NCMs",
                        ncms,
                        default=None,
                    )
                if st.form_submit_button("Adicionar contêiner"):
                    container_data = {
                        "hbl_container": hbl_container,
                        "container": container,
                        "container_weight": container_weight,
                        "container_tare": container_tare,
                        "container_type": container_type,
                        "ncm": ncm,
                    }
                    containers.append(container_data)
                    st.success(
                        f"Contêiner {container} adicionado com sucesso.",
                    )

                    df_container = pd.DataFrame(containers)

                    df_container = df_container[
                        [
                            "hbl_container",
                            "container",
                            "container_type",
                        ]
                    ]

                    st.write(df_container)