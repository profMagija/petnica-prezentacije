import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
from mpl_toolkits.axes_grid1 import make_axes_locatable
import scipy.stats


peng = sns.load_dataset("penguins").dropna()

gentoos = peng[peng.species == 'Gentoo']

np.random.seed(2)


def normalize(x, a=0, b=1):
    return (x - np.min(x)) / (np.max(x) - np.min(x)) * (b - a) + a


def lin_fit_sa_greskom(x, y):
    """traži linearni fit sa greškom. Koristi algoritam za grešku najmanjih kvadrata [LS].
    vraća cetvorku (a, b, err_a, err_b):
      - a: koeficijent pravca
      - b: odsecak na y-osi
      - err_a: greska a
      - err_b: greska b

    Reference
    ---------
    .. [LS] Weisstein, Eric W. "Least Squares Fitting." 
            From MathWorld--A Wolfram Web Resource. 
            http://mathworld.wolfram.com/LeastSquaresFitting.html
    """

    # prvo nadjemo k (koef pravca), n (odsecak),
    (a, b), res, _, _, _ = np.polyfit(x, y, 1, full=True)

    # broj podataka
    n = x.shape[0]

    # x average
    x_bar = np.mean(x)

    # zbir kvadrata (x_i - x_avg)^2
    ss_xx = np.sum((x - x_bar)**2)

    s = np.sqrt(res / (n - 2))

    # greska koeficijenta pravca
    err_a = s / np.sqrt(ss_xx)

    # greska odsecka
    err_b = s * np.sqrt(1/n + (x_bar**2)/ss_xx)

    return a, b, err_a[0], err_b[0]


def flavia():
    iris = load_iris(as_frame=True)

    idata = iris.frame
    itypes = [0, 1, 2]
    colorz = plt.rcParams['axes.prop_cycle'].by_key()['color']
    iprops = iris.feature_names

    featmax = [idata[p].max() + 0.5 for p in iprops]

    start_new(100, 1)
    for i in range(4):
        for j in range(4):
            f = plt.subplot(4, 4, 4*i+j+1)

            if j == 0:
                f.set_ylabel(iprops[i])
            if i == 3:
                f.set_xlabel(iprops[j])

            if i == j:
                f.set_xlim((0, featmax[i]))
                for n in itypes:
                    ddd = idata[idata.target == n][iprops[i]]
                    # rh, lh = np.histogram(ddd, bins=6)
                    plt.hist(ddd, bins=6, histtype='step')
            elif i < j:
                f.set_xticks([])
                f.set_yticks([])
                w = -0.2
                cc = 0
                for n in itypes:
                    v = idata[idata.target == n].corr()[iprops[i]][iprops[j]]
                    printit(f, v, w, colorz[cc])
                    w += 0.2
                    cc += 1
            else:
                f.set_xlim((0, featmax[j]))
                f.set_ylim((0, featmax[i]))
                for n in itypes:
                    f.plot(
                        idata[idata.target == n][iprops[j]],
                        idata[idata.target == n][iprops[i]],
                        '.')
    plt.legend(iris.target_names)
    plt.savefig('./iris.png')
    plt.close()
    # plt.show()


def start_new(dpi=160, aspect=0.5):
    plt.figure(num=1, figsize=(1920/dpi * aspect, 1080/dpi), dpi=dpi)


def printit(ax, v, where, color):
    ax.text(
        0.5, 0.5 + where,
        f'{v:.2f}',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes,
        color=color)


plt.style.use(['dark_background', './boxxx.mplstyle'])

flavia()

start_new()
plt.bar(['a', 'b', 'c'], [5, 7, 8])
plt.savefig('./bar_plot.png')
plt.close()

start_new()
plt.plot([1, 2, 2.5, 3, 4], [5, 7, 6, 4, 5.5])
plt.savefig('./list_plot.png')
plt.close()

start_new()
plt.pie([40, 30, 10, 20], labels=['a', 'b', 'c', 'd'])
plt.savefig('./pie_plot.png')
plt.close()

start_new()
plt.hist(peng['body_mass_g'])
plt.savefig('./hist_plot.png')
plt.close()

start_new()
plt.plot(peng.body_mass_g, peng.bill_length_mm, '.')
plt.savefig('./scatter_plot.png')
plt.close()
start_new()
plt.scatter(
    peng.body_mass_g,
    peng.bill_length_mm,
    normalize(peng.bill_depth_mm, 1, 7)**2)
plt.savefig('./scatter_plot_2.png')
plt.close()
start_new()
plt.scatter(
    peng.body_mass_g,
    peng.bill_length_mm,
    normalize(peng.bill_depth_mm, 1, 7)**2,
    c=np.where(peng.species == 'Adelie', 0, np.where(peng.species == 'Gentoo', 1, 2)))
plt.savefig('./scatter_plot_3.png')
plt.close()
start_new()

p_male = peng[peng.sex == 'MALE']
p_female = peng[peng.sex == 'FEMALE']

plt.scatter(
    p_male.body_mass_g,
    p_male.bill_length_mm,
    normalize(p_male.bill_depth_mm, 1, 7)**2,
    c=np.where(p_male.species == 'Adelie', 0, np.where(
        p_male.species == 'Gentoo', 1, 2)),
    marker='^')
plt.scatter(
    p_female.body_mass_g,
    p_female.bill_length_mm,
    normalize(p_female.bill_depth_mm, 1, 7)**2,
    c=np.where(p_female.species == 'Adelie', 0, np.where(
        p_female.species == 'Gentoo', 1, 2)),
    marker='o')

plt.savefig('./scatter_plot_4.png')
plt.close()

start_new()
plt.boxplot([np.random.normal(0, s, 1000) for s in range(1, 6)])
plt.savefig('./box_plot.png')
plt.close()

start_new()
d = np.random.normal(0, 1, 10000)
plt.xlim((-4, 4))
p1 = plt.subplot(211)
p1.boxplot(d, vert=False)
p2 = plt.subplot(212)
p2.hist(d, bins=50)
plt.savefig('./box_explained.png')
plt.close()

start_new()
plt.violinplot([np.random.normal(0, s, 100) for s in range(1, 6)])
plt.savefig('./violin_plot.png')
plt.close()


start_new()
plt.plot([1, 2, 2.5, 3, 4], [5, 7, 6, 4, 5.5])
plt.plot([1, 2, 2.5, 3, 4], [6, 5, 7, 3, 0])
plt.plot([1, 2, 2.5, 3, 4], [2, 4, 9, 2, 4])
plt.plot([1, 2, 2.5, 3, 4], [4, 3, 4, 6, 8])
plt.savefig('./list_plot_multi.png')
plt.close()

start_new()
plt.errorbar([1, 2, 2.5, 3, 4],
             [5, 7, 6, 4, 5.5],
             [0.5, 0.5, 0.25, 0.25, 0.25],
             0.1)
plt.savefig('./error_plot.png')
plt.close()

start_new()
plt.title('title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.xlim((20, 80))
plt.ylim((-0.3, 0.3))

plt.plot(np.sinc(np.linspace(-6, 6, 100)))
plt.savefig('./extra_plot.png')
plt.close()


start_new()
sns.heatmap(np.random.normal(0, 3, (5, 5)) + 20 * np.eye(5))
plt.savefig('./heatmap.png')
plt.close()

start_new()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x = np.arange(-2, 2, 0.04)
y = np.arange(-2, 2, 0.04)
xx, yy = np.meshgrid(x, y)
z = np.sinc(xx**2 + yy**2)
print(xx.shape, yy.shape, z.shape)
ax.plot(xx.flatten(), yy.flatten(), z.flatten())
plt.savefig('./plot3d.png')
plt.close()


start_new()
plt.contourf(x, y, z)
plt.savefig('./contour_plot.png')
plt.close()


def scatter_histo(dx, dy, bins=25):
    fig, ax = plt.subplots(figsize=(1080/160, 1080/160), dpi=160)
    ax.plot(dx, dy, '.')
    divider = make_axes_locatable(ax)
    axx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax)
    axy = divider.append_axes("right", 1.2, pad=0.1, sharey=ax)
    axx.xaxis.set_tick_params(labelbottom=False)
    axy.yaxis.set_tick_params(labelleft=False)
    axx.hist(dx, bins=bins)
    axy.hist(dy, bins=bins, orientation="horizontal")
    plt.savefig('./penguins.png')
    plt.close()


scatter_histo(peng.body_mass_g, peng.bill_depth_mm)


def lin_fit_plot(dx, dy):
    sns.regplot(dx, dy)


start_new()
lin_fit_plot(
    gentoos.bill_length_mm,
    gentoos.bill_depth_mm)
plt.savefig('./lin_fit.png')
plt.close()

start_new(aspect=1)
plt.subplot(1, 2, 1)
lin_fit_plot(
    gentoos.bill_length_mm,
    gentoos.bill_depth_mm)
lin_fit_plot(
    peng[peng.species == 'Adelie'].bill_length_mm,
    peng[peng.species == 'Adelie'].bill_depth_mm)
lin_fit_plot(
    peng[peng.species == 'Chinstrap'].bill_length_mm,
    peng[peng.species == 'Chinstrap'].bill_depth_mm)
plt.subplot(1, 2, 2)
lin_fit_plot(
    peng.bill_length_mm,
    peng.bill_depth_mm)
plt.savefig('./simpson.png')
plt.close()


# STAT SIG

minp = 1
while minp > 0.01:
    fig, axs = plt.subplots(
        5, 9, sharex='all', sharey='all',
        figsize=(1920/160, 1080/160),
        dpi=160)
    axs = axs.flatten()
    xss = [np.random.normal(0, 1, 101) for _ in range(10)]
    cur = 1
    print(minp)
    for i in range(10):
        for j in range(i + 1, 10):
            xs = xss[i]
            ys = xss[j]

            slope, intercept, _r, pval, _stderr = scipy.stats.linregress(xs, ys)

            if pval < 0.05:
                c = 'g.'
            else:
                c = 'r.'
                
            minp = min(minp, pval)

            ax = axs[cur - 1]
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xlabel(f'{pval:.3f}')

            ax.plot(xs, ys, c, ms=3)
            ax.plot(xs, xs * slope + intercept, 'b-')
            cur += 1
plt.savefig('./p_fit.png')
plt.close()
