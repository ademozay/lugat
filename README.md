# Lügat

`TDK Güncel Türkçe Sözlük` için komut satırı arabirimi.

![ön izleme](https://raw.githubusercontent.com/ademozay/lugat/master/lugat.gif "Lügat")

## Nasıl Yüklenir?

pip (Python 3) ile

```sh
pip install lugat
```

Docker ile kullanmak isterseniz aşağıdaki fonksiyonu profil dosyanıza(.bash_rc, .zsh_rc vb.) ekleyebilirsiniz.

```sh
function lugat() {
	docker run -it --rm ademozay/lugat $@
}
```

## Nasıl Kullanılır?

Komut satırında

```sh
lugat <kelime, atasözü, deyim vb.>

# Atasözleri, deyimler, birleşik fiiller ve birleşik kelimeler gibi detaylar için

lugat -h <kelime, atasözü, deyim vb.>
```

Python paketi olarak

```python
from lugat import lookup, LookupException

try:
    word        = lookup(search)
    variations  = word.get_variations() # kelimenin tüm varyasyonları

    for v in variations:
        print(v.name) # varyasyonun özel ismi
        print(v.origin) # kelimenin kökeni
        print(v.meanings) # özellikleri ve örnekleriyle birlikte kelimenin anlamları
        print(v.compound_words) # ilgili birleşik kelimeler
        print(v.proverbs) # ilgili atasözleri, deyimler ve birleşik fiiller

except LookupException:
    pass

```

`Alfred` ile

[Lugat.alfredworkflow](<https://github.com/ademozay/lugat/releases/download/0.2.0/Lugat.alfredworkflow>)'u indirip kurduktan sonra bir kısayol atamanız gerekecek. 
Ben `Option + Shift + L` kombiyasyonunu kullanıyorum. Eğer kısayol atamak istemezseniz, Alfred'e `lügat` yazdıktan sonra yine arama yapabilirsiniz.

`Command + L` kısayolu ile, Alfred ekranına sığmayan tanımları ve kullanım örneklerini `Large Type` ile görüntüleyebilirsiniz.

`Command + Enter` kısayolu ile, ilgili sonuçları terminalde görüntüleyebilirsiniz.

Sistemde seçili olan bir kelimeyi direkt olarak aramak istediğiniz takdirde; Alfred kısayolunu ayarladığınız pencerede, `Argument` için `Selection on macOS` seçili olmalı.

[![Lügat | Alfred](https://raw.githubusercontent.com/ademozay/lugat/master/alfred_thumbnail.jpg)](https://www.youtube.com/watch?v=YSDX0bgr5Zk "Lügat | Alfred")

*Not: [Alfred](alfredapp.com), yalnızca macOS üzerinde çalışan bir üretkenlik uygulaması, başarılı bir Spotlight alternatifi.*