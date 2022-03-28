# Програмний модуль narrativesRetrival | Вступ

**Програмний модуль narrativesRetrival – "Програмний модуль виокремлення ключових термінів (слів і словосполучень) з тематичних інформаційних потоків для подальшого пошуку наративів"**, який написаний мовою програмування `Python`, призначений для попередньої обробки природомовних текстових даних тематичних інформаційних потоків (за замовчуванням доступні українська, російська та англійська мовні моделі), що включає токенізацію тексту та видалення стоп-слів, і подальше виокремлення ключових слів і словосполучень за допомогою застосування більш широкої обробки природної мови, що базується на розбитті на частини мови – [Part-of-speech tagging](https://www.sketchengine.eu/blog/pos-tags/), та кінцевого статистичного зважування та ранжування термінів за частотою їх появи у тексті для подальшого виявлення наративів.


### Зміст
- [Позначення та найменування програмного модуля](#name)
- [Програмне забезпечення, необхідне для функціонування програмного модуля](#software)
- [Функціональне призначення](#function)
- [Опис логічної структури](#structure)
- [Використовувані технічні засоби](#hardware)
- [Виклик та завантаження](#run)
- [Вхідні дані](#inputdata)
- [Вихідні дані](#outputdata)

<a name="name"></a>
<h2>Позначення та найменування програмного модуля</h2>

Програмний модуль має позначення **"narrativesRetrival"**.

Повне найменування програмного модуля – **"Програмний модуль виокремлення ключових термінів (слів і словосполучень) з тематичних текстових потоків"**.

<a name="software"></a>
<h2>Програмне забезпечення, необхідне для функціонування програмного модуля</h2>

Для функціонування програмного модуля, написаного мовою програмування `Python`, необхідне наступне програмне забезпечення, пакети та моделі:

- `Docker` [v20.10](https://docs.docker.com/engine/release-notes/#version-2010)
- `Kubernetes` [v1.22.4](https://github.com/kubernetes/kubernetes/releases/tag/v1.22.4)
- `python 3.8.0` or newer [v3.8.0](https://www.python.org/downloads/release/python-380/)
- `importlib` [v1.0.4](https://pypi.org/project/importlib/1.0.4/)
- `pyMorphy2` [0.9.1](https://pypi.org/project/pymorphy2/0.9.1/)
- `Stanza` [v1.3.0](https://pypi.org/project/stanza/1.3.0/)
- `NLTK` [v3.7](https://pypi.org/project/nltk/3.7/)
- `SpaCy` [v3.2.3](https://pypi.org/project/spacy/3.2.3/)
- `Stop-words` [v.2018.7.23](https://pypi.org/project/stop-words/2018.7.23/)
- `fastText` [v9.0.2](https://github.com/facebookresearch/fastText)
- [lid.176.ftz](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz) — модель бібліотеки `fasttext` для ідентифікації [176 мов](https://fasttext.cc/docs/en/language-identification.html#list-of-supported-languages) 
- [uk](https://pymorphy2.readthedocs.io/en/stable/user/guide.html), [ru](https://pymorphy2.readthedocs.io/en/stable/user/guide.html), [en](https://stanfordnlp.github.io/stanza/available_models.html) моделі для відповідно української, російської та англійської мов, що використовуються програмним модулем за замовчуванням.

<a name="function"></a>
<h2>Функціональне призначення</h2>

Програмний модуль **"narrativesRetrival"** призначений для попередньої обробки природомовних текстових даних тематичних інформаційних потоків (за замовчуванням доступні українська, російська та англійська мовні моделі), що включає токенізацію тексту та видалення стоп-слів, і подальше виокремлення ключових слів і словосполучень з тематичних текстових потоків за допомогою застосування більш широкої обробки природної мови, що базується на розбитті на частини мови – [Part-of-speech tagging](https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html), та кінцевого статистичного зважування та ранжування термінів за частотою їх появи у тексті для подальшого пошуку наративів.

<a name="structure"></a>
<h2>Опис логічної структури</h2>

Програмний модуль складається з частин:
- `main.py` — головного скрипта, що викликає наступні підмодулі:
	- `defaultConfigLoader.py` — підмодуль, що здійснює обробку файлу конфігурацій `config.json` і складається з наступних функцій:
		- `load_default_languages()` — функції обробки поля з тегом `langConfig` та присвоєння відповідних мовних моделей для обробки тексту, що має визначену мітку мови
		- `default_int_value()` — функції обробки полів з тегом `minMessLength` та `maxMessLength` та присвоєння, відповідно, мінімальної та максимально заданої довжини текстового повідомлення
		- `load_default_ngrams() ` — функції обробки поля з тегом `nGrams` для визначення типів термінів, які необхідно обробити та подати у якості вихідних даних як результат роботи програмного модуля **"narrativesRetrival"**
	- `packagesInstaller.py` — підмодуль, що відповідає за перевірку та завантаження необхідних програмних бібліотек, модулів та підмодулів, і складається з наступних функцій:
		- `setup_packeges()` — функції завантаження та установки необхідних для коректного функціонування програмного модуля **"narrativesRetrival"**, бібліотек та пакетів
	- `defaultModelsLoader.py` — підмодуль, що призначений для завантаження мовних моделей, які визначені за замовчуванням для кожної із мов у файлі конфігурацій `config.json` або у списку мов за замовуванням (у випадку відсутності файла `config.json` чи виникнення проблем з його зчитуванням та обробкою), і містить наступні функції:
		- `load_default_models()` — функцію завантаження мовних моделей тих бібліотек, які визначені за замовчуванням у файлі конфігурацій `config.json` (у випадку відсутності файла `config.json` чи виникнення проблем з його зчитуванням та обробкою - у списку мов за замовуванням) для кожної із мов (зокрема мовні моделі бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/), [NLTK](https://pypi.org/project/nltk/3.7/), [SpaCy](https://pypi.org/project/spacy/3.2.3/), [Stanza](https://pypi.org/project/stanza/1.3.0/)). У випадку, коли список мов та відповідних їм моделей порожній чи невизначений, то в інтерактивному режимі пропонується задати цей список вручну, вказавши мову та бібліотеку для мовної моделі (наприклад, [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/), [NLTK](https://pypi.org/project/nltk/3.7/), [SpaCy](https://pypi.org/project/spacy/3.2.3/) чи [Stanza](https://pypi.org/project/stanza/1.3.0/)) розділивши ці вхідні дані знаком `:`. Ця функція використовує наступні підфункції завантаження відповідних мовних моделей:
			- `pymorphy2_model_loader()` — функцію завантаження мовної моделі бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/) для української або російської мови
			- `nltk_model_loader()` — функцію завантаження мовної моделі бібліотеки [NLTK](https://pypi.org/project/nltk/3.7/) для англійської мови 
			- `spacy_model_loader()` — функцію завантаження мовних моделей бібліотеки [SpaCy](https://pypi.org/project/spacy/3.2.3/) для [широкого набору мов](https://spacy.io/usage/models#languages)
			- `stanza_model_loader()` — функцію завантаження овних моделей бібліотеки [Stanza](https://pypi.org/project/stanza/1.3.0/)) для [широкого набору мов](https://stanfordnlp.github.io/stanza/available_models.html#available-ud-models)
	- `defaultSWsLoader.py` — підмодуль, що призначений для завантаження списків стоп-слів, які визначені за замовчуванням для кожної із мов у файлі конфігурацій `config.json` або у списку мов за замовуванням (у випадку відсутності файла `config.json` чи виникнення проблем з його зчитуванням та обробкою), і містить наступні функції:
		- `load_default_stop_words()` — функцію завантаження завантаження списків стоп-слів, які визначені за замовчуванням для кожної із мов у файлі конфігурацій `config.json` (у випадку відсутності файла `config.json` чи виникнення проблем з його зчитуванням та обробкою - у списку мов за замовуванням) для кожної із мов (зокрема доступні користувацькі стоп-словники для української, росфйської, англійської, китайської та івриту). У випадку, коли список мов порожній чи невизначений, то в інтерактивному режимі пропонується задати цей список вручну, вказавши мову та бібліотеку для мовної моделі (наприклад, [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/), [NLTK](https://pypi.org/project/nltk/3.7/), [SpaCy](https://pypi.org/project/spacy/3.2.3/) чи [Stanza](https://pypi.org/project/stanza/1.3.0/)) розділивши ці вхідні дані знаком `:`. Ця функція використовує наступні підфункції завантаження відповідних мовних моделей:
			- `load_stop_words()` — функцію завантаження стоп-слів для списку мов, визначених вручну
	- `textProcessor.py` — підмодуль, що відповідає за комп'ютеризовану обробку вхідного природомовного тексту, і містить наступні функції:
		- `lang_detect()` — функцію визначення мови вхідного тексту за допомогою бібліотеки `FastText`
		- `append_lang()` — функцію додавання нової мови у список мов, визначених за замовчуванням — функція розширення списку мов, що визначені за замовчуванням
		- `pymorphy2_nlp()` — функцію комп'ютеризованої обробки вхідного тексту відповідною мовною моделлю з використанням [Pipeline](https://pymorphy2.readthedocs.io/en/stable/user/guide.html#id3) конвеєра бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/) та більш широкої обробки природної мови, що базується на розбитті на частини мови – [Part-of-speech tagging](https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html), для побудови слів, біграм та триграм:
			- `pymorphy2_built_words()` - функція побудови та виокремлення слів отриманих після обробки тексту відповідною моделлю бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/)
			- `pymorphy2_built_bigrams()` - функція побудови біграм за визначеними шаблонами із виокремлених на попередньому етапі слів
			- `pymorphy2_built_threegrams()` - функція побудови триграм за визначеними шаблонами із виокремлених на попередньому етапі слів
		- `stanza_nlp()` — функцію комп'ютеризованої обробки вхідного тексту відповідною мовною моделлю з використанням [Pipeline](https://stanfordnlp.github.io/stanza/pipeline.html) конвеєра бібліотеки [Stanza](https://pypi.org/project/stanza/1.3.0/) та більш широкої обробки природної мови, що базується на розбитті на частини мови – [Part-of-speech tagging](https://stanfordnlp.github.io/stanza/pos.html), для побудови слів, біграм та триграм:
			- `stanza_built_words()` - функція побудови та виокремлення слів отриманих після обробки тексту відповідною моделлю бібліотеки [Stanza](https://pypi.org/project/stanza/1.3.0/)
			- `stanza_built_bigrams()` - функція побудови біграм за визначеними шаблонами із виокремлених на попередньому етапі слів
			- `stanza_built_threegrams()` - функція побудови триграм за визначеними шаблонами із виокремлених на попередньому етапі слів
	- `termsExtractor.py` — підмодуль, що здійснює статистичне зважування термінів (слів, біграм і триграм) за частотою їх появи у тексті, і містить наступні функції:
		- `pymorphy2_most_freq_key_terms()` — функцію визначення найбільш частотних слів, біграм і триграм отриманих в результаті обробки відповідною мовною моделлю бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/) та виокремлення `top`-списку цих термінів (за замовчуванням `top = 12` — топ 12 слів, топ 12 біграм та топ 12 триграм)
		- `pymorphy2_most_freq()` — функцію визначення найбільш частотних термінів отриманих в результаті обробки відповідною мовною моделлю бібліотеки [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/) та формування повного списку цих термінів
		- `stanza_most_freq_key_terms()` — функцію визначення найбільш частотних слів, біграм і триграм отриманих в результаті обробки відповідною мовною моделлю бібліотеки [Stanza](https://pypi.org/project/stanza/1.3.0/) та виокремлення `top`-списку цих термінів (за замовчуванням `top = 12` — топ 12 слів, топ 12 біграм та топ 12 триграм)
		- `stanza_most_freq()` — функцію визначення найбільш частотних термінів отриманих в результаті обробки відповідною мовною моделлю бібліотеки [Stanza](https://pypi.org/project/stanza/1.3.0/) та формування повного списку цих термінів
		- `get_key()` - допоміжна фунція знаходження в словнику ключа за вказаним значенням

- Набіру програмних команд для зчитування вхідного текстового файлу
- Функціоналу, що забезпечує розбиття вхідного текстового файлу на окремі повідомлення за тригером `***`
- Виводу даних за допомогою команди `print` у стандартний вихідний потік (повідомлення про помилки та інші інформаційні сповіщення про результати роботи програмного модуля виводяться у `output.log`)

Програмний модуль **"narrativesRetrival"** зчитує вхідний текстовий файл за допомогою функцій `Pipeline` відповідних бібліотек [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/), [NLTK](https://pypi.org/project/nltk/3.7/), [SpaCy](https://pypi.org/project/spacy/3.2.3/) чи [Stanza](https://pypi.org/project/stanza/1.3.0/) та здійснює послідовну обробку отриманого на вхід природомовного тексту, будує та виокремлює ключові слова, біграми та триграми за визначеними шаблонами, здійснює їх статистичне зважування за частотою появи у тексті, й наприкінці здійснює вивід найбільш частотних термінів у вигляді списку слів, біграм та триграм поданих у нормальній словниковій формі (для триграм третій елемент не нормалізується) та їх найчастотніших ненормалізованих вхідних форм в тому вигляді, в якому вони зустрічаються у вхідному тексті повідомлення.


<a name="hardware"></a>
<h2>Використовувані технічні засоби</h2>

Програмний модуль експлуатується на сервері (або у хмарі серверів) під управлінням операційної системи типу `Linux` (64-х разрядна). В основі управління всіх сервісів є система оркестрації `Kubernetes`, де всі контейнери працюють з використанням `Docker`.


<a name="run"></a>
<h2>Виклик та завантаження</h2>

Для серверів, які працюють під керівництвом операційних систем сімейства `Windows OS`, виклик програмної системи **"narrativesRetrival"** здійснюється шляхом запуску скрипта `ім'я скрипта.py` з використанням команди `python`. Потрібно відкрити командний рядок – термінал `cmd` та написати `python ім'я скрипта.py`. Важливо, щоб скрипт знаходився або в директорії, з якої запущено командний рядок, або в каталозі, прописаному у змінній середовища `PATH`. 
Тож завантаження програмної системи забезпечується введенням в командному рядку повного імені завантажувальної програми з додатковим параметром - повним іменем вхідного файлу `ім'я вхідного файлу.txt`, який необхідно опрацювати:
```cmd
python main.py fullpath/.../input.txt
```

Для серверів, які працюють під керівництвом `Unix`-подібних операційних систем (наприклад, `Linux`) також можна скористатися цим способом, але на початку скрипта `Python` у першому рядку має бути вказаний повний шлях до інтерпретатора:
``` cmd
#!/usr/bin/python3
```
або
``` cmd
#!/usr/bin/env python3
```
Після цього необхідно дозволити запуск файлу (зробити його виконуваним).
``` cmd
chmod u+x main.py
```
Тепер просто запустити скрипт, ввівши в термінал його ім'я, перед яким додати «./»:
``` cmd
./main.py
```

В результаті запуску скрипта `main.py` програмного модуля **"narrativesRetrival"**  здійснюється зчитування вхідного потоку текстових даних розділених символом `***` за допомогою функцій `Pipeline` відповідних бібліотек [pymorphy2](https://pypi.org/project/pymorphy2/0.9.1/), [NLTK](https://pypi.org/project/nltk/3.7/), [SpaCy](https://pypi.org/project/spacy/3.2.3/) чи [Stanza](https://pypi.org/project/stanza/1.3.0/) та послідовна обробка отриманого на вхід природомовного тексту, побудова та виокремлення ключових слів, біграм та триграм, їх статистичне зважування за частотою появи у тексті, й наприкінці здійснюється вивід у стандартний вихідний потік найбільш частотних термінів у вигляді списку слів, біграм та триграм поданих у нормальній словниковій формі (для триграм третій елемент не нормалізується) та їх найчастотніших ненормалізованих вхідних форм в тому вигляді, в якому вони зустрічаються у вхідному тексті повідомлення.

За замовчуванням, дані, отримані в результаті застосування програмної системи, виводяться в консолі `cmd`. Також вивід може перенаправлятися із консолі у файл, який зберігаюється у дирикторії `results` у вигляді `.txt` файла. Для цього використовується оператор `>`.
Повна команда виглядає так:
```cmd
python main.py fullpath/.../input.txt > output.txt
```
Тут `output.txt` – це текстовий файл, у який записується результат виконання скрипта.

Операція може використовуватися як в операційній системі `Windows OS`, так і в `Unix`-подібних системах.
Якщо файла, в який повинен вивестися результат, не існує – система створить його автоматично.
При використанні оператора `>` вміст файлу, в який відображаються дані, повністю перезаписується. Якщо наявні дані потрібно зберегти, а нові дописати до існуючих, то використовується оператор `>>`:
```cmd
python main.py fullpath/.../input.txt >> output.txt
``` 

<a name="inputdata"></a>
<h2>Вхідні дані</h2>

Формат вхідних даних - текстовий.
Вхідний текстовий файл формату `.txt` містить тексти інформаційних повідомлень розділених символом `***` та має наступний вигляд:
```txt
вхідний текст 1
***
вхідний текст 2
***
.
.
.
***
вхідний текст n
***
```

<a name="inputdata"></a>
<h2>Вихідні дані</h2>

Формат вихідних даних - текстовий.
Перший рядок - текст вхідного інформаційного повідомлення, яке було опрацьовано програмним модулем **"narrativesRetrival"**; наступні - найбільш частотні терміни у вигляді списку слів, біграм та триграм поданих у нормальній словниковій формі (для триграм третій елемент не нормалізується) та їх найчастотніших ненормалізованих вхідних форм в тому вигляді, в якому вони зустрічаються у вхідному тексті повідомлення. всі рядки мають відповідні теги:

```txt
<content></content>
<Words></Words>
<Source Words>/Source Words>
<Bigrams>/Bigrams>
<Source Bigrams></Source Bigrams>
<Threegrams></Threegrams>
<Source Threegrams></Source Threegrams>
```

Біграми та триграми подаються з розмежуванням їх складових слів за допомогою символа нижнього підкреслення, тобто у наступному вигляді:
- для біграм: `слово1_слово2`
- для триграм: `слово1_слово2_слово3`


Вихідний потік має наступний вигляд: 
```txt
<content>вхідний текст 1</content>
<Words>слово, слово2, ..., слово12</Words>
<Source Words>слово, слово2, ..., слово12</Source Words>
<Bigrams>біграма1, біграма2, ..., біграма12</Bigrams>
<Source Bigrams>біграма1, біграма2, ..., біграма12</Source Bigrams>
<Threegrams>триграма1, триграма2, ..., трирама12</Threegrams>
<Source Threegrams>триграма1, триграма2, ..., трирама12</Source Threegrams>
***
<content>вхідний текст 2</content>
<Words>слово, слово2, ..., слово12</Words>
<Source Words>слово, слово2, ..., слово12</Source Words>
<Bigrams>біграма1, біграма2, ..., біграма12</Bigrams>
<Source Bigrams>біграма1, біграма2, ..., біграма12</Source Bigrams>
<Threegrams>триграма1, триграма2, ..., трирама12</Threegrams>
<Source Threegrams>триграма1, триграма2, ..., трирама12</Source Threegrams>
***
.
.
.
***
<content>вхідний текст n</content>
<Words>слово, слово2, ..., слово12</Words>
<Source Words>слово, слово2, ..., слово12</Source Words>
<Bigrams>біграма1, біграма2, ..., біграма12</Bigrams>
<Source Bigrams>біграма1, біграма2, ..., біграма12</Source Bigrams>
<Threegrams>триграма1, триграма2, ..., трирама12</Threegrams>
<Source Threegrams>триграма1, триграма2, ..., трирама12</Source Threegrams>
***
```

© 2022 [Oleh Dmytrenko](https://github.com/OlehDmytrenko)


