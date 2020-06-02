# gry-kombinatoryczne
By uruchomić program
- upewnij się, że folder projektu to working directory
```
pip3 install pygame
python3 main.py N k min max [--depth D] [-h --help] [--bot-wait-time b] [--launch-test]
```
N - rozmiar zbioru liczb, na którym odbędzie się gra.  
k - długość monokolorowego ciągu arytmetycznego, który należy zbudować, by wygrać grę.  
min - dolny przedział zbioru, z którego losowane są liczby do gry.  
max - górny przedział zbioru, z którego losowane są liczby do gry.  
D - parametr decydujący o głębokości na jaką wejdzie komputer przy wyznaczaniu najlepszego ruchu korzystając z przeszukiwania alfa-beta; domyślnie 2. Uwaga: wysoki parametr znacznie wydłuża czas trwania gry.  
-h / --help - wyświetl opis argumentów i wyjdź z gry.  
b - parametr ustalający czas, który ma upłynąć między poszczególnymi ruchami graczy w sekundach; domyślnie 1.  
--launch-test - flaga określająca, czy należy uruchomić testy strategii. Wówczas odpalone zostanie 100 gier z podanymi parametrami, a po zakończeniu zostanie zwrócona liczba zwycięstw każdego gracza i średnia liczba ruchów w grze. Uwaga: ustawia parametr b na 0.  

By uruchomić testy jednostkowe:
```
python test.py
```
