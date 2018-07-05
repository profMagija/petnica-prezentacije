<style>
  h1, h2, h3, h4, h5, h6 {
  	font-family: "Source Code Pro";
  }
  
  table {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>

# grafovi - ukratko
Nikola Bebić

---

# šta je to graf?

* gomila objekata povezanih vezama

---

# šta će nam graf

* grafovi se često sreću:
  * ljudi i poznanstva
  * gradovi i putevi
  * stranice na Webu
  * računari na nekoj mreži

---

# matematički graf

* skup *čvorova* (vertex / node) $V$ i grana (edge) $E$
* grana je par $uv$ pri čemu $u,v \in V$

---

# tipovi grafova

* **usmereni** vs **neusmereni**
* **obeleženi** vs **neobeleženi**
* **težinski** vs **netežinski**
* **prosti**, sa **petljama**, sa **multigranama**

---

# pojmovi u grafu

* susedi čvora $u$ - čvorovi sa kojima je $u$ povezan
* stepen čvora - broj suseda čvora
* mostovi, cut-vertexi

---

# specijalni tipovi grafova

* **šume** i **stabla** - grafovi bez ciklusa
* **potpuni grafovi** - grafovi gde izmedju svaka dva čvora postoji grana
* **hamiltonov**, **ojlerov**, ...\
* **podgraf**, indukovani podgraf

---

# stabla

* veoma korisna:
  * razapinjuće stablo: Prim i Kraskal
  * binarna (n-arna) stabla, ...

---

# graf u računarstvu

* skup nekih objekata
* objekti su u nekoj relaciji sa "susednim" objektima

---

# matrica susedstva

|     |1|2|3|4|
|-----|-|-|-|-|
|**1**|0|0|1|1|
|**2**|0|0|0|1|
|**3**|1|0|0|1|
|**4**|1|1|1|0|

---

# lista susedstva

```python
{
    1: [3, 4],
    2: [4],
    3: [1, 4],
    4: [1, 2, 3]
}
```
---

# algoritmi na grafovima

* BFS, DFS
* traženje najkraćeg puta: Dijkstra
* centrality

---

# problem: drustvene mreze

* mreže gde su ivice neke interakcije među čvorovima
* primeri: 
  * Facebook/Instagram/Twitter/...
  * Stranice na webu
  * Koautorstvo na radovima
* imaju slične osobine: power laws