import streamlit as st
import random

from database.DBInterface import DBInterface
from apputils.utils import wr, get_fighters_by_last_name, set_variable
from app.model import FighterDisplay


silver_db = DBInterface("database/ufc_silver")
df = silver_db.Pdf("combatants", close=True)

letters = [chr(i) for i in range(65, 91)]

st.subheader("Find a fighter by their last name")

with st.container():
    cols = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = st.columns(26)


for letter, button in zip(letters, cols):
    button.button(letter, key=letter, args=('chosen_letter', letter), on_click=set_variable)


fighters = get_fighters_by_last_name(st.session_state.chosen_letter)
col1, col2 = st.columns([1, 3])


if fighters is not None:
    for fighter in fighters:
        col1.button(fighter, key=fighter + str(random.randint(0, 1000)), args=('chosen_fighter',fighter), on_click=set_variable)


col2.write(st.session_state.chosen_fighter)


FD = FighterDisplay()
