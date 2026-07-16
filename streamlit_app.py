import streamlit as st
import random as r

st.title("MISES WOOOOOOO")
st.write(
    "Tu entres un nombre. Tu valides. Tu cliques sur Calculer. Tu pleures parce que tu as min maxé et que tu as 0 mises."
)
number_dices = st.number_input("Nombre de dés", step=1)
explosion = st.checkbox("10 Explosent")
mises_Q = st.checkbox("Mises de 15")


def calculs(num_dices) :
    l = []
    for i in range(num_dices):
        l.append(r.randint(1, 10))
    l_ori = l.copy()
    l_reroll = []
    mises = 0
    if not mises_Q :
        k = 0
        while k < len(k) :
            if l[k] == 10 :
                if explosion :
                    while l[k] == 10 :
                        mises += 1
                        l[k] = r.randint(1, 10)
                        l_reroll.append(l[k])
                else :
                    mises += 1
                    l.pop(k)
                    k -= 1
            k += 1
    l.sort()
    l.reverse()
    if mises_Q :
        j = 15
        limit = 21
    else :
        j = 10
        limit = 18
    while j < limit:
        retour = calculs_start(l, j)
        mises += retour[0]
        l = retour[1]
        j += 1
    return mises, l_ori, l, l_reroll

def calculs_start(l, limit) :
    mises = 0
    l_cal = l.copy()
    i = 0
    pas_trouve = True
    while i < len(l_cal) :
        l_iter = l_cal.copy()
        l_iter.pop(i)
        retour = calculs_rec([l_cal[i]], l_iter, limit)
        if (len(retour) != 0):
            if pas_trouve :
                pas_trouve = False
                st.write("Mises de ", limit)
            mises += 1
            for j in retour:
                l_cal.remove(j)
            i = 0
            st.write("Mise : ", retour)
        else :
            i += 1
    return mises, l_cal

def calculs_rec(curr, l_ori, limit) :
    l = l_ori.copy()
    l.reverse()
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
    st.divider()
    retour = calculs(number_dices)
    mises = retour[0]
    liste = retour[1]
    liste_rest = retour[2]
    liste_reroll = retour[3]
    des = ""
    des_rest = ""
    for d in liste:
        des = des + str(d) + " "
    for d_r in liste_rest:
        des_rest = des_rest + str(d_r) + " "
    st.divider()
    st.write("Dés : ", des)
    st.write("Dés restants : ", des_rest)
    if explosion :
        des_roll = ""
        for d_roll in liste_reroll :
            des_roll = des_roll + str(d_roll) + " "
        st.write("Dés rerolls : ", des_roll)
    if mises_Q :
        st.write("Mises : ", mises, " x 2 = ", mises * 2)
    else :
        st.write("Mises : ", mises)