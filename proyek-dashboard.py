import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk menampilkan total penggunaan sepeda berdasarkan hari kerja dan akhir pekan
def tampilan_penyewaan_cuaca(hour_df):
    hour_df.groupby(by="weathersit")["cnt"].sum().sort_values(ascending=False)
    # Membuat mapping untuk weathersit
    weather_mapping = {
        1: "Clear",
        2: "Mist",
        3: "Light Snow",
        4: "Heavy Rain"
    }

    # Mengganti nilai weathersit dengan label deskriptif
    hour_df['weathersit'] = hour_df['weathersit'].replace(weather_mapping)

    # Mengelompokkan data berdasarkan kondisi cuaca (weathersit), menghitung total penyewaan (cnt), dan mengurutkan
    weather_rentals = hour_df.groupby(by="weathersit")["cnt"].sum().sort_values(ascending=False)

    # Streamlit Title
    st.title('Total Penyewaan Sepeda Berdasarkan Cuaca')

    # Membuat plot bar chart
    st.subheader('Visualisasi Penyewaan Berdasarkan Kondisi Cuaca')

    # Create a matplotlib figure
    plt.figure(figsize=(10, 6))
    sns.barplot(x=weather_rentals.index, y=weather_rentals.values, palette="tab10")

    # Menambahkan judul dan label sumbu
    plt.title("Total Penyewaan Sepeda Berdasarkan Cuaca", fontsize=16)
    plt.xlabel("Kondisi Cuaca", fontsize=12)
    plt.ylabel("Total Rental", fontsize=12)

    # Menampilkan plot di Streamlit
    st.pyplot(plt)

def tampilan_register_casual(hour_df):
    total_registered = hour_df["registered"].sum()
    total_casual = hour_df["casual"].sum()
    # Buat DataFrame untuk total pengguna
    data = {
        'User Type': ['Registered', 'Casual'],
        'Total': [total_registered, total_casual]
    }
    users_df = pd.DataFrame(data)

    # Judul halaman
    st.title('Perbandingan Penyewa Sepeda: Registered vs Casual')

    # Deskripsi singkat
    st.write("""
    Berikut ini adalah perbandingan total penyewa sepeda antara pengguna **terdaftar (registered)** dan pengguna **kasual (casual)**. 
    Grafik bar di bawah menunjukkan total penyewa berdasarkan tipe pengguna.
    """)

    # Buat bar chart menggunakan matplotlib dan seaborn
    plt.figure(figsize=(8, 5))
    colors = ['#2ca02c', '#2ca02c']  # Warna hijau tua
    sns.barplot(x='User Type', y='Total', data=users_df, palette=colors)

    # Memberi judul dan label sumbu
    plt.title('Total Penyewa Sepeda: Registered vs Casual', fontsize=16)
    plt.xlabel('Tipe Penyewa', fontsize=12)
    plt.ylabel('Total Penyewa', fontsize=12)

    # Menampilkan plot di Streamlit
    st.pyplot(plt)

def tampilan_jenis_hari(day_df):
    average_rentals = day_df.groupby(["holiday", "workingday"])["cnt"].mean().reset_index()
    # Mengonversi kolom boolean menjadi string agar mudah dimengerti
    average_rentals['holiday'] = average_rentals['holiday'].map({0: 'Working Day', 1: 'Holiday'})
    average_rentals['workingday'] = average_rentals['workingday'].map({0: 'Not Working', 1: 'Working'})

    # Gabungkan kolom untuk label pie chart
    average_rentals['label'] = average_rentals['holiday'] + " & " + average_rentals['workingday']

    # Ambil nilai rata-rata penyewaan untuk setiap kombinasi
    sizes = average_rentals['cnt']

    # Judul halaman
    st.title('Rata-rata Penyewaan Sepeda Berdasarkan Jenis Hari')

    # Deskripsi singkat
    st.write("""
    Grafik pie chart berikut menggambarkan perbandingan rata-rata penyewaan sepeda berdasarkan 
    hari kerja, hari libur, dan apakah itu merupakan hari kerja aktif atau tidak aktif.
    """)

    # Buat pie chart menggunakan matplotlib
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=average_rentals['label'], autopct='%1.1f%%', startangle=90, 
            colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])

    # Menambahkan judul
    plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Jenis Hari', fontsize=16)

    # Menampilkan plot dalam Streamlit
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    st.pyplot(plt)
    
def tampilan_rental_bulanan(day_df):
    # Ekstrak bulan dan tahun
    day_df['year'] = day_df['dteday'].dt.year
    day_df['month'] = day_df['dteday'].dt.month

    # Agregasi data penyewaan per bulan
    monthly_rentals = day_df.groupby(['year', 'month']).agg({
        'casual': 'sum',
        'registered': 'sum'
    }).reset_index()
    # Buat kolom 'date' untuk x-axis dengan hari pertama setiap bulan
    monthly_rentals['date'] = pd.to_datetime(monthly_rentals[['year', 'month']].assign(day=1))

    # Judul halaman
    st.title('Perkembangan Penyewaan Sepeda Bulanan: Registered vs Casual Users')

    # Deskripsi singkat
    st.write("""
    Grafik berikut menunjukkan perkembangan jumlah penyewaan sepeda bulanan untuk 
    pengguna terdaftar dan pengguna kasual. Data ditampilkan untuk setiap bulan selama dua tahun.
    """)

    # Buat line chart menggunakan matplotlib
    plt.figure(figsize=(12, 6))

    # Menggambar garis untuk pengguna terdaftar
    plt.plot(monthly_rentals['date'], monthly_rentals['registered'], marker='o', label='Registered Users', color='blue')

    # Menggambar garis untuk pengguna kasual
    plt.plot(monthly_rentals['date'], monthly_rentals['casual'], marker='o', label='Casual Users', color='green')

    # Menambahkan judul dan label
    plt.title('Catatan Rental Sepeda Bulanan: Registered vs Casual Users', fontsize=16)
    plt.xlabel('Tanggal', fontsize=12)
    plt.ylabel('Total Rental', fontsize=12)

    # Menambahkan legenda
    plt.legend()

    # Menampilkan grid
    plt.grid()

    # Mengatur layout agar tidak terpotong
    plt.tight_layout()

    # Menampilkan plot dalam Streamlit
    st.pyplot(plt)
    

# Fungsi untuk menampilkan halaman Beranda
def show_homepage():
    st.subheader("Dashboard Data Penyewaan Sepeda")
    st.write(""" 
    Dashboard ini bertujuan untuk memberikan gambaran tentang data penyewaan sepeda dari tahun 2011 - 2013
    """)

    # Membaca dataset day.csv
    day_df = pd.read_csv('sewaSepeda/day.csv')
    st.write("### Data day.csv")
    st.dataframe(day_df)

    # Membaca dataset hour.csv
    hour_df = pd.read_csv('sewaSepeda/hour.csv')
    st.write("### Data hour.csv")
    st.dataframe(hour_df)

# Fungsi untuk menampilkan kesimpulan dengan pertanyaan dan jawaban
def show_conclusion():

    st.write(""" 
    **1: Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?**
    """)
    st.markdown(""" 
    <p style='font-size: 14px;'>
    Berdasarkan data yang telah diolah dan dianalisis, semakin baik cuaca makan penyewaan sepeda semakin banyak. Hal ini ditunjukan dengan penyewaan terbanyak ada di cuaca (Clear, Few clouds, Partly cloudy, Partly cloudy) sedangkan penyewaan terendah ada di cuaca (Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog)
    </p>
    """, unsafe_allow_html=True)
    

    st.write(""" 
    **2. Adakah perbedaan jumlah penyewa casual dan ter-registrasi?**
    """)
    st.markdown(""" 
    <p style='font-size: 14px;'>
    Perbedaan terlihat ketika membandingkan data jumlah total penyewa kasual dan penyewa yang ter-registrasi. Dari data yang diambil, jumlah registered users berbeda empat kali lipat dibandingkan casual users
    </p>
    """, unsafe_allow_html=True)
    
    st.write(""" 
    **3. Apakah terdapat perbedaan pola penyewaan berdasarkan hari kerja dan akhir pekan?**
    """)
    st.markdown(""" 
    <p style='font-size: 14px;'>
    Berdasarkan data penyewa terbesar terjadi di hari kerja, disusul di hari kerja tetapi libur, dan yang terakhir di hari libur (bukan hari kerja)
    </p>
    """, unsafe_allow_html=True)
    
    st.write(""" 
    **4. Bagaimana perkembangan penyewaan sepeda per bulan dalam range dua tahun berdasarkan jenis penyewa?**
    """)
    st.markdown(""" 
    <p style='font-size: 14px;'>
    Terjadi kenaikan dan penurunan penyewa setiap bulan, dimana titik puncak penyewa ada di bulan September 2012
    </p>
    """, unsafe_allow_html=True)
    
    

# Main function untuk menjalankan Streamlit
def main():
    # Membaca dataset
    day_df = pd.read_csv('sewaSepeda/day.csv')
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df = pd.read_csv('sewaSepeda/hour.csv')
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    

    st.sidebar.title("Navigasi")
    option = st.sidebar.selectbox(
        'Pilih Halaman',
        ['Beranda', 
         'Data Penyewaan Sepeda Berdasar Cuaca', 
         'Total Penyewaan Berdasarkan Jenis Penyewa',
         'Rata Rata Penyewaan Berdasarkan Jenis Hari',
         'Catatan Rental Sepeda Bulanan',
         'Kesimpulan']
    )

    # Halaman Beranda
    if option == 'Beranda':
        show_homepage()
    elif option == 'Data Penyewaan Sepeda Berdasar Cuaca':
        st.subheader("Data Penyewaan Sepeda Berdasar Cuaca")  # Judul halaman kedua
        tampilan_penyewaan_cuaca(hour_df)
    elif option == 'Total Penyewaan Berdasarkan Jenis Penyewa':
        st.subheader("Total Penyewaan Berdasarkan Jenis Penyewa")  # Judul halaman ketiga
        tampilan_register_casual(hour_df)
    elif option == 'Rata Rata Penyewaan Berdasarkan Jenis Hari':
        st.subheader("Rata Rata Penyewaan Berdasarkan Jenis Hari")  # Judul halaman keempat
        tampilan_jenis_hari(day_df)
    elif option == 'Catatan Rental Sepeda Bulanan':
        st.subheader("Catatan Rental Sepeda Bulanan")  # Judul halaman kelima
        tampilan_rental_bulanan(day_df)
    elif option == 'Kesimpulan':
        st.subheader("Kesimpulan")  # Judul halaman keenam
        show_conclusion()

# Jalankan aplikasi streamlit
if __name__ == "__main__":
    main()
