# Проект 1. Кто хочет стать миллионером кинопроката?

В рамках проекта необходимо решить 27 заданий с использованием датасета IMDB [[тыць тута](https://github.com/salnykov-se/SkillFactory/blob/master/module_1/movie_bd_v5.csv)]
## Общие комментарии по логике решения

Решения основывались на модифицированном датасете, в котором данные по жанрам, режисерам, актерам и кинокомпаниям были трансформированы в отсортированные в алфавитном порядке списки. При анализе для работы со списками использовалось два подхода:

 - **Метод1:** "Взрыв" датафреймов и сплит серий при помощи функций `df.explode()`и `series.split()` сответственно
 - **Метод2:** "Наивный" подход, при котором списки в датафрейме итерировались при помощи циклов
 
 В большинстве задач было использовано оба метода, но, поскольку Метод 1 является более быстрым и лаконичным, некоторые решения реализованы только при помощи этого метода.

## Результаты викторины

Было набрано 27 из 27 возможных баллов.

## Саморефлексия

### 1. Какова была ваша роль в команде? 
Команда была сплоченной и дружной. Задачи очень грамотно были распределены между коллективом. Каждый знал, что нужно делать. Жена регулярно ругалась, что я сижу в своем мире и забыл про семью, дети переодически выключали компьютер с несохраненным проектом, одни рыбки в аквариуме бездельничали и отвлекали своей бессмысленой болтовней.
### 2. Какой частью своей работы вы остались особенно довольны? 
Эволюцией решения от ресурсозатратного подхода с созданием дамми-переменных для категорий, режисеров и т.д. к более эффективному решению
### 3. Что не получилось сделать так, как хотелось? Над чем ещё стоит поработать? 
Не вместился в рекоммендованные 4 чача
### 4. Что интересного и полезного вы узнали в этом модуле? 
Изучил новые для себя функции

    

 - `df.explode()`
 - `series.split()`
 - `df.at()`

### 5. Что является вашим главным результатом при прохождении этого проекта? 
То, что я его сделал
### 6. Планируете ли вы менять стратегию изучения последующих модулей?
Нет, вроде все было познавательно и весело

## History



## Credits



## License
MIT License

Copyright (c) 2020 salnykov-se

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
