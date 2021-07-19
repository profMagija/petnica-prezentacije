---
marp: true
style: |
    h1, h2, h3, h4, h5, h6 {
        font-family: "Cascadia Code";
        color: white;
        font-weight: 300;
    }

    * {
        font-family: "Cascadia Code";
    }

    section {
        background: black;
        color: white;
    }
    
    section::after {
        font-family: "Cascadia Code";
    }

    pre {
        color: black;
    }
---

# vizualizacija podataka

---
<!--
footer: vizualizacija / nikola bebić / petnica / 2020
paginate: true
-->

# šta je to podatak ?

---

## tipovi podataka

- nominalni
- numerički
  - diskretni
  - kontinualni

---
<!-- 
# šta je to statistika ?

---

# statistička terminologija

- prosek `[mean]` - srednja vrednost
- medijana `[median]` - vrednost u sredini
- modus `[mode]` - najčešća vrednost

---

# statistička terminologija

- std. devijacija - $\sigma^2 = \sum \left(x_i - \bar x\right)^2$
- skg `[mse]` - $\frac {\sigma^2}{n}$
- korelacija
  - pirson: $\rho = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sigma^2_x \sigma^2_y}$ 

---
-->

# šta je vizualizacija ?

---

# tipovi grafika
- dvodimenzionalni
- trodimenzionalni
- n-dimenzionalni ?

---

## bar plot

* nom x kont

![bg right fit](./bar_plot.png)

---

## line plot

* dis -> kont
* kont -> kont

![bg right fit](./list_plot.png)

---

## pie plot

* nikad

![bg right fit](./pie_plot.png)

---

## histogram

* [ kont ]

![bg right fit](./hist_plot.png)

---

## scatter plot

* [ kont x kont ]

![bg right fit](./scatter_plot.png)

---

## scatter plot ++

- [ kont x kont x kont ]

![bg right fit](scatter_plot_2.png)

---

## scatter plot +++

- ...

![bg right fit](scatter_plot_3.png)

---

## scatter plot ++++

- ...

![bg right fit](scatter_plot_4.png)

---

## box plot

* [ kont ]
* bitna raspodela

![bg right fit](./box_plot.png)

---

### box plot - explained

![right bg fit](./box_explained.png)

---

## violin plot

* [ kont ]
* ***bitna*** raspodela

![bg right fit](./violin_plot.png)

---

## serijski podaci

* nom -> ...
* nom x ...

![bg right fit](./list_plot_multi.png)

---


## podaci sa greškama

![bg right fit](./error_plot.png)

---

## heatmap

* (nom x nom) -> kont

![bg right fit](./heatmap.png)

---

## 3d plot

* nikad

![bg right fit](./plot3d.png)

---

## contour plot

* (kont x kont) -> kont

![bg right fit](./contour_plot.png)

---

# linearni fit

![bg right fit](./lin_fit.png)

---

# više plotova odjednom

---

![bg fit](./penguins.png)

---

![bg fit](./iris.png)

---

# "friziranje" podataka

---

## simpsonov paradoks

---

![bg fit](./simpson.png)

---

## p-fitovanje

---

![bg fit](./p_fit.png)