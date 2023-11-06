import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")

colors = [  "#89CFF0", "#FF69B4", "#FFD700", "#7B68EE", "#FF4500",
            "#9370DB", "#32CD32", "#8A2BE2", "#FF6347", "#20B2AA",
            "#FF69B4", "#00CED1", "#FF7F50", "#7FFF00", "#DA70D6"]

st.set_page_config(page_title="Shopping Trends Dataset", page_icon="👔")

st.image('./img/trends.png')

st.markdown("# Shopping Trends Dataset 👔")
st.markdown('---')



# Baca file CSV
df = pd.read_csv("shopping_trends_updated.csv")



# Tampilkan dataframe
st.write("Data Shopping Trends", df)
st.markdown('---')



# Menggunakan df.describe() dan menampilkan hasilnya sebagai tabel
st.write("Deskripsi Statistik")
st.dataframe(df.describe(), use_container_width=True)
st.markdown('---')



# Visualisasi menggunakan Matplotlib
st.write("Perbandingan Jenis Kelamin")
plt.figure(figsize=(20, 6))
ax = df["Gender"].value_counts().plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(('Male', 'Female'))

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25,
                p.get_height() + 1), ha='center', va='bottom', color='black')
    ax.tick_params(axis='both', labelsize=15)

plt.xlabel('Gender', weight="bold", color="#D71313", fontsize=14, labelpad=20)
plt.ylabel('Number of Occurrences', weight="bold",
            color="#D71313", fontsize=14, labelpad=20)

st.pyplot(plt)
st.markdown('---')



# Visualisasi diagram lingkaran menggunakan Matplotlib
st.write("Perbandingan Jenis Kelamin Menggunakan Diagram Pie")
fig, ax = plt.subplots(figsize=(20, 6))
counts = df["Gender"].value_counts()
explode = (0, 0.1)

ax.pie(counts, labels=counts.index, colors=colors, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 12})
ax.set_xlabel('Gender', weight="bold", color="#2F0F5D", fontsize=14, labelpad=20)
ax.axis('equal')

st.pyplot(fig)
st.markdown('---')



# Membuat histogram dengan kurva kepadatan
st.write("Histogram Distribusi Umur dengan Kurva Kepadatan")
fig, ax = plt.subplots(figsize=(20, 5))
ax.hist(df['Age'], bins=25, edgecolor='black', alpha=0.7, color='skyblue', density=True)
df['Age'].plot(kind='kde', color='red', ax=ax)

ax.set_xlabel('Age')
ax.set_ylabel('Count / Density')
ax.set_title('Age Distribution Histogram with Density Curve')
ax.legend(['Density Curve', 'Histogram'])

# Menampilkan gambar di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang untuk distribusi kategori
st.write("Grafik Pembelian Tertinggi Berdasarkan Kategori")
fig, ax = plt.subplots(figsize=(20, 6))
ax = df["Category"].value_counts().plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(['Clothing', 'Accessories', 'Footwear', 'Outerwear'])

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
    ax.tick_params(axis='both', labelsize=15)

ax.set_xlabel('Category', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



st.write("Grafik Pembelian Tertinggi Berdasarkan Kategori dengan Diagram Pie")
# Menghitung jumlah kategori
counts = df["Category"].value_counts()

# Persiapan data untuk pie chart
explode = (0, 0, 0, 0.1)
colors = ["#89CFF0", "#FF69B4", "#FFD700", "#7B68EE"]

# Membuat pie chart
fig, ax = plt.subplots(figsize=(20, 6))
ax.pie(counts, labels=counts.index, colors=colors, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 12})
ax.set_xlabel('Category', weight="bold", color="#2F0F5D", fontsize=14, labelpad=20)
ax.axis('equal')

# Menampilkan pie chart di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang horizontal
st.write("Grafik Pembelian Item Tertinggi")
fig, ax = plt.subplots(figsize=(16, 7))
item_counts = df["Item Purchased"].value_counts().sort_values(ascending=True)
item_counts.plot(kind='barh', color=sns.color_palette('tab20'), edgecolor='black')
ax.set_ylabel('Item Purchased', fontsize=16)
ax.set_xlabel('Number of Occurrences', fontsize=16)
ax.set_title('Item Purchased', fontsize=16)
ax.tick_params(axis='both', labelsize=16)

# Menampilkan grafik batang horizontal di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("10 Lokasi dengan Grafik Pembelian Tertinggi")
fig, ax = plt.subplots(figsize=(16, 6))
location_counts = df["Location"].value_counts()[:10].sort_values(ascending=False)
location_counts.plot(kind='bar', color=sns.color_palette('inferno'), edgecolor='black')
ax.set_xlabel('Location', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.tick_params(axis='x', labelrotation=0, labelsize=16)
plt.tight_layout()

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Grafik Pembelian Berdasarkan Ukuran")
fig = plt.figure(figsize = (20, 6))
ax = df["Size"].value_counts().plot(kind = 'bar', color = colors, rot = 0)
ax.set_xticklabels(('Medium', 'Large', 'Small', 'Extra Large'))

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha = 'center', va = 'bottom', color = 'black')
    ax.tick_params(axis = 'both', labelsize = 15)
plt.xlabel('Size', weight = "bold", color = "#D71313", fontsize = 14, labelpad = 20)
plt.ylabel('Number of Occurrences', weight = "bold", color = "#D71313", fontsize = 14, labelpad = 20);
# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Grafik Pembelian Berdasarkan Warna")
fig, ax = plt.subplots(figsize=(16, 6))
color_counts = df["Color"].value_counts()
top_10_colors = color_counts.nlargest(10).sort_values(ascending=True)
top_10_colors.plot(kind='barh', color=sns.color_palette('tab20'), edgecolor='black')
ax.set_xlabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Color', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.tick_params(axis='both', labelsize=16)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Data Pembelian Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(20, 6))
season_counts = df["Season"].value_counts()
season_order = ['Spring', 'Fall', 'Winter', 'Summer']
season_counts = season_counts.reindex(season_order)
season_counts.plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(season_order)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
ax.tick_params(axis='both', labelsize=15)
ax.set_xlabel('Season', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Perbandingan Pembeli Yang Berlangganan atau Tidak Berlangganan")
fig, ax = plt.subplots(figsize=(20, 6))
subscription_counts = df["Subscription Status"].value_counts()
subscription_order = ['No', 'Yes']
subscription_counts = subscription_counts.reindex(subscription_order)
subscription_counts.plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(subscription_order)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
ax.tick_params(axis='both', labelsize=15)
ax.set_xlabel('Subscription Status', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Grafik Perbandingan Jenis Metode Pembayaran")
fig, ax = plt.subplots(figsize=(20, 6))
payment_method_counts = df["Payment Method"].value_counts()
payment_method_order = ['Credit Card', 'Venmo', 'Cash', 'PayPal', 'Debit Card', 'Bank Transfer']
payment_method_counts = payment_method_counts.reindex(payment_method_order)
payment_method_counts.plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(payment_method_order)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
ax.tick_params(axis='both', labelsize=15)
ax.set_xlabel('Payment Method', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Membuat grafik batang
st.write("Grafik Perbandingan Jenis Metode Pengiriman Barang")
fig, ax = plt.subplots(figsize=(20, 6))
shipping_type_counts = df["Shipping Type"].value_counts()
shipping_type_order = ['Free Shipping', 'Standard', 'Store Pickup', 'Next Day Air', 'Express', '2-Day Shipping']
shipping_type_counts = shipping_type_counts.reindex(shipping_type_order)
shipping_type_counts.plot(kind='bar', color=colors, rot=0)
ax.set_xticklabels(shipping_type_order)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x() + 0.25, p.get_height() + 1), ha='center', va='bottom', color='black')
ax.tick_params(axis='both', labelsize=15)
ax.set_xlabel('Shipping Type', weight="bold", color="#D71313", fontsize=14, labelpad=20)
ax.set_ylabel('Number of Occurrences', weight="bold", color="#D71313", fontsize=14, labelpad=20)

# Menampilkan grafik batang di Streamlit
st.pyplot(fig)
st.markdown('---')



# Menggabungkan teks dari kolom "Frequency of Purchases"
st.write("Grafik Frekuensi Pembelian dengan Word Cloud")
text = " ".join(title for title in df["Frequency of Purchases"])

# Membuat word cloud
word_cloud = WordCloud(collocations=False, background_color='white').generate(text)

# Menampilkan word cloud di Streamlit
fig, ax = plt.subplots(figsize=(20, 5))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(fig)
st.markdown('---')



st.success('Barang apa yang paling sering dibeli?')
most_common_item = df['Item Purchased'].mode()[0]
st.header(most_common_item)
st.markdown('---')



st.success('Berapa jumlah total pembelian untuk setiap kategori?')
total_purchase_by_category = df.groupby('Category')['Purchase Amount (USD)'].sum()
st.dataframe(total_purchase_by_category, use_container_width=True)
st.markdown('---')



st.success('Berapa rata-rata rating ulasan untuk pelanggan pria dan pelanggan wanita secara terpisah?')
average_rating_male = df[df['Gender'] == 'Male']['Review Rating'].mean().round(1)
average_rating_female = df[df['Gender'] == 'Female']['Review Rating'].mean().round(1)
st.header('Male : ' + str(average_rating_male))
st.header('Female : ' + str(average_rating_female))
st.markdown('---')



st.success('Apa metode pembayaran yang paling umum digunakan oleh pelanggan?')
most_common_payment_method = df['Payment Method'].mode()[0]
st.header(most_common_payment_method)
st.markdown('---')



st.success('Berapa jumlah pembelian rata-rata (USD)?')
median_purchase_amount = df['Purchase Amount (USD)'].median()
st.header(median_purchase_amount)
st.markdown('---')



st.success('Berapa banyak pelanggan yang memilih Berlangganan?')
subscription_count = df[df['Subscription Status'] == 'Yes']['Customer ID'].count()
st.header(subscription_count)
st.markdown('---')



st.success('Musim apa yang paling umum untuk berbelanja?')
most_common_season = df['Season'].mode()[0]
st.header(most_common_season)
st.markdown('---')



st.success('Berapa jumlah total pembelian untuk setiap jenis kelamin?')
total_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].sum()
st.write("Total Purchase Amount by Gender:")
st.dataframe(total_purchase_by_gender, use_container_width=True)
st.markdown('---')



st.success('Berapa usia rata-rata pelanggan yang melakukan pembelian di musim panas?')
average_age_summer = df[df['Season'] == 'Summer']['Age'].mean()
average_age_summer_int = int(round(average_age_summer))
st.header(str(average_age_summer_int))
st.markdown('---')



st.success('Berapa banyak pelanggan yang menggunakan kode promo untuk pembelian mereka?')
promo_code_count = df[df['Promo Code Used'] == 'Yes']['Customer ID'].count()
st.header(promo_code_count)
st.markdown('---')



st.success('Berapa peringkat ulasan maksimum dan minimum dalam kumpulan data?')
max_review_rating = df['Review Rating'].max()
min_review_rating = df['Review Rating'].min()
st.write("Maximum Review Rating:", max_review_rating)
st.write("Minimum Review Rating:", min_review_rating)
st.markdown('---')



st.success('Jenis pengiriman apa yang paling umum untuk pelanggan dengan peringkat ulasan di atas 4?')
common_shipping_high_rating = df[df['Review Rating'] > 4]['Shipping Type'].mode()[0]
st.header(common_shipping_high_rating)
st.markdown('---')



st.success('Berapa banyak pelanggan yang telah melakukan lebih dari 30 pembelian sebelumnya?')
customers_above_30_previous_purchases = df[df['Previous Purchases'] > 30]['Customer ID'].count()
st.header(customers_above_30_previous_purchases)
st.markdown('---')



st.success('Berapa jumlah pembelian rata-rata untuk pelanggan yang telah melakukan lebih dari 30 pembelian sebelumnya?')
avg_purchase_above_30_previous_purchases = df[df['Previous Purchases'] > 30]['Purchase Amount (USD)'].mean()
st.header(avg_purchase_above_30_previous_purchases)
st.markdown('---')



st.success('Apa metode pembayaran paling umum bagi pelanggan yang berbelanja di musim dingin?')
total_purchase_free_shipping = df[df['Shipping Type'] == 'Free Shipping']['Purchase Amount (USD)'].sum()
st.header(total_purchase_free_shipping)
st.markdown('---')



st.success('Berapa jumlah pembelian rata-rata untuk pelanggan yang menggunakan diskon?')
avg_purchase_with_discount = df[df['Discount Applied'] == 'Yes']['Purchase Amount (USD)'].mean()
st.header(avg_purchase_with_discount)
st.markdown('---')



st.success('Kategori barang apa yang paling umum dibeli oleh pelanggan wanita dengan peringkat ulasan di bawah 3?')
common_category_low_rating_female = df[(df['Gender'] == 'Female') & (df['Review Rating'] < 3)]['Category'].mode()[0]
st.header(common_category_low_rating_female)
st.markdown('---')



st.success('Berapa rata-rata usia pelanggan yang melakukan pembelian dengan rating ulasan di atas 4 dan menggunakan kode promo?')
average_age_high_rating_promo = df[(df['Review Rating'] > 4) & (df['Promo Code Used'] == 'Yes')]['Age'].mean()
st.header(average_age_high_rating_promo)
st.markdown('---')



st.success('Berapa jumlah total pembelian untuk pelanggan di setiap lokasi?')
total_purchase_by_location = df.groupby('Location')['Purchase Amount (USD)'].sum()
st.dataframe(total_purchase_by_location, use_container_width=True)
st.markdown('---')



st.success("Berapakah distribusi frekuensi pada kolom 'Frekuensi Pembelian'?")
purchase_frequency_distribution = df['Frequency of Purchases'].value_counts()
st.dataframe(purchase_frequency_distribution, use_container_width=True)
st.markdown('---')



st.success('Berapa rata-rata jumlah pembelian untuk setiap warna barang?')
avg_purchase_by_color = df.groupby('Color')['Purchase Amount (USD)'].mean()
st.dataframe(avg_purchase_by_color, use_container_width=True)
st.markdown('---')



st.success('Berapa banyak pelanggan yang melakukan pembelian di setiap kategori?')
purchase_count_by_category = df['Category'].value_counts()
st.dataframe(purchase_count_by_category, use_container_width=True)
st.markdown('---')



st.success('Berapa total jumlah pembelian setiap ukuran item pakaian (XL, L, M, S) ?')
total_purchase_by_size = df[df['Category'] == 'Clothing'].groupby('Size')['Purchase Amount (USD)'].sum()
st.dataframe(total_purchase_by_size, use_container_width=True)
st.markdown('---')
