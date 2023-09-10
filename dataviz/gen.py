import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


tips = sns.load_dataset("tips").dropna()
peng = sns.load_dataset("penguins").dropna()
flights = sns.load_dataset("flights").dropna()
fmri = sns.load_dataset("fmri").dropna()

gentoos = peng[peng.species == "Gentoo"]

np.random.seed(2)


def start_new(dpi=160, aspect=0.5):
    plt.figure(num=1, figsize=(1920 / dpi * aspect, 1080 / dpi), dpi=dpi)


def save(name):
    plt.savefig(name)
    plt.close()


plt.style.use(["dark_background", "./boxxx.mplstyle"])


# print(tips[["total_bill", "tip"]].head(10))

start_new()
sns.scatterplot(data=tips, x="total_bill", y="tip")
save("./example_plot.png")

start_new()
sns.barplot(
    data=peng,
    x="island",
    y="body_mass_g",
    errwidth=1,
    errcolor="1",
    capsize=0.3,
)
save("./bar_plot_1.png")

start_new()
sns.barplot(
    data=peng,
    x="island",
    y="body_mass_g",
    hue="sex",
    errwidth=1,
    errcolor="1",
    capsize=0.3,
)
save("./bar_plot_2.png")

start_new()
sns.lineplot(
    data=fmri.query("region == 'frontal' & event == 'stim' & subject == 's13'"),
    x="timepoint",
    y="signal",
)
save("./line_plot_1.png")

start_new()
sns.lineplot(
    data=fmri.query("region == 'frontal' & subject == 's13'"),
    x="timepoint",
    y="signal",
    hue="event",
)
save("./line_plot_2.png")


start_new()
sns.scatterplot(
    data=peng,
    x="body_mass_g",
    y="bill_length_mm",
)
save("./scatter_plot_1.png")

start_new()
sns.scatterplot(
    data=peng,
    x="body_mass_g",
    y="bill_length_mm",
    hue="species",
)
save("./scatter_plot_2.png")

start_new()
sns.scatterplot(
    data=peng,
    x="body_mass_g",
    y="bill_length_mm",
    hue="species",
    style="sex",
    size="sex",
)
save("./scatter_plot_3.png")

start_new()
sns.histplot(data=peng, x="flipper_length_mm", binwidth=3)
save("./hist_plot_1.png")

start_new()
plt.pie([40, 30, 10, 20], labels=["a", "b", "c", "d"])
save("./pie_plot.png")


start_new()
bp = sns.barplot(
    x=["jan", "jun", "dec"],
    y=[20.7, 20.3, 20.2],
)
bp.set_ylim((20, 21))
save("./malicious.png")
