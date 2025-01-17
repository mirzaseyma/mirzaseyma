import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükleme ve analiz etme fonksiyonu
def analyze_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        data.fillna(0, inplace=True)
        
        # İlgili sütunlar
        data = data[['Study_Hours_Per_Day', 'Sleep_Hours_Per_Day']]
        
        # Ortalama değerler
        average_sleep = data['Sleep_Hours_Per_Day'].mean()
        average_study = data['Study_Hours_Per_Day'].mean()
        
        # Dağılım grafikleri
        plt.hist(data['Sleep_Hours_Per_Day'], bins=10, alpha=0.7, color='blue', label='Uyku Saatleri')
        plt.title("Uyku Saatleri Dağılımı")
        plt.xlabel("Saat")
        plt.ylabel("Frekans")
        plt.show()
        
        plt.scatter(data['Study_Hours_Per_Day'], data['Sleep_Hours_Per_Day'], alpha=0.7, color='green')
        plt.title("Ders Çalışma ve Uyku Arasındaki İlişki")
        plt.xlabel("Ders Çalışma Süresi (saat)")
        plt.ylabel("Uyku Süresi (saat)")
        plt.show()
        
        return average_sleep, average_study
    except Exception as e:
        print(f"Veri seti analiz edilirken bir hata oluştu: {e}")
        return None, None

# Kullanıcıdan veri alma fonksiyonu
def get_user_input():
    try:
        user_sleep = float(input("Kaç saat uyuyorsunuz? "))
        user_study = float(input("Günde kaç saat ders çalışıyorsunuz? "))
        return user_sleep, user_study
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return None, None

# Karşılaştırma fonksiyonu
def compare_with_averages(user_sleep, user_study, average_sleep, average_study):
    if user_sleep is not None and user_study is not None:
        if user_sleep < average_sleep:
            print("Daha fazla uyumanız önerilir.")
        else:
            print("Uyku düzeniniz iyi görünüyor.")
        
        if user_study < average_study:
            print("Daha fazla ders çalışmanız önerilir.")
        else:
            print("Ders çalışma düzeniniz yeterli.")

# Ana fonksiyon
def main():
    file_path = r"C:\Users\v\Downloads\student_lifestyle_dataset.csv"  
    average_sleep, average_study = analyze_dataset(file_path)
    
    if average_sleep is not None and average_study is not None:
        user_sleep, user_study = get_user_input()
        compare_with_averages(user_sleep, user_study, average_sleep, average_study)

# Programı çalıştır
if __name__ == "__main__":
    main()
