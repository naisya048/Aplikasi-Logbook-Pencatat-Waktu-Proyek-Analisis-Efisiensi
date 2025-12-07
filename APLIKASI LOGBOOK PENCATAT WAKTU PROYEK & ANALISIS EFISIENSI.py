import streamlit as st
import pandas as pd
import datetime
import os
import altair as alt
import csv
import os
import matplotlib.pyplot as plt

log_file = "logbook.csv"

# Buat file CSV jika belum ada
if not os.path.exists(log_file):
    with open(log_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Hari", "Proyek", "Durasi (menit)"])


def tambah_log():
    print("\nPilih Hari Aktivitas:")
    for i in range(1, 8 + 1):
        print(f"{i}. Hari {i}")

    hari = input("Masukkan pilihan hari (1-8): ")

    proyek = input("Masukkan nama proyek/aktivitas: ")
    durasi = float(input("Masukkan durasi pengerjaan (menit): "))

    # Simpan ke file
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([hari, proyek, durasi])

    print("Data berhasil disimpan!\n")


def tampilkan_log():
    print("\n=== DATA LOGBOOK ===")
    with open(log_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


def grafik_durasi():
    hari = []
    durasi = []

    with open(log_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            hari.append("Hari " + row[0])
            durasi.append(float(row[2]))

    if len(durasi) == 0:
        print("Belum ada data untuk ditampilkan.")
        return

    plt.figure()
    plt.bar(hari, durasi)
    plt.title("Grafik Durasi Pekerjaan per Hari")
    plt.xlabel("Hari")
    plt.ylabel("Durasi (menit)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Menu Utama
while True:
    print("=== APLIKASI LOGBOOK PENCATAT WAKTU PROYEK ===")
    print("1. Tambah Log Aktivitas")
    print("2. Tampilkan Logbook")
    print("3. Tampilkan Grafik Durasi")
    print("4. Keluar")

    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        tambah_log()
    elif menu == "2":
        tampilkan_log()
    elif menu == "3":
        grafik_durasi()
    elif menu == "4":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid!\n")
