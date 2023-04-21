---
marp: true
theme: my_black_style
author: nikola bebić
math: katex
---

# grafovi
Nikola Bebić / Petnica / 2023

---
<!--
footer: grafovi / Nikola Bebić / Petnica / 2023
paginate: true
-->

## šta je graf ?

* skup *čvorova* (vertices) $V$ i *ivica* (edges) $E \subseteq V^2$
  * ivica = par $uv$, pri čemu $u, v \in V$

---

## tipovi grafova

* **neusmereni** vs **usmereni**
* **ciklični** vs **aciklični**
* **netežinski** vs **težinski**
* **prosti** vs **sa petljama** vs **sa multigranama**

---

## susedstvo

* susedi čvora $u$ - čvorovi sa kojima je $u$ povezan
  $N(u) = \{ v \in V\ |\ uv \in E\}$
* stepen čvora $u$ - broj suseda
  $\delta(u) = |N(u)|$
* kod usmerenih grafova:
  * ulazni/izlazni susedi
  * ulazni/izlazni stepen

---

## putevi

* put -- niz čvorova $u_1u_2\dots u_n$, gde $u_iu_{i+1} \in E$
    * dužina puta = broj "koraka"
    * kod težinskih -- težina puta = zbir težina svih ivica
* ciklus -- put gde $u_1 = u_n$

---

## povezanost

* $u$ i $v$ su *povezani* ukoliko postoji put $u w_1 w_2\dots w_n v$
* graf je *povezan* ukoliko su svaka dva čvora povezana
* *povezane komponente* su maksimalni povezani podskupovi grafa

---

## stablo

* **stablo** je aciklični povezani neusmereni graf
    * uvek ima $n$ čvorova i $n-1$ ivicu
    * nije povezan - šuma

---

## usmereni aciklični graf
* **usmereni aciklični graf (DAG)** je usmereni aciklični graf

---

## podgraf

* **podgraf** grafa -- graf koji se sastoji od podskupa čvorova i podskupa ivica
    * **indukovani podgraf** -- podgraf koji "uzme" sve ivice između čvorova iz početnog grafa

---

## još neki tipovi grafova

* **kompletan graf** -- graf koji ima ivice između svaka svoja dva čvora
    * **klika** (*clique*) -- kompletan podgraf
* **bipartitan graf**

---
<!--
_paginate: false
_footer: ""
-->
# <center><font color="#444444">predah</font></center>

---

## šta je graf ?
* gomila stvari u medjusobnim relacijama 

---

## šta će nama graf ?
* dobar model za mnoge probleme
  * ljudi i međuljudski odnosi
  * mesta i putevi
  * web stranice i linkovi
  * pozicije u igri i potezi

---

## grafovi u računarstvu

* kako predstavljamo grafove?
    * matrica susedstva
    * lista susedstva

---

## algoritmi nad grafovima

* grafovski problem -> grafovsko rešenje

---

## najkraći put

* prost graf - BFS
* težinski graf - Dijstra
* sa heuristikom - A\*

---

## razapinjuće stablo (*spanning tree*)

* "odsečemo" "višak" ivica, tako da ostane stablo
    * minimalno = sa minimalnim ukupnim zbirom ivica
* Kruskal

---

## topološko sortiranje

* poređati čvorove DAG-a, tako da ivice idu "sa leva na desno"

---

## bojenje grafa

* dodeliti oznake (boje) čvorovima, tako da susedi uvek imaju različitu boju

---

## mečing (uparivanje)

* podeliti čvorove u disjunktne parove suseda
* maksimalni mečing -- u težinskom grafu, maksimizovati zbir težina uparenih ivica 

---

## graf toka (*flow graph*)

* težine u grafu = maksimalni protok
* koliki je ukupni protok u grafu
* *max-flow min-cut* algoritam

---

## kompleksne mreže

* veliki, netrivijalni grafovi (*mreže*)
  * društvene, biološke, tehničke, ...
* interesuju nas makroosobine same mreže, a ne mikroosobine čvorova

---

## problemi u kompleksnim mrežama

* prečnik mreže, prosečna dužina puta
* koeficijent klasterovanja
* centralnost
* pronalaženje društava, modularnost
* pronalaženje maksimalnih klika

---
<!--
_footer: ""
_paginate: false
-->

###### <center>fin</center>