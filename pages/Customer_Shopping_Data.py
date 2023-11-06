import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns



st.set_page_config(page_title="Customer Shopping Data", page_icon="🛒")

st.image('./img/mall.png')

st.markdown("# Customer Shopping Data 🛒")


# Baca file CSV
df = pd.read_csv("customer_shopping_data.csv")



# Tampilkan dataframe
st.write("Customer Shopping Data", df)
st.markdown('---')


# Menampilkan deskripsi data
st.write("Deskripsi Statistik Data")
st.dataframe(df.describe(include='object'),use_container_width=True)
st.markdown('---')



# Set ukuran plot
st.write("Perbandingan Jenis Kelamin Untuk Setiap Kategori")
a4_dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=a4_dims)

# Buat plot Seaborn
sns.countplot(ax=ax, x='category', hue='gender', data=df)
plt.title("Category on gender wise")

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)



df['age_group'] = pd.cut(x=df['age'], bins=[0, 16, 30, 45, 100], labels=['Child', 'Young Adults', 'Middle-aged Adults','Old-aged Adults'])
df[['age', 'age_group']].head(10)

df_age_group = df.groupby('age_group')['customer_id'].count().reset_index()
df_age_group.columns = ['age_group', 'quality']
df_age_group['percent'] = (df_age_group['quality'] / df_age_group['quality'].sum() *100).round(2)

df_category = df.groupby('category')['customer_id'].count().reset_index()
df_category.columns = ['category', 'quality']
df_category['percent'] = (df_category['quality'] / df_category['quality'].sum() *100).round(2)

df_payment_method = df.groupby('payment_method')['customer_id'].count().reset_index()
df_payment_method.columns = ['payment_method', 'quality']
df_payment_method['percent'] = (df_payment_method['quality'] / df_payment_method['quality'].sum() *100).round(2)

df_shopping_mall = df.groupby('shopping_mall')['customer_id'].count().reset_index()
df_shopping_mall.columns = ['shopping_mall', 'quality']
df_shopping_mall['percent'] = (df_shopping_mall['quality'] / df_shopping_mall['quality'].sum() *100).round(2)


# Set ukuran plot
fig, ax = plt.subplots(figsize=(16, 6))
colors = sns.color_palette("Set2")

# Fungsi untuk menampilkan plot pie
def plot_pie(df, title, label_column, percent_column):
    ax.pie(df[percent_column], labels=df[label_column].tolist(), colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.5))
    ax.set_title(title, pad=20, fontsize=15)
    ax.axis('equal')

st.markdown('---')
# Menampilkan setiap plot pie secara terpisah
plot_pie(df_age_group, 'Distribution of Values by Age Group', 'age_group', 'percent')
st.pyplot(fig)
st.markdown('---')

plot_pie(df_category, 'Distribution of Values by Category', 'category', 'percent')
st.pyplot(fig)
st.markdown('---')

plot_pie(df_payment_method, 'Distribution of Values by Payment Method', 'payment_method', 'percent')
st.pyplot(fig)
st.markdown('---')

plot_pie(df_shopping_mall, 'Distribution of Values by Shopping Mall', 'shopping_mall', 'percent')
st.pyplot(fig)
st.markdown('---')



# Menghitung jumlah pengamatan untuk setiap kategori 'Age_Range'
st.write("Berapa Persentase atau Distribusi Usianya?")
cut_labels_4 = ['10-20', '21-30', '31-50', '51-70']
cut_bins = [0, 20, 30, 50, 70]
df["Age_Range"] = pd.cut(df['age'], bins=cut_bins, labels=cut_labels_4)
age_range_counts = df['Age_Range'].value_counts().sort_index()

# Membuat plot pie menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(16, 6))
ax.pie(age_range_counts, labels=age_range_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
ax.set_title('Ages of All Customers')

# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)
st.markdown('---')



st.success('Apa Kategori Yang Paling Banyak Dibeli?')

# Menghitung frekuensi kemunculan setiap item dalam kolom "category"
category_counts = df['category'].value_counts()

# Item yang paling sering dibeli
most_purchased_item = category_counts.idxmax()

# Membuat DataFrame untuk menampilkan kategori dan jumlah angka
category_counts_df = pd.DataFrame({'Kategori': category_counts.index, 'Jumlah': category_counts.values})

st.write("Item yang ada dalam kolom 'category' dan jumlah angka masing-masing:")
st.dataframe(category_counts_df, use_container_width=True)

st.write(f"Item yang paling sering dibeli adalah '{most_purchased_item}'.")
st.markdown('---')



st.success('Jenis Pembayaran Paling Sering Digunakan?')

# Menghitung frekuensi kemunculan setiap jenis pembayaran
payment_counts = df['payment_method'].value_counts()

# Jenis pembayaran yang paling sering digunakan
most_common_payment = payment_counts.idxmax()

st.write("Jenis pembayaran yang paling sering digunakan:")
st.write(most_common_payment)
st.markdown('---')



st.success('Shopping Mall Dengan Kunjungan Terbanyak?')

# Menghitung jumlah pengunjung di setiap shopping mall
visitor_counts = df['shopping_mall'].value_counts()

# Shopping mall dengan jumlah pengunjung terbanyak
most_visited_mall = visitor_counts.idxmax()

most_visited_count = visitor_counts.max()

st.write(f"Shopping mall dengan jumlah pengunjung terbanyak adalah '{most_visited_mall}' dengan jumlah pengunjung sebanyak {most_visited_count} orang.")
st.markdown('---')



st.success('Pembelian Paling Mahal?')

# Mencari pembelian paling mahal
max_purchase = df[df['price'] == df['price'].max()]

if not max_purchase.empty:
    customer_id = max_purchase['customer_id'].values[0]
    shopping_mall = max_purchase['shopping_mall'].values[0]
    max_price = max_purchase['price'].values[0]

    st.write(f"Pembelian paling mahal adalah sebesar ${max_price} oleh Customer ID {customer_id}, di shopping mall '{shopping_mall}'.")
else:
    st.write("Data pembelian kosong atau ada kesalahan dalam analisis.")
st.markdown('---')