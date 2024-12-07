
# Multiprogramming (Çok Programlılık)  
Birden fazla programın bellekte tutulup sıralı olarak çalıştırılmasıdır. Amaç, CPU ve kaynakları daha verimli kullanmaktır.  

---

# Multitasking (Çok Görevlilik)  
Birden fazla görevin aynı anda çalışıyormuş gibi görünmesini sağlar. CPU görevler arasında hızlı geçiş yapar.  

---

# Parallelism (Paralellik)  
Görevlerin aynı anda fiziksel olarak farklı çekirdeklerde çalıştırılmasıdır. Gerçek zamanlı eş zamanlı işlemler içerir.  

---

# Concurrency (Eşzamanlılık)  
Birden fazla işlemin bir zaman diliminde birlikte ilerlemesidir. Paralellikten farklı olarak tek çekirdekte de gerçekleşebilir.  

---

# Amdahl Law(Amdahl Yasası)  
Paralel işlem sistemlerinin maksimum performans kazancını belirleyen bir yasadır:  

> **Speedup = 1 / (S + (1 - S) / N)**  

- **S**: Seri olarak çalışması gereken kısım oranı.  
- **N**: Kullanılan işlemci veya çekirdek sayısı.  
Seri kısım ne kadar küçükse hızlanma o kadar fazla olur, ancak bir üst sınır vardır.  


