STATUS_BAR_TIMEOUT = 2500

MAX_STRING_LENGTH = 45000

INIT_AXIOM = "X"
INIT_THEOREMS = {
    "X": "-YF+XFX+FY-",
    "Y": "+XF-YFY-FX+"
}
INIT_DELTA_ANGLE = 90
INIT_LINE_LENGTH = 10

CASH_SIZE = 16

L_SYSTEM_HELP_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" 
"http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }
</style></head>
<body style=" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; 
-qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:16pt;">
l-системы</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; 
text-indent:0px;">
<span style=" font-family:'MS Shell Dlg 2'; font-size:14pt; font-style:italic;">L-система</span>
<span style=" font-family:'MS Shell Dlg 2'; font-size:14pt;"> - система переписывания и вид формально
й графики. Она состоит из:</span></p>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 1;">
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
 <span style=" font-style:italic;">Алфавита</span> - используемых символов</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-style:italic;">Аксиомы</span> - начальной строки</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-style:italic;">Теорем</span> - правил подстановки определяющих, каким образом
 символы могут быть заменёны комбинациями символов</li></ul>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;
 text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:14pt;">Символам алфавита
  соответствуют команды для отрисовки графики</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;
 text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:14pt;">Пример L-системы
  (для кривой Коха):</span></p>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 1;"><li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" 
style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0;
text-indent:0px;">Теоремы: F-F++F-F</li>
<li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:12px; margin-bottom:12px; 
margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Аксиома: </span><span style=" font-size:14pt;">F</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
1-ая итерация: <span style=" text-decoration: underline;">F</span> -&gt; 
<span style=" text-decoration: underline;">F-F++F-F</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
2-ая итерация: <span style=" text-decoration: underline;">F</span>-
<span style=" text-decoration: underline;">F</span>++
<span style=" text-decoration: underline;">F</span>-
<span style=" text-decoration: underline;">F</span> -&gt; 
<span style=" text-decoration: underline;">F-F++F-F</span>-
<span style=" text-decoration: underline;">F-F++F-F</span>++
<span style=" text-decoration: underline;">F-F++F-F</span>-
<span style=" text-decoration: underline;">F-F++F-F</span></li></ul></body></html>"""

WORK_WITH_PROGRAM_HELP_HTML = f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" 
"http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">p, li {'{white-space: pre-wrap;}'}
</style></head>
<body style=" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;">
<p align="center" 
style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; 
-qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:16pt;">
Работа с программой</span></p>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 1;">
<li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:12px; margin-bottom:12px; 
margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Изменить конфигурацию L-системы: меню &quot;Фрактал&quot; -&gt; &quot;
Изменить конфигурацию&quot;</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Сохранить изображение: меню &quot;Фрактал&quot; -&gt; &quot;Сохранить в файл&quot;</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Смена итерации: кнопки со стрелками под изображением</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Максимально возможная итерация зависит от скорости увеличения длины L-строки: I
<span style=" vertical-align:sub;">max</span> = I<span style=" vertical-align:sub;">
первая, на которой длина l-строки &gt;= {MAX_STRING_LENGTH}</span> + 1</li></ul></body></html>"""

GRAPHIC_COMMANDS_HELP_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" 
"http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">p, li { white-space: pre-wrap; }
</style></head>
<body style=" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; 
-qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:16pt;">
Графические команды</span></p>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 1;">
<li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:12px; margin-bottom:12px; 
margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt; font-weight:600;">F, G</span><span style=" font-size:14pt;">
 нарисовать линию и переместить перо</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">f, g</span> переместить перо, не рисуя линию</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">+ </span>повернуть на заданный угол по часовой стрелке</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">-</span> повернуть на заданный угол против часовой стрелки</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">|</span> повернуть на 180 градусов</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">[</span> сохранить текущее состояние пера (координаты, угол поворота)
 в стеке</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">] </span>загрузить состояние пера из стека</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:12px; 
margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Остальные символы не соответствуют каким либо командам</li></ul></body></html>"""

FRACTALS_EXAMPLES_HELP_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" 
"http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">p, li { white-space: pre-wrap; }
</style></head>
<body style=" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; 
-qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:16pt;">
Примеры фракталов</span></p>
<ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 1;">
<li style=" font-family:'MS Shell Dlg 2';" 
style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; 
text-indent:0px;"><span style=" font-size:14pt;">Треугольник Серпинского</span>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 2;"><li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Аксиома: F-G-G</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Теоремы: F -&gt; F-G+F+G-F; G -&gt; GG</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Угол поворота: 120 градусов</li></ul></li>
<li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:0px; margin-bottom:0px; 
margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Кривая Коха</span>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 2;"><li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Аксиома: F</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Теоремы: F-F++F-F</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Угол поворота: 60 градусов</li></ul></li>
<li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:0px; margin-bottom:0px; 
margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Дерево Пифагора</span>
<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; 
-qt-list-indent: 2;"><li style=" font-family:'MS Shell Dlg 2';" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:14pt;">Аксиома: ffffffffffffff--F (&quot;f&quot; в начале нужны для того,
 чтобы сместить изображение вправо, т.к. в программе на данный момент не предусмотрена возможность
  сместить начало координат)</span></li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; margin-bottom:0px;
 margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
 Теоремы: F -&gt; G[-F]+F; G -&gt; GG</li>
<li style=" font-family:'MS Shell Dlg 2'; font-size:14pt;" style=" margin-top:0px; 
margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
Угол поворота: 45 градусов</li></ul></li></ol></body></html>"""
