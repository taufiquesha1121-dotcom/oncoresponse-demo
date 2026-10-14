import streamlit as st
import pandas as pd

st.set_page_config(page_title="OncoResponse", layout="wide")

st.title("OncoResponse")
st.caption("Research prototype: gene-expression based pCR prediction in breast cancer. Not for clinical use.")

tab1, tab2, tab3 = st.tabs(["Results", "Figures", "Top genes"])

with tab1:
    st.subheader("Model performance")
    perf = pd.read_csv("performance_summary.csv")
    st.dataframe(perf, use_container_width=True)
    st.markdown(
        "**Main point:** Elastic net validation ROC-AUC is 0.750, close to its nested CV "
        "AUC of 0.758. The in-sample AUC of 0.892 is optimistic and should not be quoted."
    )

with tab2:
    st.subheader("Evaluation")
    st.image("evaluation.png")
    st.subheader("Feature stability")
    st.image("stability.png")

with tab3:
    st.subheader("Gene selection ranking")
    genes = pd.read_csv("fdr_gene_ranking.csv")
    st.dataframe(genes.head(20), use_container_width=True)
