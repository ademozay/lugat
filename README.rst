lügat
=====

*lugat*, `TDK Güncel Türkçe Sözlük <https://sozluk.gov.tr>`_'ün komut satırı üzerinden kullanılmasını sağlar.

.. image:: https://raw.githubusercontent.com/ademozay/lugat/master/lugat.gif
    :alt: lugat önizlemesi
    :width: 100%
    :align: center
        
Nasıl Yüklenir
--------------
.. code:: shell
  
  pip3 install lugat
      
Nasıl Kullanılır
----------------                

* Komutun satırında

.. code:: shell
  
  lugat <kelime>

* Python uygulaması içinde

.. code:: python

  from lugat import lookup, LookupException

  try:
      word        = lookup(word)
      variations  = word.get_variations()

      for v in variations:
          print(v.name)
          print(v.origin)
          print(v.meanings)
          print(v.compound_words)
          print(v.proverbs)

  except LookupException:
      pass