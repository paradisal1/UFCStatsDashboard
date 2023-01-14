import streamlit as st

try:
    from database.DBInterface import DBInterface
except:
    from UFCStatsGUI.database.DBInterface import DBInterface


def wr(arg):
    st.write(arg)


def get_fighters_by_last_name(letter):
    import numpy as np

    db = DBInterface("database/ufc_silver")
    df = db.Pdf("combatants")
    drop_words = ["junior","de","dos","da","jr.","jr","júnior","júnior",None,"del","van","von",]

    cleaned = (
        df["F_NAME"]
        .str.split()
        .apply(lambda x: [x for x in x if x.lower() not in drop_words])
    )
    last_names = cleaned.apply(lambda x: x[-1]).str.lower()
    try:
        return df[
            df.index.isin(
                last_names[last_names.str.lower().str.startswith(letter.lower())].index
            )
        ].sort_values(by="LAST_NAME")["F_NAME"]
    except:
        return ["Select a letter to get started."]


x = get_fighters_by_last_name("A")
print(x)


def write_to_col(col, item, button=False):
    with col:
        if button:
            st.button(item)
        else:
            wr(item)


def set_variable(var, val):
    st.session_state[var] = val

def qr(df, col, val):
    return df[df[col] == val]
