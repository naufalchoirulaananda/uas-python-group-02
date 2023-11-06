import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
import math



st.set_page_config(page_title="Job Offers Software Engineer in Poland", page_icon="💼")

st.image('./img/software.png')

st.markdown("# Job Offers Software Engineer in Poland 💼")
st.markdown('---')



# Baca file CSV
df = pd.read_csv("Job Offers for Software Engineers in Poland.csv")



# Tampilkan dataframe
st.write("Job Offers for Software Engineers", df)
st.markdown('---')


# Menghitung statistik
tech_stats = df.groupby(['technology'])['company'].count().reset_index().sort_values('company', ascending=False)
loc_stats = df.groupby(['location'])['company'].count().reset_index().sort_values('company', ascending=False)
seniority_stats = df.groupby(['seniority'])['company'].count().reset_index().sort_values('company', ascending=False)
company_stats = df.groupby(['company size'])['company'].count().reset_index().sort_values('company size', ascending=False)

# Menggunakan Streamlit untuk menampilkan pie charts
st.set_option('deprecation.showPyplotGlobalUse', False)  # Untuk menghindari pesan peringatan
st.title("STATISTIK DATA")
st.write('Dalam analisis pasar kerja rekayasa perangkat lunak di Polandia, kami menggunakan diagram lingkaran untuk memberikan wawasan tentang beberapa aspek kunci. Berikut adalah ringkasan dari hasil analisis:')

# Chart Teknologi
st.subheader("Teknologi")
narrative = """
<div style="text-align: justify;">
    Diagram lingkaran ini menggambarkan popularitas berbagai teknologi di antara semua tawaran pekerjaan. Hasilnya menunjukkan bahwa Java, JavaScript, C#, dan Python adalah teknologi paling populer. Dalam kenyataannya, teknologi-teknologi ini mencakup tiga perempat dari semua penawaran pekerjaan. Hal ini menggambarkan tren yang dominan dalam industri rekayasa perangkat lunak di Polandia.
</div>
"""

st.markdown(narrative, unsafe_allow_html=True)
st.markdown('')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(tech_stats['company'], labels=tech_stats['technology'], colors=plt.cm.tab20b(range(len(tech_stats))))
plt.title("Teknologi")
st.pyplot(fig)

# Chart Lokasi
st.subheader("Lokasi")
narrative = """
<div style="text-align: justify;">
    Diagram lingkaran ini mencerminkan distribusi tawaran pekerjaan di berbagai lokasi di Polandia, termasuk jumlah tawaran pekerjaan jarak jauh. Temuan menarik adalah bahwa lebih dari setengah tawaran pekerjaan merupakan posisi jarak jauh, menunjukkan perubahan signifikan dalam dinamika kerja yang dipengaruhi oleh perkembangan teknologi. Di sisi lain, untuk posisi on-site atau hybrid, distribusinya tampaknya berkaitan dengan ukuran kota. Ini menggambarkan fleksibilitas dalam lokasi kerja yang ditawarkan oleh berbagai perusahaan.
</div>
"""

st.markdown(narrative, unsafe_allow_html=True)
st.markdown('')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(loc_stats['company'], labels=loc_stats['location'], colors=plt.cm.tab20b(range(len(loc_stats))))
plt.title("Lokasi")
st.pyplot(fig)

# Chart Senioritas
st.subheader("Senioritas")
narrative = """
<div style="text-align: justify;">
    Diagram lingkaran ini menyoroti permintaan kandidat dengan tingkat senioritas yang berbeda. Hasil analisis menunjukkan bahwa mayoritas tawaran pekerjaan ditujukan untuk posisi tingkat menengah dan senior. Sementara itu, posisi junior dan ahli relatif kurang umum. Hal ini mencerminkan tingkat pengalaman dan keahlian yang dibutuhkan dalam pasar kerja rekayasa perangkat lunak Polandia.
</div>
"""

st.markdown(narrative, unsafe_allow_html=True)
st.markdown('')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(seniority_stats['company'], labels=seniority_stats['seniority'], colors=plt.cm.tab20b(range(len(seniority_stats))))
plt.title("Senioritas")
st.pyplot(fig)

# Chart Ukuran Perusahaan
st.subheader("Ukuran Perusahaan")
narrative = """
<div style="text-align: justify;">
    Diagram lingkaran ini menunjukkan jumlah tawaran pekerjaan dari perusahaan dengan ukuran yang berbeda. Hasil analisis menunjukkan bahwa hampir setengah tawaran pekerjaan berasal dari perusahaan dengan beberapa ratus karyawan, sedangkan sekitar seperempat tawaran berasal dari perusahaan kecil dengan kurang dari 100 karyawan. Ini mencerminkan keragaman dalam ukuran perusahaan yang aktif dalam industri rekayasa perangkat lunak di Polandia.
</div>
"""

st.markdown(narrative, unsafe_allow_html=True)
st.markdown('')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(company_stats['company'], labels=company_stats['company size'], colors=plt.cm.tab20b(range(len(company_stats))))
plt.title("Ukuran Perusahaan")
st.pyplot(fig)


# Analisis Lokasi Pekerjaan
st.title("Analisis Lokasi Pekerjaan")
location_stats = df['location'].value_counts()
st.bar_chart(location_stats)

# Analisis Senioritas Pekerjaan
st.title("Analisis Senioritas Pekerjaan")
seniority_stats = df['seniority'].value_counts()
st.bar_chart(seniority_stats)

# Analisis Ukuran Perusahaan
st.title("Analisis Ukuran Perusahaan")
company_size_stats = df['company size'].value_counts()
st.bar_chart(company_size_stats)

# Analisis Kombinasi Gaji B2B dan Gaji Penuh Waktu
st.title("Analisis Kombinasi Gaji B2B dan Gaji Penuh Waktu")
df['salary_difference'] = df['salary employment max'] - df['salary b2b min']
st.line_chart(df['salary_difference'])

# Analisis Teknologi Tertentu
st.title("Analisis Teknologi Tertentu")
selected_technology = st.selectbox("Pilih Teknologi:", df['technology'].unique())
tech_stats = df[df['technology'] == selected_technology]['company'].value_counts()
st.bar_chart(tech_stats)

# Hitung pekerjaan remote
remote_count = df[df['location'] == 'Remote']['location'].count()

# Hitung pekerjaan on-site (Non Remote)
on_site_count = df[df['location'] != 'Remote']['location'].count()

st.title("Analisis Remote vs. On-site")
st.bar_chart({'Remote': [remote_count], 'Non Remote': [on_site_count]})
st.markdown('---')



st.success('Perusahaan Dengan Jumlah Karyawan Senior Terbanyak?')
# Filter df hanya untuk seniority = "senior"
senior_data = df[df['seniority'] == 'senior']

# Group df berdasarkan perusahaan dan hitung jumlah seniority "senior" untuk setiap perusahaan
company_seniority_counts = senior_data.groupby('company')['seniority'].count()

# Temukan perusahaan dengan jumlah seniority "senior" terbanyak
max_seniority_company = company_seniority_counts.idxmax()

# Jumlah seniority "senior" terbanyak
max_seniority_count = company_seniority_counts.max()

st.write(f"Perusahaan dengan seniority 'senior' terbanyak adalah {max_seniority_company} dengan jumlah {max_seniority_count} Karyawan.")
st.markdown('---')



st.success('Technology "Bahasa Pemrograman" Yang Paling Banyak Digunakan?')
# Menghitung frekuensi kemunculan setiap teknologi
technology_counts = df['technology'].value_counts()

# Teknologi dengan frekuensi tertinggi
most_used_technology = technology_counts.idxmax()

# Jumlah penggunaan teknologi tertinggi
most_used_technology_count = technology_counts.max()

st.write(f"Teknologi yang paling banyak digunakan adalah '{most_used_technology}' dengan jumlah penggunaan sebanyak {most_used_technology_count} kali.")
st.markdown('---')



st.success('Jenis Location Paling Banyak?')
# Menghitung frekuensi kemunculan setiap jenis lokasi
location_counts = df['location'].value_counts()

# Jenis lokasi dengan frekuensi tertinggi
most_common_location = location_counts.idxmax()

# Jumlah kemunculan jenis lokasi tertinggi
most_common_location_count = location_counts.max()

st.write(f"Jenis lokasi yang paling banyak digunakan adalah '{most_common_location}' dengan jumlah kemunculan sebanyak {most_common_location_count} kali.")
st.markdown('---')