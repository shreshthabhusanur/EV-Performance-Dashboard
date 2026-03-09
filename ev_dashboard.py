import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EV Performance Analytics Dashboard")

# Sample EV data
data = {
    "Time":[0,1,2,3,4,5,6,7,8,9],
    "Speed_kmph":[0,15,30,45,55,60,65,70,75,80],
    "Battery_SOC":[100,98,96,94,92,90,88,86,84,82],
    "Power_kW":[0,10,20,35,40,45,50,55,60,65],
    "Distance_km":[0,0.5,1.2,2.5,4,6,8.5,11.5,15,19]
}

df = pd.DataFrame(data)

st.subheader("EV Dataset")
st.write(df)

# Speed Graph
st.subheader("Speed vs Time")
fig, ax = plt.subplots()
ax.plot(df["Time"], df["Speed_kmph"], marker="o")
ax.set_xlabel("Time")
ax.set_ylabel("Speed (km/h)")
st.pyplot(fig)

# Battery Graph
st.subheader("Battery SOC vs Time")
fig, ax = plt.subplots()
ax.plot(df["Time"], df["Battery_SOC"], marker="o")
ax.set_xlabel("Time")
ax.set_ylabel("Battery SOC (%)")
st.pyplot(fig)

# Power Graph
st.subheader("Power Consumption vs Time")
fig, ax = plt.subplots()
ax.plot(df["Time"], df["Power_kW"], marker="o")
ax.set_xlabel("Time")
ax.set_ylabel("Power (kW)")
st.pyplot(fig)

# Distance Graph
st.subheader("Distance vs Time")
fig, ax = plt.subplots()
ax.plot(df["Time"], df["Distance_km"], marker="o")
ax.set_xlabel("Time")
ax.set_ylabel("Distance (km)")
st.pyplot(fig)