import streamlit as st
import pandas as pd

df = pd.read_csv('patriot_league_per_game.csv')

st.title('Team Anaylzer')
st.subheader('Stats are per game')
df.drop(columns='Class', inplace=True)

Team = st.selectbox('Who is the upcoming opponet', df['Team'].unique().tolist())

tab3, tab2, tab1 = st.tabs(["Shooting", "Offense", "Defense"])

df_Sel_Team = df[df['Team'] == Team]

# Defensive stats
STL= df_Sel_Team[['Player','STL']].sort_values(by='STL', ascending=False)
DRB = df_Sel_Team[['Player','DRB']].sort_values(by='DRB', ascending=False)
BLK = df_Sel_Team[['Player','BLK']].sort_values(by='BLK', ascending=False)
PF = df_Sel_Team[['Player','PF']].sort_values(by='PF', ascending=False)

# Offensive stats
PTS= df_Sel_Team[['Player','PTS']].sort_values(by='PTS', ascending=False)
ORB= df_Sel_Team[['Player','ORB']].sort_values(by='ORB', ascending=False)
TOV= df_Sel_Team[['Player','TOV']].sort_values(by='TOV', ascending=False)
FG= df_Sel_Team[['Player','FG']].sort_values(by='FG', ascending=False)

# Shooting Stats
threePointper = df_Sel_Team[['Player','3P%']].sort_values(by='3P%', ascending=False)
twoPointper = df_Sel_Team[['Player','2P%']].sort_values(by='2P%', ascending=False)
threePoint = df_Sel_Team[['Player','3P']].sort_values(by='3P', ascending=False)
twoPoint = df_Sel_Team[['Player','2P']].sort_values(by='2P', ascending=False)

with tab1:
    st.bar_chart(data=STL.head(),x='Player', y='STL',x_label='Steal' ,horizontal=True, sort=False)
    st.bar_chart(data=DRB.head(),x='Player', y='DRB',x_label='Defensive Rebounds' ,horizontal=True, sort=False)
    st.bar_chart(data=BLK.head(),x='Player', y='BLK',x_label='Blocks' ,horizontal=True, sort=False)
    st.bar_chart(data=PF.head(),x='Player', y='PF',x_label='Personal Fouls' ,horizontal=True, sort=False)

with tab2:
    st.bar_chart(data=PTS.head(),x='Player', y='PTS',x_label='Points', horizontal=True, sort=False)
    st.bar_chart(data=ORB.head(),x='Player', y='ORB',x_label='Offensive Rebouds', horizontal=True, sort=False)
    st.bar_chart(data=TOV.head(),x='Player', y='TOV',x_label='Turnovers',horizontal=True, sort=False)
    st.bar_chart(data=FG.head(),x='Player', y='FG',x_label='Field Goals',horizontal=True, sort=False)

with tab3:
    st.bar_chart(data=threePointper.head(),x='Player', y='3P%',x_label='Three Pointer Percentage', horizontal=True, sort=False)
    st.bar_chart(data=twoPointper.head(),x='Player', y='2P%',x_label= 'Two Pointer Percantage',horizontal=True, sort=False)
    st.bar_chart(data=threePoint.head(),x='Player', y='3P',x_label='Three Pointers Made',horizontal=True, sort=False)
    st.bar_chart(data=twoPoint.head(),x='Player', y='2P',x_label='Two Pointers Made',horizontal=True, sort=False)






