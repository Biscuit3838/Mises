import streamlit as st
import random as r

st.title("MISES WOOOOOOO")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
number_dices = st.number_input("Nombre de dés", step=1)


def calculs(num_dices) :
    l = []
    for i in range(num_dices):
        l.append(r.randint(1, 10))
    l.sort()
    l_ori = l.copy()
    mises = 0
    for j in range(9):
        retour = calculs_start(l, 10 + j)
        mises += retour[0]
        l = retour[1]
    return mises, l_ori

def calculs_start(l, limit) :
    mises = 0
    l_cal = l.copy()
    cont = True
    while cont:
        retour = calculs_rec([], l_cal, limit)
        if (len(retour) == 0):
            cont = False
        else:
            mises += 1
            for i in retour:
                l_cal.remove(i)
    return mises, l_cal

def calculs_rec(curr, l, limit) :
    for i in range(len(l)):
        if sum(curr) + l[i] == limit:
            return curr + [l[i]]
        elif sum(curr) + l[i] < limit:
            l_iter = l.copy()
            l_iter.pop(i)
            retour = calculs_rec(curr + [l[i]], l_iter, limit)
            if len(retour) == 0:
                continue
            else:
                return retour
        else:
            return []
    return []

st.write("Number of dices : ", number_dices)
if st.button("Calculer"):
    retour = calculs(number_dices)
    mises = retour[0]
    liste = retour[1]
    st.write("Dés : ", liste)
    st.write("Mises : ", mises)