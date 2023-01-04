import streamlit as st

from database.DBInterface import DBInterface


db = DBInterface("database/ufc_silver")
combatants = db.Pdf("split_bouts")
combatant_selector = st.selectbox(
    "Select a fighter", (combatants["F_FIRST"] + " " + combatants["F_LAST"]).unique()
)

f, l = combatant_selector.split(" ")
combatant = combatants[(combatants["F_FIRST"] == f) & (combatants["F_LAST"] == l)]
