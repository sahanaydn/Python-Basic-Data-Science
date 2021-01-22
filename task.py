
#DİKKAT verilen veride kolon adları arası boşluklar '_' işareti ile doldurulmuştur.



import pandas as pd
import  matplotlib.pyplot as plt




veri =pd.read_csv("sat.csv")
#Bu veritabanında kaç okul izleniyor?
dizi=veri.School_Name.unique()
print(" \nBu veride birbirinden farklı " ,len(dizi)," okul vardır")

#Kaç okulda ilişkili test bilgisi yok?


eksik=0
for i in range(len(veri)):
    if veri.iloc[i].isnull().sum()>0:
        eksik=eksik+1
print(" \nBu veride ", eksik, "adet okulun verisi eksiktir ")

#Hangi okullar genel olarak en iyi puana sahiptir?
thebest=veri.groupby(["Critical_Reading_Mean", "Mathematics_Mean","Writing_Mean"])["School_Name"].max().tail(10)
print("\nGenel ortalama olarak en iyi puana sahip ilk 10 okul aşağıdaki tablodaki gibidir")
print("\n",thebest)


#Hangi okullar matematik ve eleştirel okuma arasında en farklı puanlara sahiptir?
veri2=veri["Critical_Reading_Mean"].sub(veri["Mathematics_Mean"],axis="index")
df=pd.DataFrame()
df['School_Name']=veri['School_Name']
df['divergent_scores']=abs(veri2)
print("\nMatematik ve eleştirel okuma arasında en farklı puanlara sahip ilk 10 okul aşağıdaki tablo gibidir")
print("\n",df.groupby(["divergent_scores"])["School_Name"].max().tail(10))

#verimizdeki boş değerleri veriye etki etmeyecek şekilde ortalama değerler ile doldurun.(seçtiğim soru)
print("\nVerimizdeki boş değerlere verinin kendi sütunun ortlama değerini atadığımız veri aşağıdaki gibidir")
veri3=veri.fillna(veri.mean())
print("\n",veri3)


#Bonus Görselleştirme (Critical Reading Mean ve Writing Mean değerleriyle bir grafik oluşturuldu. Düzenli bir
# orantı olmasada aralarında bir doğru orantı olduğu söylenebilir. Eksik veriler silinmiş ve
# değerler büyükten küçüğe sıralanmış halde grafik oluşturuldu )


df2=pd.DataFrame()
df2["Critical_Reading_Mean"]=veri["Critical_Reading_Mean"].sort_values()
df2["Writing_Mean"]=veri["Writing_Mean"].sort_values()
df2.dropna(inplace=True)
print(df2)


plt.plot(df2.Writing_Mean, df2.Critical_Reading_Mean)
plt.show()








