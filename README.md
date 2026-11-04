# PathBinder

Yol şablonundaki parametreleri URL güvenli segmentlere çevirir.

## Girdi

template ve values. Parametreler {isim}.

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python pathbinder.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
"/v/a%2Fb"
```
