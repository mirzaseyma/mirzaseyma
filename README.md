# Öğrenci Yaşam Tarzı Analizi

Bu proje öğrencilere ait çalışma saatleri ve diğer yaşam tarzı faktörlerinin ilişkisini analiz eder.Program,görselleştirmeler ve ortalama değerler sunar ve kullanıcının girdiği verilere dayalı kişiselleştirilmiş önerilerde bulunur.

### İçindekiler

- kurulum
- kullanım
- fonksiyonlar
- örnek
- gereksinimler

### Kurulum

1. Depoyu klonlayın ya da kaynak kodunu yerel makinenize indirin.
2. Gerekli python kütüphanlerinizi yükleyin:
   > pip install pandas matplotlib
3. Kaggle'dan
   _student_lifestyle_dataset.csv_ dosyasını indirdiğinizden emin olun.Bu dosyayı proje klasörüne yerleştirebilir veya _file_path_ değişkenini indirdiğiniz dosyaya göre ayarlayabilirsiniz.

### Kullanım

#### programı çalıştırma

1. Terminal ya da komut istemcisini açın.
2. Proje klasörüne gidin.
3. Python script'ini çalıştırın:
   > python student_lifestyle_analysis.py
4. CSV dosyasından veri setini yükler.
   2.Uyku saatleri dağılımını ve ders çalışma ve uyku arasındaki ilişkiyi gösteren histogramlar ve dağılım grafikleri oluşturur.
5. Kullanıcıdan çalışma ve uyku saatlerini alır.
6. Veri setindeki ortalama değerlerle kullanıcının girdiklerini karşılaştırarak kişiselleştirilmiş önerilerde bulunur.

### Örnek

Kullanıcıdan, çalışma ve uyku saatlerini girmesini istenir:

> kaç saat uyuyorsunuz? 6

> Günde kaç saat ders çalışıyorsunuz? 4

kullanıcının girdiğine göre program şu geri bildirimi verecektir:

> uyku düzeniniz iyi görünüyor.

> Ders çalışma düzeniniz yeterli.

### Fonksiyonlar

### analyze_dataset(file_path)

- açıklama:
  Veri setini yükler ve analiz eder.Uyku saatleri dağılımı ve ders çalışma ile uyku arasındaki ilişkiyi gösteren histogramlar ve dağılım grafikleri oluşturur.
- Argümanlar:
  file_path (str) - CSV dosyasının yolu.
- Geri Dönüş Değeri: Ortalama uyku ve çalışma saatleri.

### get_user_input()

- Açıklama: Kullanıcıdan ders çalışma ve uyku saatlerini alır.
- Geri Dönüş Değeri: user_sleep (float), user_study (float) - Kullanıcının girdiği ders çalışma ve uyku saatleri.

### compare_with_averages(user_sleep, user_study, average_sleep, average_study)

- Açıklama: Kullanıcının uyku ve ders çalışma saatlerini, veri setindeki ortalama değerlerle karşılaştırır ve geri bildirimde bulunur.
- Argümanlar: user_sleep (float), user_study (float), average_sleep (float), average_study (float).

## Örnek

    file_path = "C:/path/to/student_lifestyle_dataset.csv"average_sleep, average_study = analyze_dataset(file_path)
    if average_sleep is not None and average_study is not None:
    user_sleep, user_study = get_user_input()
    compare_with_averages(user_sleep, user_study, average_sleep  average_study)

## Gereksinimler

- python 3.x
- kütüphanler:_pandas,matplotlib_
- gerekli kütüphanleri yüklemek için:
  > pip install pandas matplotlib

## Notlar

- Veri setinde en az şu sütunlar bulunmalıdır:
- _Study_Hours_Per_Day_
- _Sleep_Hours_Per_Day_

- Eksik değerlerle karşılaşırsanız,bunlar otomatik olarak 0 ile doldurulacaktır.

``

