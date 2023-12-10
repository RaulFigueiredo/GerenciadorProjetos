import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Plot:
    @staticmethod
    def set_style():
        plt.close()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().set_facecolor('#FFFFFF')
        plt.gcf().set_facecolor('#FFFFFF')
        plt.tick_params(axis='x', which='both', colors='grey', bottom=False,
                        top=False)
        plt.tick_params(axis='y', which='both', colors='grey', left=False,
                        right=False)
        plt.grid(True, linestyle='-', axis='y', linewidth=0.5,
                 color='grey', alpha=0.5)
    
    @staticmethod
    def make_lineplot(data, title):
        plt.close()
        x, y = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.plot(x, y)
        ax.scatter(x, y)
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_barplot(data, title):
        plt.close()
        sorted_ = sorted(data.items(), key=lambda item: item[1], reverse=True)
        labels = [i[0] for i in sorted_]
        values = [i[1] for i in sorted_]
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(labels, values, zorder=4)
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_areaplot(data, title):
        plt.close()
        x, y = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.fill_between(x, y, zorder=4, alpha=0.8)
        ax.plot(x, y, zorder=4, alpha=1)
        ax.set_xticks(ax.get_xticks()[::len(ax.get_xticks()) // 4])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        ax.set_title(title)
        Plot.set_style()
        return fig

    @staticmethod
    def make_pieplot(data, title):
        plt.close()
        labels, values = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        try:
            _, cat_labels, val_labels = ax.pie(values, labels=labels,
                                            autopct='%1.0f%%')
            for label in cat_labels:
                label.set_color('grey')
            for label in val_labels:
                label.set_fontsize(8)
                label.set_color('black')
        except:
            pass
        ax.set_title(title)
        return fig

    @staticmethod
    def make_donutplot(data, title):
        plt.close()
        labels, values = list(data.keys()), list(data.values())
        fig, ax = plt.subplots(figsize=(4, 3))
        try:
            _, cat_labels, val_labels = ax.pie(values, labels=labels,
                                            startangle=-40,
                                            wedgeprops=dict(width=0.4),
                                            autopct='%1.0f%%', pctdistance=0.8)
            for label in cat_labels:
                label.set_color('grey')
            for label in val_labels:
                label.set_fontsize(8)
                label.set_color('black')
        except:
            pass
        ax.set_title(title)
        return fig
