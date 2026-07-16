import streamlit as st
import random as r

st.title("MISES WOOOOOOO")
st.write(
    "Tu entres un nombre. Tu valides. Tu cliques sur Calculer. Tu pleures parce que tu as min maxé et que tu as 0 mises."
)
number_dices = st.number_input("Nombre de dés", step=1)


def calculs(num_dices) :
    l = []
    for i in range(num_dices):
        l.append(r.randint(1, 10))
    l.sort()
    l.reverse()
    l_ori = l.copy()
    mises = 0
    for i in l :
        if i == 10 :
            l.remove(i)
            mises += 1
    j = 0
    while j < 9:
        st.write("Cherche : ", 10 + j)
        retour = calculs_start(l, 10 + j)
        mises += retour[0]
        l = retour[1]
        j += 1
    return mises, l_ori, l

def calculs_start(l, limit) :
    mises = 0
    l_cal = l.copy()
    i = 0
    while i < len(l_cal) :
        l_iter = l_cal.copy()
        l_iter.pop(i)
        retour = calculs_rec([l_cal[i]], l_iter, limit)
        if (len(retour) != 0):
            mises += 1
            for j in retour:
                l_cal.remove(j)
            i = 0
            st.write("Mise : ", retour)
        else :
            i += 1
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

if st.button("Calculer"):
    retour = calculs(number_dices)
    mises = retour[0]
    liste = retour[1]
    liste_rest = retour[2]
    des = ""
    des_rest = ""
    for d in liste:
        des = des + str(d) + " "
    for d_r in liste_rest:
        des_rest = des_rest + str(d_r) + " "
    st.write("Dés : ", des)
    st.write("Dés restants :", des_rest)
    st.write("Mises : ", mises)